"""Application entry point.

Intentionally tiny: it demonstrates the wiring (typed settings + logging)
without pretending to be a real app. Gut everything below and build here.
"""

from __future__ import annotations

import logging

from app.config import get_settings

logger = logging.getLogger(__name__)


def greet(name: str) -> str:
    """Return a greeting for ``name``.

    A stand-in for "your core logic" — it exists so the sample unit test has
    something real to assert against, including the error path.
    """
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"


def main() -> None:
    """Run the sample app: load config, log startup, print a greeting."""
    logging.basicConfig(level=logging.INFO)
    settings = get_settings()
    logger.info("Starting %s in %s mode", settings.app_name, settings.environment)
    print(greet("world"))


if __name__ == "__main__":
    main()
