# image légère python
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
COPY src/ ./src/
COPY .env.example .env

RUN pip install --upgrade pip && pip install hatch && hatch env create && hatch run pip install -e .

EXPOSE 8000

CMD ["hatch", "run", "start-api"]
