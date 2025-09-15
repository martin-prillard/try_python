# Installation

## Prérequis

- Python 3.11 ou supérieur
- Git
- pip ou uv (gestionnaire de paquets)

## Installation avec Hatch (recommandé)

Hatch est le gestionnaire de projet moderne utilisé par ce projet.

```bash
# Cloner le repository
git clone https://github.com/your-username/todo-list-best-practices.git
cd todo-list-best-practices

# Créer l'environnement virtuel
hatch env create

# Installer les dépendances de développement
hatch run pip install -e ".[dev]"
```

## Installation avec pip

```bash
# Cloner le repository
git clone https://github.com/your-username/todo-list-best-practices.git
cd todo-list-best-practices

# Créer un environnement virtuel
python -m venv .venv

# Activer l'environnement virtuel
# Sur Linux/macOS :
source .venv/bin/activate
# Sur Windows :
.venv\Scripts\activate

# Installer les dépendances
pip install -e ".[dev]"
```

## Installation avec uv

```bash
# Cloner le repository
git clone https://github.com/your-username/todo-list-best-practices.git
cd todo-list-best-practices

# Installer les dépendances
uv sync --dev
```

## Vérification de l'installation

```bash
# Vérifier que l'API fonctionne
hatch run start-api
# ou
uv run uvicorn todo_app.api:app --host 0.0.0.0 --port 8000

# Dans un autre terminal, tester l'API
curl http://localhost:8000/health
```

## Configuration

### Variables d'environnement

Créez un fichier `.env` dans la racine du projet :

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

## Dépannage

### Problèmes courants

1. **Erreur de version Python** : Assurez-vous d'utiliser Python 3.11+
2. **Erreur de permissions** : Utilisez un environnement virtuel
3. **Erreur de dépendances** : Vérifiez que toutes les dépendances sont installées

### Support

Si vous rencontrez des problèmes, consultez :
- [Issues GitHub](https://github.com/your-username/todo-list-best-practices/issues)
- [Documentation complète](https://your-username.github.io/todo-list-best-practices)
