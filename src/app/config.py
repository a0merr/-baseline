"""Typed application settings loaded from environment variables.

Nothing that varies between environments should be hardcoded. Everything
configurable lives here and is validated at startup, so a misconfiguration
fails loudly and immediately instead of deep inside a request.
"""

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration, sourced from the environment (and `.env`).

    Field types are enforced by pydantic: `DEBUG=true` becomes a real ``bool``,
    not the string ``"true"``. Add fields here as your project grows; never
    reach for ``os.environ`` scattered through the codebase.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "baseline"
    environment: str = "development"
    debug: bool = False

    # Example service config — delete or extend as your project needs.
    database_url: str = "postgresql://baseline:baseline@localhost:5432/baseline"


def get_settings() -> Settings:
    """Return application settings.

    Kept as a function rather than a module-level singleton so tests can
    construct fresh settings deterministically without import-time side effects.
    """
    return Settings()
