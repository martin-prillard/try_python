"""Configuration centralisée (pydantic BaseSettings).

Permet de lire les variables d'environnement et d'avoir des valeurs par défaut sûres.
"""

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings.

    Les valeurs sensibles doivent être injectées via variables d'environnement.
    """

    app_env: str = "production"
    api_host: AnyHttpUrl = "http://localhost:8000"
    secret_key: str

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
