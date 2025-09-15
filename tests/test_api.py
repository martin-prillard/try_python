"""Tests for API layer - business functionality only."""

from fastapi.testclient import TestClient

from todo_app.api import app, get_service
from todo_app.repository import InMemoryTodoRepository
from todo_app.service import TodoService


class TestTodoAPI:
    """Test FastAPI endpoints."""

    def setup_method(self):
        """Set up test client for each test."""
        # Create a fresh repository and service for each test
        self.repo = InMemoryTodoRepository()
        self.service = TodoService(self.repo)
        
        # Override the dependency
        app.dependency_overrides[get_service] = lambda: self.service
        
        self.client = TestClient(app)
    
    def teardown_method(self):
        """Clean up after each test."""
        app.dependency_overrides.clear()

    def test_list_todos_empty(self):
        """Test listing todos when empty."""
        response = self.client.get("/todos")
        assert response.status_code == 200
        assert response.json() == []

    def test_list_todos_with_data(self):
        """Test listing todos with data."""
        # Create a todo first
        create_response = self.client.post(
            "/todos", json={"title": "Test Todo", "description": "Test description"}
        )
        assert create_response.status_code == 201

        # List todos
        response = self.client.get("/todos")
        assert response.status_code == 200
        todos = response.json()
        assert len(todos) == 1
        assert todos[0]["title"] == "Test Todo"
        assert todos[0]["description"] == "Test description"
        assert todos[0]["completed"] is False

    def test_create_todo_success(self):
        """Test creating a todo successfully."""
        payload = {"title": "Test Todo", "description": "Test description"}
        response = self.client.post("/todos", json=payload)

        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Test Todo"
        assert data["description"] == "Test description"
        assert data["completed"] is False
        assert "id" in data
        assert "created_at" in data

    def test_create_todo_minimal(self):
        """Test creating a todo with minimal data."""
        payload = {"title": "Test Todo"}
        response = self.client.post("/todos", json=payload)

        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Test Todo"
        assert data["description"] is None

    def test_create_todo_validation_error(self):
        """Test creating a todo with validation error."""
        payload = {"title": ""}  # Empty title should fail
        response = self.client.post("/todos", json=payload)

        assert response.status_code == 422

    def test_update_todo_success(self):
        """Test updating a todo successfully."""
        # Create a todo first
        create_response = self.client.post("/todos", json={"title": "Original Title"})
        todo_id = create_response.json()["id"]

        # Update it
        update_payload = {"title": "Updated Title", "completed": True}
        response = self.client.patch(f"/todos/{todo_id}", json=update_payload)

        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"
        assert data["completed"] is True
        assert data["id"] == todo_id

    def test_update_todo_not_found(self):
        """Test updating a non-existent todo."""
        update_payload = {"title": "Updated Title"}
        response = self.client.patch("/todos/999", json=update_payload)

        assert response.status_code == 404
        assert "Todo not found" in response.json()["detail"]

    def test_delete_todo_success(self):
        """Test deleting a todo successfully."""
        # Create a todo first
        create_response = self.client.post("/todos", json={"title": "Test Todo"})
        todo_id = create_response.json()["id"]

        # Delete it
        response = self.client.delete(f"/todos/{todo_id}")

        assert response.status_code == 204

        # Verify it's gone
        get_response = self.client.get("/todos")
        assert len(get_response.json()) == 0

    def test_delete_todo_not_found(self):
        """Test deleting a non-existent todo."""
        response = self.client.delete("/todos/999")

        assert response.status_code == 404
        assert "Todo not found" in response.json()["detail"]

    def test_multiple_todos_operations(self):
        """Test multiple todos operations."""
        # Create multiple todos
        todo1_response = self.client.post("/todos", json={"title": "Todo 1"})
        todo2_response = self.client.post("/todos", json={"title": "Todo 2"})

        assert todo1_response.status_code == 201
        assert todo2_response.status_code == 201

        # List all todos
        list_response = self.client.get("/todos")
        assert list_response.status_code == 200
        todos = list_response.json()
        assert len(todos) == 2

        # Update one todo
        todo1_id = todo1_response.json()["id"]
        update_response = self.client.patch(
            f"/todos/{todo1_id}", json={"completed": True}
        )
        assert update_response.status_code == 200

        # Delete one todo
        todo2_id = todo2_response.json()["id"]
        delete_response = self.client.delete(f"/todos/{todo2_id}")
        assert delete_response.status_code == 204

        # Verify final state
        final_list_response = self.client.get("/todos")
        final_todos = final_list_response.json()
        assert len(final_todos) == 1
        assert final_todos[0]["title"] == "Todo 1"
        assert final_todos[0]["completed"] is True