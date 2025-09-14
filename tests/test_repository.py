"""Tests for repository layer."""
import pytest
from datetime import datetime
from unittest.mock import patch

from todo_app.repository import InMemoryTodoRepository
from todo_app.models import TodoCreate, TodoUpdate, TodoInDB


class TestInMemoryTodoRepository:
    """Test InMemoryTodoRepository functionality."""

    def setup_method(self):
        """Set up test repository for each test."""
        self.repo = InMemoryTodoRepository()

    def test_initial_state(self):
        """Test repository initial state."""
        assert len(self.repo._data) == 0
        assert self.repo._next_id == 1

    def test_list_empty(self):
        """Test listing todos when repository is empty."""
        todos = self.repo.list()
        assert todos == []

    def test_create_todo(self):
        """Test creating a todo."""
        payload = TodoCreate(title="Test Todo", description="Test description")
        todo = self.repo.create(payload)
        
        assert todo.id == 1
        assert todo.title == "Test Todo"
        assert todo.description == "Test description"
        assert todo.completed is False
        assert isinstance(todo.created_at, datetime)
        assert len(self.repo._data) == 1
        assert self.repo._next_id == 2

    def test_create_multiple_todos(self):
        """Test creating multiple todos."""
        payload1 = TodoCreate(title="Todo 1")
        payload2 = TodoCreate(title="Todo 2")
        
        todo1 = self.repo.create(payload1)
        todo2 = self.repo.create(payload2)
        
        assert todo1.id == 1
        assert todo2.id == 2
        assert len(self.repo._data) == 2
        assert self.repo._next_id == 3

    def test_get_existing_todo(self):
        """Test getting an existing todo."""
        payload = TodoCreate(title="Test Todo")
        created = self.repo.create(payload)
        retrieved = self.repo.get(1)
        
        assert retrieved == created

    def test_get_nonexistent_todo(self):
        """Test getting a non-existent todo."""
        retrieved = self.repo.get(999)
        assert retrieved is None

    def test_list_todos(self):
        """Test listing all todos."""
        payload1 = TodoCreate(title="Todo 1")
        payload2 = TodoCreate(title="Todo 2")
        
        todo1 = self.repo.create(payload1)
        todo2 = self.repo.create(payload2)
        
        todos = self.repo.list()
        assert len(todos) == 2
        assert todo1 in todos
        assert todo2 in todos

    def test_update_existing_todo(self):
        """Test updating an existing todo."""
        payload = TodoCreate(title="Original Title")
        created = self.repo.create(payload)
        
        update_payload = TodoUpdate(title="Updated Title", completed=True)
        updated = self.repo.update(1, update_payload)
        
        assert updated is not None
        assert updated.id == 1
        assert updated.title == "Updated Title"
        assert updated.completed is True
        assert updated.description == created.description  # unchanged
        assert updated.created_at == created.created_at  # unchanged

    def test_update_nonexistent_todo(self):
        """Test updating a non-existent todo."""
        update_payload = TodoUpdate(title="Updated Title")
        updated = self.repo.update(999, update_payload)
        assert updated is None

    def test_update_partial(self):
        """Test partial update of a todo."""
        payload = TodoCreate(title="Original Title", description="Original description")
        self.repo.create(payload)
        
        update_payload = TodoUpdate(completed=True)
        updated = self.repo.update(1, update_payload)
        
        assert updated is not None
        assert updated.title == "Original Title"  # unchanged
        assert updated.description == "Original description"  # unchanged
        assert updated.completed is True  # updated

    def test_delete_existing_todo(self):
        """Test deleting an existing todo."""
        payload = TodoCreate(title="Test Todo")
        self.repo.create(payload)
        
        result = self.repo.delete(1)
        assert result is True
        assert len(self.repo._data) == 0
        assert self.repo.get(1) is None

    def test_delete_nonexistent_todo(self):
        """Test deleting a non-existent todo."""
        result = self.repo.delete(999)
        assert result is False

    def test_id_increment_after_delete(self):
        """Test that ID continues to increment after deletion."""
        payload1 = TodoCreate(title="Todo 1")
        payload2 = TodoCreate(title="Todo 2")
        
        todo1 = self.repo.create(payload1)
        todo2 = self.repo.create(payload2)
        
        self.repo.delete(1)
        
        payload3 = TodoCreate(title="Todo 3")
        todo3 = self.repo.create(payload3)
        
        assert todo3.id == 3  # Not 1, even though 1 was deleted
        assert len(self.repo._data) == 2
        assert self.repo._next_id == 4

    @patch('todo_app.repository.datetime')
    def test_create_with_mocked_datetime(self, mock_datetime):
        """Test creating todo with mocked datetime."""
        mock_now = datetime(2023, 1, 1, 12, 0, 0)
        mock_datetime.utcnow.return_value = mock_now
        
        payload = TodoCreate(title="Test Todo")
        todo = self.repo.create(payload)
        
        assert todo.created_at == mock_now
