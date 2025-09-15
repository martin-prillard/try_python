"""Tests for service layer."""

from unittest.mock import Mock, patch

import pytest

from todo_app.models import TodoCreate, TodoInDB, TodoUpdate
from todo_app.repository import InMemoryTodoRepository
from todo_app.service import TodoService


class TestTodoService:
    """Test TodoService functionality."""

    def setup_method(self):
        """Set up test service for each test."""
        self.repo = InMemoryTodoRepository()
        self.service = TodoService(self.repo)

    def test_list_todos(self):
        """Test listing todos."""
        # Add some test data
        payload1 = TodoCreate(title="Todo 1")
        payload2 = TodoCreate(title="Todo 2")
        self.service.create_todo(payload1)
        self.service.create_todo(payload2)

        todos = self.service.list_todos()
        assert len(todos) == 2
        assert todos[0].title == "Todo 1"
        assert todos[1].title == "Todo 2"

    def test_create_todo(self):
        """Test creating a todo."""
        payload = TodoCreate(title="Test Todo", description="Test description")
        todo = self.service.create_todo(payload)

        assert todo.title == "Test Todo"
        assert todo.description == "Test description"
        assert todo.completed is False
        assert todo.id == 1

    def test_update_todo_success(self):
        """Test successful todo update."""
        # Create a todo first
        payload = TodoCreate(title="Original Title")
        created = self.service.create_todo(payload)

        # Update it
        update_payload = TodoUpdate(title="Updated Title", completed=True)
        updated = self.service.update_todo(1, update_payload)

        assert updated.title == "Updated Title"
        assert updated.completed is True
        assert updated.id == 1

    def test_update_todo_not_found(self):
        """Test updating a non-existent todo."""
        update_payload = TodoUpdate(title="Updated Title")

        with pytest.raises(ValueError, match="Todo not found"):
            self.service.update_todo(999, update_payload)

    def test_delete_todo_success(self):
        """Test successful todo deletion."""
        # Create a todo first
        payload = TodoCreate(title="Test Todo")
        self.service.create_todo(payload)

        # Delete it
        self.service.delete_todo(1)

        # Verify it's gone
        with pytest.raises(ValueError, match="Todo not found"):
            self.service.update_todo(1, TodoUpdate(title="Updated"))

    def test_delete_todo_not_found(self):
        """Test deleting a non-existent todo."""
        with pytest.raises(ValueError, match="Todo not found"):
            self.service.delete_todo(999)

    @patch("todo_app.service.logger")
    def test_list_todos_logging(self, mock_logger):
        """Test that list_todos logs correctly."""
        self.service.list_todos()
        mock_logger.info.assert_called_once_with("Listing todos")

    @patch("todo_app.service.logger")
    def test_create_todo_logging(self, mock_logger):
        """Test that create_todo logs correctly."""
        payload = TodoCreate(title="Test Todo")
        self.service.create_todo(payload)
        mock_logger.info.assert_called_once_with("Creating todo: %s", "Test Todo")

    @patch("todo_app.service.logger")
    def test_update_todo_logging(self, mock_logger):
        """Test that update_todo logs correctly."""
        # Create a todo first
        payload = TodoCreate(title="Test Todo")
        self.service.create_todo(payload)

        # Update it
        update_payload = TodoUpdate(title="Updated Title")
        self.service.update_todo(1, update_payload)

        # Check logging calls
        assert mock_logger.info.call_count == 2  # create + update
        mock_logger.info.assert_any_call("Updating todo %s", 1)

    @patch("todo_app.service.logger")
    def test_update_todo_not_found_logging(self, mock_logger):
        """Test that update_todo logs warning when todo not found."""
        update_payload = TodoUpdate(title="Updated Title")

        with pytest.raises(ValueError):
            self.service.update_todo(999, update_payload)

        mock_logger.warning.assert_called_once_with("Todo %s not found", 999)

    @patch("todo_app.service.logger")
    def test_delete_todo_logging(self, mock_logger):
        """Test that delete_todo logs correctly."""
        # Create a todo first
        payload = TodoCreate(title="Test Todo")
        self.service.create_todo(payload)

        # Delete it
        self.service.delete_todo(1)

        # Check logging calls
        assert mock_logger.info.call_count == 2  # create + delete
        mock_logger.info.assert_any_call("Deleting todo %s", 1)

    @patch("todo_app.service.logger")
    def test_delete_todo_not_found_logging(self, mock_logger):
        """Test that delete_todo logs warning when todo not found."""
        with pytest.raises(ValueError):
            self.service.delete_todo(999)

        mock_logger.warning.assert_called_once_with("Todo %s not found", 999)

    def test_service_with_mock_repository(self):
        """Test service with mocked repository."""
        mock_repo = Mock()
        service = TodoService(mock_repo)

        # Test list_todos
        mock_todos = [TodoInDB(id=1, title="Test", created_at="2023-01-01")]
        mock_repo.list.return_value = mock_todos

        result = service.list_todos()
        assert result == mock_todos
        mock_repo.list.assert_called_once()

        # Test create_todo
        payload = TodoCreate(title="Test Todo")
        mock_todo = TodoInDB(id=1, title="Test Todo", created_at="2023-01-01")
        mock_repo.create.return_value = mock_todo

        result = service.create_todo(payload)
        assert result == mock_todo
        mock_repo.create.assert_called_once_with(payload)

        # Test update_todo success
        update_payload = TodoUpdate(title="Updated")
        mock_repo.update.return_value = mock_todo

        result = service.update_todo(1, update_payload)
        assert result == mock_todo
        mock_repo.update.assert_called_once_with(1, update_payload)

        # Test update_todo not found
        mock_repo.update.return_value = None

        with pytest.raises(ValueError, match="Todo not found"):
            service.update_todo(1, update_payload)

        # Test delete_todo success
        mock_repo.delete.return_value = True
        service.delete_todo(1)
        mock_repo.delete.assert_called_once_with(1)

        # Test delete_todo not found
        mock_repo.delete.return_value = False

        with pytest.raises(ValueError, match="Todo not found"):
            service.delete_todo(1)
