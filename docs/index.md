# Todo List API

API moderne de gestion de tâches avec FastAPI et Streamlit, respectant les bonnes pratiques de développement Python.

## 🚀 Démarrage rapide

### Prérequis
- Python 3.11+
- Git

### Installation

```bash
# Cloner le repository
git clone https://github.com/your-username/todo-list-best-practices.git
cd todo-list-best-practices

# Installer avec Hatch (recommandé)
hatch env create
hatch run pip install -e ".[dev]"

# Ou avec pip
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou .venv\Scripts\activate  # Windows
pip install -e ".[dev]"
```

## 🏃‍♂️ Commandes essentielles

### Lancer l'application

```bash
# API FastAPI
hatch run start-api
# ou
uvicorn todo_app.api:app --host 0.0.0.0 --port 8000 --reload

# Interface web Streamlit
hatch run start-web
# ou
streamlit run todo_app/webapp.py --server.port 8501
```

### Tests

```bash
# Tous les tests
hatch run pytest

# Tests avec couverture
hatch run pytest --cov=todo_app --cov-report=html --cov-fail-under=85

# Tests spécifiques
hatch run pytest tests/test_api.py -v
```

### Documentation

```bash
# Servir la documentation
hatch run mkdocs serve

# Construire la documentation
hatch run mkdocs build
```

## 📊 Endpoints API

- **Documentation interactive** : http://localhost:8000/docs
- **Documentation ReDoc** : http://localhost:8000/redoc
- **Health check** : http://localhost:8000/health

### Exemples d'utilisation

```bash
# Lister les tâches
curl http://localhost:8000/todos

# Créer une tâche
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Ma tâche", "description": "Description"}'

# Mettre à jour une tâche
curl -X PATCH http://localhost:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# Supprimer une tâche
curl -X DELETE http://localhost:8000/todos/1
```

## 🛠️ Fonctionnalités

- ✅ **API REST** avec FastAPI
- ✅ **Interface web** avec Streamlit
- ✅ **Validation** des données avec Pydantic
- ✅ **Tests** complets avec pytest
- ✅ **Documentation** automatique
- ✅ **Docker** support
- ✅ **CI/CD** avec GitHub Actions
- ✅ **Qualité du code** avec Ruff, Black, mypy
