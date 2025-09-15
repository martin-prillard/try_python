# API Reference

## Endpoints

### GET /todos

Liste toutes les tâches.

**Réponse :**
```json
[
  {
    "id": 1,
    "title": "Ma tâche",
    "description": "Description de la tâche",
    "completed": false,
    "created_at": "2023-01-01T12:00:00Z"
  }
]
```

### POST /todos

Crée une nouvelle tâche.

**Corps de la requête :**
```json
{
  "title": "string",
  "description": "string"  // optionnel
}
```

**Réponse :**
```json
{
  "id": 1,
  "title": "Ma tâche",
  "description": "Description de la tâche",
  "completed": false,
  "created_at": "2023-01-01T12:00:00Z"
}
```

### PATCH /todos/{id}

Met à jour une tâche existante.

**Paramètres :**
- `id` (int) : ID de la tâche à mettre à jour

**Corps de la requête :**
```json
{
  "title": "string",        // optionnel
  "description": "string",  // optionnel
  "completed": true         // optionnel
}
```

**Réponse :**
```json
{
  "id": 1,
  "title": "Tâche mise à jour",
  "description": "Nouvelle description",
  "completed": true,
  "created_at": "2023-01-01T12:00:00Z"
}
```

### DELETE /todos/{id}

Supprime une tâche.

**Paramètres :**
- `id` (int) : ID de la tâche à supprimer

**Réponse :**
- Code de statut : `204 No Content`

### GET /health

Health check de l'API.

**Réponse :**
```json
{
  "status": "healthy",
  "timestamp": "2023-01-01T12:00:00Z",
  "version": "0.1.0",
  "service": "todo-list-api"
}
```

### GET /health/ready

Readiness check de l'API.

**Réponse :**
```json
{
  "status": "ready",
  "timestamp": "2023-01-01T12:00:00Z"
}
```

## Codes de statut

| Code | Description |
|------|-------------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 404 | Not Found |
| 422 | Unprocessable Entity |

## Validation des données

### Contraintes

- **title** : 1-200 caractères
- **description** : 0-2000 caractères (optionnel)

### Exemples d'erreurs de validation

```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "title"],
      "msg": "String should have at least 1 character",
      "input": ""
    }
  ]
}
```

## Documentation interactive

- **Swagger UI** : http://localhost:8000/docs
- **ReDoc** : http://localhost:8000/redoc
