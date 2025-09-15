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

# Tests en mode watch
hatch run ptw
```

### Qualité du code

```bash
# Linting avec Ruff
hatch run ruff check .
hatch run ruff format .

# Formatage avec Black
hatch run black .

# Tri des imports avec isort
hatch run isort .

# Vérification des types avec mypy
hatch run mypy todo_app/

# Tous les checks
hatch run pre-commit run --all-files
```

### Documentation

```bash
# Générer la documentation
hatch run mkdocs serve
# Puis ouvrir http://localhost:8000

# Construire la documentation
hatch run mkdocs build
```

## 🐳 Docker

### Développement

```bash
# Lancer tous les services
docker-compose up

# Lancer en arrière-plan
docker-compose up -d

# Services de développement
docker-compose --profile dev up
```

### Production

```bash
# Construire l'image
docker build -t todo-api .

# Lancer le conteneur
docker run -p 8000:8000 todo-api
```

## 🔧 Configuration

### Variables d'environnement

Créez un fichier `.env` :

```bash
APP_NAME=Todo List API
DEBUG=false
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=INFO
```

### Configuration avancée

```bash
# Variables d'environnement personnalisées
export APP_NAME="Mon API Todo"
export DEBUG=true
export LOG_LEVEL=DEBUG
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

## 🧪 Tests

### Structure des tests

```
tests/
├── test_api.py          # Tests d'intégration API
├── test_service.py      # Tests unitaires service
├── test_repository.py   # Tests unitaires repository
├── test_models.py       # Tests unitaires modèles
├── test_config.py       # Tests unitaires configuration
├── test_logger.py       # Tests unitaires logging
└── test_webapp.py       # Tests unitaires webapp
```

### Commandes de test

```bash
# Tests avec couverture détaillée
hatch run pytest --cov=todo_app --cov-report=html --cov-report=term-missing

# Tests par marqueurs
hatch run pytest -m "unit"
hatch run pytest -m "integration"
hatch run pytest -m "not slow"

# Tests avec debug
hatch run pytest --pdb

# Tests en parallèle
hatch run pytest -n auto
```

## 🔄 CI/CD

### GitHub Actions

Le projet utilise GitHub Actions pour :

- **Linting** : Ruff, Black, isort, mypy
- **Tests** : pytest avec couverture >= 85%
- **Sécurité** : Safety, Bandit
- **Build** : Docker multi-stage
- **Déploiement** : Staging et Production
- **Documentation** : MkDocs

### Workflows disponibles

- `ci-cd.yml` : Pipeline principal
- `pr-checks.yml` : Vérifications pour les PR
- `release.yml` : Gestion des releases

### Déclencher manuellement

```bash
# Créer une release
git tag v1.0.0
git push origin v1.0.0

# Déclencher le workflow de release
gh workflow run release.yml
```

## 📚 Documentation

### Génération locale

```bash
# Servir la documentation
hatch run mkdocs serve

# Construire la documentation
hatch run mkdocs build

# Déployer la documentation
hatch run mkdocs gh-deploy
```

### Structure de la documentation

- **Installation** : Guide d'installation
- **Utilisation** : Guide d'utilisation
- **API** : Référence API complète
- **Architecture** : Architecture du projet
- **Tests** : Guide des tests
- **Déploiement** : Guide de déploiement
- **Contribution** : Guide de contribution

## 🛠️ Développement

### Hooks pre-commit

```bash
# Installer les hooks
hatch run pre-commit install

# Lancer manuellement
hatch run pre-commit run --all-files

# Mettre à jour les hooks
hatch run pre-commit autoupdate
```

### Structure du projet

```
todo_app/
├── __init__.py
├── api.py          # API FastAPI
├── config.py       # Configuration
├── logger.py       # Logging
├── models.py       # Modèles Pydantic
├── repository.py   # Couche d'accès aux données
├── service.py      # Logique métier
└── webapp.py       # Interface Streamlit
```

### Ajouter une nouvelle fonctionnalité

1. Créer une branche feature
2. Développer la fonctionnalité
3. Ajouter les tests
4. Vérifier la qualité du code
5. Créer une PR

## 🚀 Déploiement

### Environnements

- **Development** : Local avec hot-reload
- **Staging** : Environnement de test
- **Production** : Environnement de production

### Déploiement local

```bash
# Avec Docker Compose
docker-compose up -d

# Avec Hatch
hatch run start-api
hatch run start-web
```

### Déploiement cloud

Le projet supporte :
- **AWS** : ECS, Lambda, App Runner
- **Google Cloud** : Cloud Run, App Engine
- **Azure** : Container Instances, App Service
- **Kubernetes** : Helm charts inclus

## 📈 Monitoring

### Health checks

- **API** : http://localhost:8000/health
- **Readiness** : http://localhost:8000/health/ready

### Logs

```bash
# Voir les logs
docker-compose logs -f api

# Logs avec filtrage
docker-compose logs -f api | grep ERROR
```

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature
3. Développer et tester
4. Créer une PR
5. Attendre la review

### Standards de code

- **Python** : PEP 8 avec Black
- **Linting** : Ruff
- **Types** : mypy
- **Tests** : pytest avec couverture >= 85%
- **Documentation** : MkDocs

## 📄 Licence

MIT License - voir [LICENSE](LICENSE) pour plus de détails.

## 🆘 Support

- **Issues** : [GitHub Issues](https://github.com/your-username/todo-list-best-practices/issues)
- **Discussions** : [GitHub Discussions](https://github.com/your-username/todo-list-best-practices/discussions)
- **Documentation** : [Documentation complète](https://your-username.github.io/todo-list-best-practices)

## 🎯 Roadmap

- [ ] Authentification JWT
- [ ] Base de données persistante
- [ ] Cache Redis
- [ ] Monitoring avancé
- [ ] Tests de performance
- [ ] Documentation API interactive