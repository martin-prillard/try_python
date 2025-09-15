"""Tests for Pydantic models."""

from datetime import datetime

import pytest
from pydantic import ValidationError

from todo_app.models import TodoCreate, TodoInDB, TodoUpdate


class TestTodoCreate:
    """Test TodoCreate model validation."""

    def test_valid_todo_create(self):
        """Test creating a valid todo."""
        todo = TodoCreate(title="Test Todo", description="Test description")
        assert todo.title == "Test Todo"
        assert todo.description == "Test description"

    def test_todo_create_without_description(self):
        """Test creating a todo without description."""
        todo = TodoCreate(title="Test Todo")
        assert todo.title == "Test Todo"
        assert todo.description is None

    def test_todo_create_title_too_short(self):
        """Test validation error for title too short."""
        with pytest.raises(ValidationError) as exc_info:
            TodoCreate(title="")
        assert "String should have at least 1 character" in str(exc_info.value)

    def test_todo_create_title_too_long(self):
        """Test validation error for title too long."""
        with pytest.raises(ValidationError) as exc_info:
            TodoCreate(title="x" * 201)
        assert "String should have at most 200 characters" in str(exc_info.value)

    def test_todo_create_description_too_long(self):
        """Test validation error for description too long."""
        with pytest.raises(ValidationError) as exc_info:
            TodoCreate(title="Test", description="x" * 2001)
        assert "String should have at most 2000 characters" in str(exc_info.value)


class TestTodoInDB:
    """Test TodoInDB model."""

    def test_todo_in_db_creation(self):
        """Test creating a TodoInDB instance."""
        now = datetime.utcnow()
        todo = TodoInDB(
            id=1,
            title="Test Todo",
            description="Test description",
            completed=False,
            created_at=now,
        )
        assert todo.id == 1
        assert todo.title == "Test Todo"
        assert todo.description == "Test description"
        assert todo.completed is False
        assert todo.created_at == now

    def test_todo_in_db_defaults(self):
        """Test TodoInDB with default values."""
        now = datetime.utcnow()
        todo = TodoInDB(id=1, title="Test Todo", created_at=now)
        assert todo.completed is False
        assert todo.description is None


class TestTodoUpdate:
    """Test TodoUpdate model validation."""

    def test_valid_todo_update(self):
        """Test creating a valid todo update."""
        update = TodoUpdate(title="Updated Title", completed=True)
        assert update.title == "Updated Title"
        assert update.completed is True
        assert update.description is None

    def test_todo_update_all_fields(self):
        """Test updating all fields."""
        update = TodoUpdate(
            title="New Title", description="New description", completed=True
        )
        assert update.title == "New Title"
        assert update.description == "New description"
        assert update.completed is True

    def test_todo_update_empty(self):
        """Test empty update (all fields None)."""
        update = TodoUpdate()
        assert update.title is None
        assert update.description is None
        assert update.completed is None

    def test_todo_update_title_too_short(self):
        """Test validation error for title too short."""
        with pytest.raises(ValidationError) as exc_info:
            TodoUpdate(title="")
        assert "String should have at least 1 character" in str(exc_info.value)

    def test_todo_update_title_too_long(self):
        """Test validation error for title too long."""
        with pytest.raises(ValidationError) as exc_info:
            TodoUpdate(title="x" * 201)
        assert "String should have at most 200 characters" in str(exc_info.value)

    def test_todo_update_description_too_long(self):
        """Test validation error for description too long."""
        with pytest.raises(ValidationError) as exc_info:
            TodoUpdate(description="x" * 2001)
        assert "String should have at most 2000 characters" in str(exc_info.value)
