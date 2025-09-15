# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Configuration MkDocs pour la génération de documentation
- Documentation complète avec guides d'installation, utilisation, API, architecture, tests et déploiement
- Support pour la génération de documentation avec `hatch run mkdocs serve` et `hatch run mkdocs build`

### Changed
- Simplification des tests pour se concentrer uniquement sur le code métier
- Suppression des tests d'infrastructure (logger, config, webapp)
- Amélioration de la couverture de code à 97% pour le code métier

### Fixed
- Correction de l'utilisation de `datetime.utcnow()` déprécié vers `datetime.now(timezone.utc)`
- Correction de l'utilisation de méthodes Pydantic dépréciées (`dict()` → `model_dump()`, `copy()` → `model_copy()`)
- Ajout de l'injection de dépendances dans l'API pour l'isolation des tests

## [0.1.0] - 2025-01-15

### Added
- API REST avec FastAPI pour la gestion des tâches
- Interface web avec Streamlit
- Modèles Pydantic pour la validation des données
- Repository en mémoire pour la persistance des données
- Service layer pour la logique métier
- Tests unitaires et d'intégration avec pytest
- Configuration avec variables d'environnement
- Support Docker avec docker-compose
- CI/CD avec GitHub Actions
- Outils de qualité de code (Ruff, Black, mypy)
- Documentation automatique avec FastAPI
- Health checks pour le monitoring

### Features
- CRUD complet pour les tâches (Create, Read, Update, Delete)
- Validation des données avec Pydantic
- Interface utilisateur intuitive avec Streamlit
- API documentée automatiquement avec Swagger UI
- Tests avec couverture de code >= 85%
- Support pour les environnements de développement et production
- Configuration flexible via variables d'environnement
