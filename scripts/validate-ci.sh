#!/bin/bash

# Script de validation locale du pipeline CI/CD
# Usage: ./scripts/validate-ci.sh

set -e

echo "🚀 Validation du pipeline CI/CD local..."

# Couleurs pour les logs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Fonction pour afficher les messages
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Vérifier que nous sommes dans le bon répertoire
if [ ! -f "pyproject.toml" ]; then
    log_error "Ce script doit être exécuté depuis la racine du projet"
    exit 1
fi

# Vérifier que uv est installé
if ! command -v uv &> /dev/null; then
    log_error "uv n'est pas installé. Installez-le avec: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

log_info "Installation des dépendances..."
uv sync --dev

log_info "Vérification des linters..."

# Ruff
log_info "Exécution de Ruff..."
if uv run ruff check todo_app tests; then
    log_info "✅ Ruff: OK"
else
    log_error "❌ Ruff: Échec"
    exit 1
fi

# Black
log_info "Exécution de Black..."
if uv run black --check todo_app tests; then
    log_info "✅ Black: OK"
else
    log_error "❌ Black: Échec"
    exit 1
fi

# isort
log_info "Exécution de isort..."
if uv run isort --check-only todo_app tests; then
    log_info "✅ isort: OK"
else
    log_error "❌ isort: Échec"
    exit 1
fi

# MyPy
log_info "Exécution de MyPy..."
if uv run mypy todo_app; then
    log_info "✅ MyPy: OK"
else
    log_error "❌ MyPy: Échec"
    exit 1
fi

log_info "Exécution des tests avec couverture..."
if uv run pytest --cov=todo_app --cov-report=term-missing --cov-report=html --cov-fail-under=85; then
    log_info "✅ Tests: OK"
else
    log_error "❌ Tests: Échec"
    exit 1
fi

log_info "Construction de la documentation..."
if uv run mkdocs build --clean --strict; then
    log_info "✅ Documentation: OK"
else
    log_error "❌ Documentation: Échec"
    exit 1
fi

log_info "Construction de l'image Docker..."
if docker build -t todo-list-best-practices:test .; then
    log_info "✅ Docker: OK"
else
    log_error "❌ Docker: Échec"
    exit 1
fi

log_info "🎉 Toutes les vérifications sont passées avec succès!"
log_info "Le pipeline CI/CD devrait fonctionner correctement."

# Nettoyage
log_info "Nettoyage des artefacts de test..."
docker rmi todo-list-best-practices:test 2>/dev/null || true
rm -rf site/ htmlcov/ .coverage coverage.xml pytest-report.xml 2>/dev/null || true

log_info "✅ Validation terminée!"
