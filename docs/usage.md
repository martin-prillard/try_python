# Utilisation

## Démarrage de l'application

### API FastAPI

```bash
# Avec Hatch
hatch run start-api

# Avec uvicorn directement
uvicorn todo_app.api:app --host 0.0.0.0 --port 8000 --reload

# Avec uv
uv run uvicorn todo_app.api:app --host 0.0.0.0 --port 8000 --reload
```

L'API sera disponible sur http://localhost:8000

### Interface web Streamlit

```bash
# Avec Hatch
hatch run start-web

# Avec streamlit directement
streamlit run todo_app/webapp.py --server.port 8501

# Avec uv
uv run streamlit run todo_app/webapp.py --server.port 8501
```

L'interface web sera disponible sur http://localhost:8501

## Utilisation de l'API

### Endpoints disponibles

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/todos` | Lister toutes les tâches |
| POST | `/todos` | Créer une nouvelle tâche |
| PATCH | `/todos/{id}` | Mettre à jour une tâche |
| DELETE | `/todos/{id}` | Supprimer une tâche |
| GET | `/health` | Health check |
| GET | `/health/ready` | Readiness check |

### Exemples d'utilisation

#### Lister les tâches

```bash
curl http://localhost:8000/todos
```

#### Créer une tâche

```bash
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Ma première tâche",
    "description": "Description de la tâche"
  }'
```

#### Mettre à jour une tâche

```bash
curl -X PATCH http://localhost:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{
    "completed": true
  }'
```

#### Supprimer une tâche

```bash
curl -X DELETE http://localhost:8000/todos/1
```

## Utilisation de l'interface web

1. Ouvrez http://localhost:8501 dans votre navigateur
2. Utilisez le formulaire pour créer de nouvelles tâches
3. Cochez les cases pour marquer les tâches comme terminées
4. Utilisez les filtres pour organiser vos tâches

## Modèles de données

### TodoCreate

```python
{
    "title": "string",           # Obligatoire, 1-200 caractères
    "description": "string"       # Optionnel, max 2000 caractères
}
```

### TodoInDB

```python
{
    "id": 1,                     # ID unique
    "title": "string",           # Titre de la tâche
    "description": "string",     # Description (peut être null)
    "completed": false,          # Statut de complétion
    "created_at": "2023-01-01T12:00:00Z"  # Date de création
}
```

### TodoUpdate

```python
{
    "title": "string",           # Optionnel, 1-200 caractères
    "description": "string",     # Optionnel, max 2000 caractères
    "completed": true            # Optionnel, booléen
}
```

## Gestion des erreurs

L'API retourne des codes de statut HTTP appropriés :

- `200` : Succès
- `201` : Créé avec succès
- `204` : Supprimé avec succès
- `404` : Ressource non trouvée
- `422` : Erreur de validation

### Exemple d'erreur

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
