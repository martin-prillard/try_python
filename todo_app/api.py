"""ASGI API pour la todo-list.

On garde des endpoints simples et documentés automatiquement par OpenAPI.
"""

from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from .models import TodoCreate, TodoInDB, TodoUpdate
from .repository import InMemoryTodoRepository
from .service import TodoService

app = FastAPI(title="Todo List API", version="0.1.0")

# dependencies (could utiliser injection via Depends si nécessaire)
_repo = InMemoryTodoRepository()
_service = TodoService(_repo)


@app.get("/todos", response_model=list[TodoInDB])
def list_todos():
    """Liste tous les todos"""
    return _service.list_todos()


@app.post("/todos", response_model=TodoInDB, status_code=201)
def create_todo(payload: TodoCreate):
    """Créer un todo"""
    return _service.create_todo(payload)


@app.patch("/todos/{todo_id}", response_model=TodoInDB)
def update_todo(todo_id: int, payload: TodoUpdate):
    """Mettre à jour un todo"""
    try:
        return _service.update_todo(todo_id, payload)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    """Supprimer un todo"""
    try:
        _service.delete_todo(todo_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@app.get("/health")
def health_check():
    """Health check endpoint for load balancers and monitoring"""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "version": "0.1.0",
            "service": "todo-list-api",
        },
    )


@app.get("/health/ready")
def readiness_check():
    """Readiness check endpoint for Kubernetes"""
    # In a real application, you would check:
    # - Database connectivity
    # - External service dependencies
    # - Required resources availability
    return JSONResponse(
        status_code=200,
        content={"status": "ready", "timestamp": datetime.utcnow().isoformat()},
    )


# point d'entrée pour lancer localement: uvicorn todo_app.api:app
