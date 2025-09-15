"""Service layer: logique métier.

La séparation "service/repository" rend le code testable et maintenable.
"""

from .logger import logger
from .models import TodoCreate, TodoInDB, TodoUpdate
from .repository import InMemoryTodoRepository


class TodoService:
    """Service for todo operations.

    Gère la logique applicative et utilise un repository (dépendance).
    """

    def __init__(self, repo: InMemoryTodoRepository) -> None:
        self.repo = repo

    def list_todos(self) -> list[TodoInDB]:
        logger.info("Listing todos")
        return self.repo.list()

    def create_todo(self, payload: TodoCreate) -> TodoInDB:
        logger.info("Creating todo: %s", payload.title)
        return self.repo.create(payload)

    def update_todo(self, todo_id: int, payload: TodoUpdate) -> TodoInDB:
        logger.info("Updating todo %s", todo_id)
        updated = self.repo.update(todo_id, payload)
        if updated is None:
            logger.warning("Todo %s not found", todo_id)
            raise ValueError("Todo not found")
        return updated

    def delete_todo(self, todo_id: int) -> None:
        logger.info("Deleting todo %s", todo_id)
        if not self.repo.delete(todo_id):
            logger.warning("Todo %s not found", todo_id)
            raise ValueError("Todo not found")
