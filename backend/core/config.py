# backend/core/config.py
import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# This finds the absolute path to your 'backend/' directory
BACKEND_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    PROJECT_NAME: str = "Finance Dashboard API"

    # Giving these safe local defaults prevents Pydantic from crashing
    # if it doesn't find the .env file immediately.
    DATABASE_URL: str = "sqlite:///./finance.db"
    COINSPOT_KEY: str = ""
    COINSPOT_SECRET: str = ""

    # Explicitly point to the absolute path of the .env file
    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Safely skips any extra variables in your .env
    )


settings = Settings()
