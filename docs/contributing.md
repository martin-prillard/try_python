# Contribution

## Comment contribuer

Nous accueillons les contributions ! Voici comment vous pouvez aider :

1. **Fork** le projet
2. **Créer** une branche feature
3. **Développer** votre fonctionnalité
4. **Tester** votre code
5. **Créer** une Pull Request

## Workflow de développement

### 1. Fork et clone

```bash
# Fork le projet sur GitHub, puis :
git clone https://github.com/votre-username/todo-list-best-practices.git
cd todo-list-best-practices

# Ajouter le remote upstream
git remote add upstream https://github.com/original-username/todo-list-best-practices.git
```

### 2. Créer une branche

```bash
# Créer et basculer sur une nouvelle branche
git checkout -b feature/nouvelle-fonctionnalite

# Ou pour une correction de bug
git checkout -b fix/correction-bug
```

### 3. Développer

```bash
# Installer les dépendances
hatch env create
hatch run pip install -e ".[dev]"

# Développer votre fonctionnalité
# ... votre code ...

# Vérifier la qualité du code
hatch run pre-commit run --all-files
```

### 4. Tester

```bash
# Exécuter tous les tests
hatch run pytest

# Tests avec couverture
hatch run pytest --cov=todo_app --cov-report=html

# Vérifier les types
hatch run mypy todo_app/
```

### 5. Commit et push

```bash
# Ajouter les fichiers modifiés
git add .

# Commit avec un message descriptif
git commit -m "feat: ajouter nouvelle fonctionnalité"

# Push vers votre fork
git push origin feature/nouvelle-fonctionnalite
```

### 6. Pull Request

1. Aller sur GitHub
2. Cliquer sur "New Pull Request"
3. Remplir le template de PR
4. Attendre la review

## Standards de code

### Python

- **PEP 8** : Style de code Python
- **Black** : Formatage automatique
- **Ruff** : Linting et corrections
- **mypy** : Vérification des types

### Commits

Utilisez le format [Conventional Commits](https://www.conventionalcommits.org/) :

```
type(scope): description

feat(api): ajouter endpoint pour supprimer les tâches
fix(service): corriger bug dans la validation
docs(readme): mettre à jour les instructions d'installation
test(api): ajouter tests pour le nouvel endpoint
```

**Types disponibles :**
- `feat` : Nouvelle fonctionnalité
- `fix` : Correction de bug
- `docs` : Documentation
- `style` : Formatage, point-virgules manquants, etc.
- `refactor` : Refactoring du code
- `test` : Ajout ou modification de tests
- `chore` : Tâches de maintenance

### Tests

- **Couverture minimum** : 85%
- **Tests unitaires** : Pour chaque fonction
- **Tests d'intégration** : Pour les workflows complets
- **Nommage** : `test_<fonctionnalité>_<scenario>`

### Documentation

- **Docstrings** : Pour toutes les fonctions publiques
- **Type hints** : Pour tous les paramètres et retours
- **README** : Mise à jour si nécessaire
- **MkDocs** : Documentation technique

## Configuration de l'environnement

### Pre-commit hooks

```bash
# Installer les hooks
hatch run pre-commit install

# Lancer manuellement
hatch run pre-commit run --all-files

# Mettre à jour les hooks
hatch run pre-commit autoupdate
```

### IDE Configuration

#### VS Code

```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": ".venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.formatting.provider": "black",
    "python.sortImports.args": ["--profile", "black"],
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

#### PyCharm

1. Configurer l'interpréteur Python vers `.venv/bin/python`
2. Activer Ruff comme linter
3. Configurer Black comme formateur
4. Activer mypy pour la vérification des types

## Types de contributions

### 🐛 Corrections de bugs

1. Identifier le bug
2. Créer une issue si elle n'existe pas
3. Créer une branche `fix/description-du-bug`
4. Implémenter la correction
5. Ajouter des tests
6. Créer une PR

### ✨ Nouvelles fonctionnalités

1. Créer une issue pour discuter la fonctionnalité
2. Attendre l'approbation
3. Créer une branche `feature/nom-fonctionnalite`
4. Implémenter la fonctionnalité
5. Ajouter des tests complets
6. Mettre à jour la documentation
7. Créer une PR

### 📚 Documentation

1. Identifier les sections à améliorer
2. Créer une branche `docs/description`
3. Améliorer la documentation
4. Vérifier la cohérence
5. Créer une PR

### 🧪 Tests

1. Identifier les parties non testées
2. Créer une branche `test/description`
3. Ajouter les tests manquants
4. Vérifier la couverture
5. Créer une PR

## Processus de review

### Pour les contributeurs

1. **Attendre** la review
2. **Répondre** aux commentaires
3. **Appliquer** les suggestions
4. **Tester** les modifications
5. **Mettre à jour** la PR si nécessaire

### Pour les reviewers

1. **Vérifier** le code
2. **Tester** les modifications
3. **Commenter** de manière constructive
4. **Approuver** si tout est correct
5. **Merger** la PR

## Guidelines

### Code

- **Simplicité** : Code simple et lisible
- **Performance** : Optimiser quand nécessaire
- **Sécurité** : Respecter les bonnes pratiques
- **Maintenabilité** : Code facile à maintenir

### Communication

- **Respect** : Être respectueux envers tous
- **Constructif** : Commentaires constructifs
- **Clair** : Communication claire et précise
- **Patient** : Être patient avec les autres

### Tests

- **Complets** : Tests pour tous les cas
- **Rapides** : Tests qui s'exécutent rapidement
- **Fiables** : Tests qui ne flakent pas
- **Maintenables** : Tests faciles à maintenir

## Support

### Questions

- **GitHub Issues** : Pour les bugs et questions
- **GitHub Discussions** : Pour les discussions générales
- **Email** : Pour les questions privées

### Ressources

- **Documentation** : [Documentation complète](https://your-username.github.io/todo-list-best-practices)
- **Code de conduite** : [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- **Changelog** : [CHANGELOG.md](CHANGELOG.md)

## Merci !

Merci de contribuer à ce projet ! Chaque contribution, même petite, est appréciée.
