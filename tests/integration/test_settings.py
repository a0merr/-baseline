"""Integration test: exercises the real env/file boundary unit tests mock away.

It writes an actual ``.env`` file and confirms ``Settings`` loads and *types*
values from it (e.g. ``DEBUG=true`` -> ``bool``), rather than mocking the
loader. Deterministic and offline — no network, no wall-clock dependence.
"""

import pytest

from app.config import Settings

pytestmark = pytest.mark.integration


def test_settings_load_from_env_file(tmp_path) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "APP_NAME=from-env\nDEBUG=true\nENVIRONMENT=staging\n",
        encoding="utf-8",
    )

    settings = Settings(_env_file=str(env_file))

    assert settings.app_name == "from-env"
    assert settings.debug is True  # parsed as a real bool, not the string "true"
    assert settings.environment == "staging"
