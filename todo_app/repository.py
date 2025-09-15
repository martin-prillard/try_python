"""Repository layer: abstraction over data storage.

For this pedagogical example we use an in-memory store. In production,
remplacez par une base de données et adaptez les méthodes (SQLAlchemy/ORM).
"""

from datetime import datetime, timezone

from .models import TodoCreate, TodoInDB, TodoUpdate


class InMemoryTodoRepository:
    """Simple thread-unsafe in-memory repository (for tests and demos).

    Methods are synchronous for clarity. If you use async database drivers,
    adaptez en conséquence.
    """

    def __init__(self) -> None:
        self._data: dict[int, TodoInDB] = {}
        self._next_id = 1

    def list(self) -> list[TodoInDB]:
        return list(self._data.values())

    def create(self, payload: TodoCreate) -> TodoInDB:
        todo = TodoInDB(
            id=self._next_id,
            title=payload.title,
            description=payload.description,
            completed=False,
            created_at=datetime.now(timezone.utc),
        )
        self._data[self._next_id] = todo
        self._next_id += 1
        return todo

    def get(self, todo_id: int) -> TodoInDB | None:
        return self._data.get(todo_id)

    def update(self, todo_id: int, payload: TodoUpdate) -> TodoInDB | None:
        todo = self._data.get(todo_id)
        if not todo:
            return None
        updated = todo.model_copy(update=payload.model_dump(exclude_unset=True))
        self._data[todo_id] = updated
        return updated

    def delete(self, todo_id: int) -> bool:
        return self._data.pop(todo_id, None) is not None
