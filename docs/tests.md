# Tests

## Vue d'ensemble

Le projet utilise pytest comme framework de tests principal, avec une couverture de code cible de 85%.

## Structure des tests

```
tests/
├── test_api.py          # Tests d'intégration API
├── test_service.py      # Tests unitaires service
├── test_repository.py   # Tests unitaires repository
└── test_models.py       # Tests unitaires modèles
```

## Types de tests

### Tests unitaires

Testent des unités individuelles de code en isolation.

**Exemple :**
```python
def test_create_todo():
    """Test creating a todo."""
    payload = TodoCreate(title="Test Todo", description="Test description")
    todo = self.service.create_todo(payload)

    assert todo.title == "Test Todo"
    assert todo.description == "Test description"
    assert todo.completed is False
    assert todo.id == 1
```

### Tests d'intégration

Testent l'interaction entre plusieurs composants.

**Exemple :**
```python
def test_create_todo_success():
    """Test creating a todo successfully."""
    payload = {"title": "Test Todo", "description": "Test description"}
    response = self.client.post("/todos", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Todo"
    assert data["description"] == "Test description"
    assert data["completed"] is False
```

## Commandes de test

### Exécuter tous les tests

```bash
# Avec Hatch
hatch run pytest

# Avec uv
uv run pytest

# Avec pytest directement
pytest
```

### Tests avec couverture

```bash
# Couverture complète
hatch run pytest --cov=todo_app --cov-report=html --cov-fail-under=85

# Couverture en mode terminal
hatch run pytest --cov=todo_app --cov-report=term-missing
```

### Tests spécifiques

```bash
# Tests d'un module
hatch run pytest tests/test_api.py -v

# Tests d'une classe
hatch run pytest tests/test_service.py::TestTodoService -v

# Tests d'une méthode
hatch run pytest tests/test_api.py::TestTodoAPI::test_create_todo_success -v
```

### Tests en mode watch

```bash
# Surveiller les changements
hatch run ptw

# Avec couverture
hatch run ptw -- --cov=todo_app
```

## Configuration des tests

### pytest.ini

```ini
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--strict-config",
    "--cov=todo_app",
    "--cov-report=term-missing",
    "--cov-report=html",
    "--cov-report=xml",
    "--cov-fail-under=85",
    "--cov-branch",
    "-v"
]
```

### Marqueurs de test

```python
@pytest.mark.unit
def test_unit_example():
    """Test unitaire."""
    pass

@pytest.mark.integration
def test_integration_example():
    """Test d'intégration."""
    pass

@pytest.mark.slow
def test_slow_example():
    """Test lent."""
    pass
```

## Bonnes pratiques

### 1. Nommage des tests

- **Fonctions** : `test_<fonctionnalité>_<scenario>`
- **Classes** : `Test<Classe>`
- **Fichiers** : `test_<module>.py`

### 2. Structure des tests

```python
def test_example():
    """Test description."""
    # Arrange
    payload = TodoCreate(title="Test")
    
    # Act
    result = service.create_todo(payload)
    
    # Assert
    assert result.title == "Test"
```

### 3. Isolation des tests

Chaque test doit être indépendant et ne pas affecter les autres.

### 4. Mocks et stubs

Utilisez des mocks pour isoler les dépendances externes.

```python
@patch("todo_app.service.logger")
def test_with_mock(mock_logger):
    """Test with mocked logger."""
    service.create_todo(payload)
    mock_logger.info.assert_called_once()
```

## Couverture de code

### Objectif

- **Minimum** : 85%
- **Cible** : 95%

### Exclusions

Les modules suivants sont exclus de la couverture :
- `config.py` (configuration)
- `logger.py` (infrastructure)
- `webapp.py` (interface utilisateur)

### Rapport de couverture

```bash
# Générer le rapport HTML
hatch run pytest --cov=todo_app --cov-report=html

# Ouvrir le rapport
open htmlcov/index.html
```

## Tests en CI/CD

### GitHub Actions

Les tests sont exécutés automatiquement sur :
- Push sur main
- Pull requests
- Tags de release

### Pipeline de test

1. **Installation** des dépendances
2. **Linting** avec Ruff
3. **Tests unitaires** avec pytest
4. **Couverture** de code
5. **Tests d'intégration**
6. **Build** Docker

## Dépannage

### Problèmes courants

1. **Tests qui échouent** : Vérifiez l'isolation des tests
2. **Couverture faible** : Ajoutez des tests pour les cas manqués
3. **Tests lents** : Utilisez des mocks pour les dépendances externes

### Debug des tests

```bash
# Mode debug
hatch run pytest --pdb

# Tests avec output détaillé
hatch run pytest -s -v

# Tests d'une seule méthode
hatch run pytest tests/test_api.py::TestTodoAPI::test_create_todo_success -v -s
```
