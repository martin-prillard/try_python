from todo_app.repository import InMemoryTodoRepository
from todo_app.service import TodoService
from todo_app.models import TodoCreate


def test_create_and_list():
    repo = InMemoryTodoRepository()
    svc = TodoService(repo)

    created = svc.create_todo(TodoCreate(title="t1", description="d"))
    assert created.id == 1

    todos = svc.list_todos()
    assert len(todos) == 1
    assert todos[0].title == "t1"
