# Secrets GitHub Actions

Ce document liste les secrets nécessaires pour le bon fonctionnement du pipeline CI/CD.

## Secrets requis

### Pour le déploiement
- `RENDER_SERVICE_ID`: ID du service Render pour le déploiement
- `RENDER_API_KEY`: Clé API Render pour l'authentification

### Pour la publication PyPI (optionnel)
- `PYPI_API_TOKEN`: Token d'API PyPI pour publier les packages

### Pour Codecov (optionnel)
- `CODECOV_TOKEN`: Token Codecov pour l'upload des rapports de couverture

## Configuration des secrets

1. Allez dans les paramètres du repository GitHub
2. Naviguez vers "Secrets and variables" > "Actions"
3. Cliquez sur "New repository secret"
4. Ajoutez chaque secret avec sa valeur correspondante

## Notes importantes

- Les secrets sont chiffrés et ne sont accessibles que dans les workflows GitHub Actions
- Ne jamais commiter les secrets dans le code source
- Utilisez des tokens avec des permissions minimales nécessaires
- Régénérez régulièrement les tokens pour la sécurité
