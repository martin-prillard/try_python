# Déploiement

## Environnements

### Développement
- **Local** : Machine de développement
- **Configuration** : Debug activé, logs détaillés
- **Base de données** : In-memory

### Staging
- **Serveur** : Environnement de test
- **Configuration** : Similaire à la production
- **Base de données** : Base de données de test

### Production
- **Serveur** : Environnement de production
- **Configuration** : Optimisée pour la performance
- **Base de données** : Base de données de production

## Déploiement local

### Avec Docker Compose

```bash
# Développement
docker-compose up

# En arrière-plan
docker-compose up -d

# Services spécifiques
docker-compose up api web
```

### Avec Hatch

```bash
# API
hatch run start-api

# Interface web
hatch run start-web
```

### Avec uv

```bash
# API
uv run uvicorn todo_app.api:app --host 0.0.0.0 --port 8000

# Interface web
uv run streamlit run todo_app/webapp.py --server.port 8501
```

## Déploiement cloud

### AWS

#### ECS (Elastic Container Service)

```yaml
# task-definition.json
{
  "family": "todo-api",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::account:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "todo-api",
      "image": "your-account.dkr.ecr.region.amazonaws.com/todo-api:latest",
      "portMappings": [
        {
          "containerPort": 8000,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "APP_NAME",
          "value": "Todo List API"
        }
      ]
    }
  ]
}
```

#### Lambda

```python
# lambda_handler.py
from mangum import Mangum
from todo_app.api import app

handler = Mangum(app)
```

### Google Cloud

#### Cloud Run

```yaml
# cloudbuild.yaml
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/todo-api', '.']
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/todo-api']
  - name: 'gcr.io/cloud-builders/gcloud'
    args: ['run', 'deploy', 'todo-api', '--image', 'gcr.io/$PROJECT_ID/todo-api', '--platform', 'managed', '--region', 'us-central1']
```

### Azure

#### Container Instances

```yaml
# azure-pipelines.yml
trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: Docker@2
  inputs:
    command: 'buildAndPush'
    repository: 'todo-api'
    dockerfile: 'Dockerfile'
    containerRegistry: 'your-registry'

- task: AzureContainerInstances@0
  inputs:
    azureSubscription: 'your-subscription'
    resourceGroupName: 'your-resource-group'
    location: 'East US'
    image: 'your-registry.azurecr.io/todo-api:$(Build.BuildId)'
    containerName: 'todo-api'
    ports: '8000'
```

## Configuration de production

### Variables d'environnement

```bash
# Production
APP_NAME=Todo List API
DEBUG=false
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=INFO

# Base de données
DATABASE_URL=postgresql://user:password@localhost:5432/todo_db

# Sécurité
SECRET_KEY=your-secret-key
```

### Docker

#### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install -e .

COPY todo_app/ todo_app/

EXPOSE 8000

CMD ["uvicorn", "todo_app.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### docker-compose.yml

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - APP_NAME=Todo List API
      - DEBUG=false
      - LOG_LEVEL=INFO
    restart: unless-stopped

  web:
    build: .
    command: streamlit run todo_app/webapp.py --server.port 8501 --server.headless true
    ports:
      - "8501:8501"
    environment:
      - APP_NAME=Todo List API
    restart: unless-stopped
```

## Monitoring

### Health checks

```bash
# Vérifier l'état de l'API
curl http://localhost:8000/health

# Vérifier la disponibilité
curl http://localhost:8000/health/ready
```

### Logs

```bash
# Docker Compose
docker-compose logs -f api

# Docker
docker logs -f todo-api

# Kubernetes
kubectl logs -f deployment/todo-api
```

### Métriques

- **Uptime** : Disponibilité du service
- **Response time** : Temps de réponse des endpoints
- **Error rate** : Taux d'erreur
- **Throughput** : Nombre de requêtes par seconde

## Sécurité

### HTTPS

```nginx
# nginx.conf
server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Authentification

```python
# middleware.py
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer

security = HTTPBearer()

async def verify_token(token: str = Depends(security)):
    if not verify_jwt_token(token.credentials):
        raise HTTPException(status_code=401, detail="Invalid token")
    return token
```

## Scaling

### Horizontal scaling

```yaml
# kubernetes-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: todo-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: todo-api
  template:
    metadata:
      labels:
        app: todo-api
    spec:
      containers:
      - name: todo-api
        image: todo-api:latest
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

### Load balancing

```yaml
# kubernetes-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: todo-api-service
spec:
  selector:
    app: todo-api
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer
```

## Rollback

### Docker

```bash
# Rollback vers une version précédente
docker run -p 8000:8000 todo-api:previous-version
```

### Kubernetes

```bash
# Rollback du déploiement
kubectl rollout undo deployment/todo-api

# Voir l'historique
kubectl rollout history deployment/todo-api
```

## Maintenance

### Mise à jour

```bash
# Mise à jour des dépendances
hatch run pip install -U -e ".[dev]"

# Rebuild de l'image Docker
docker build -t todo-api:latest .

# Redémarrage du service
docker-compose restart api
```

### Sauvegarde

```bash
# Sauvegarde de la base de données
pg_dump todo_db > backup.sql

# Restauration
psql todo_db < backup.sql
```
