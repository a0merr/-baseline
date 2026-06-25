"""Unit tests for core logic — fast, deterministic, no I/O."""

import pytest

from app.main import greet


def test_greet_returns_greeting() -> None:
    assert greet("Andrew") == "Hello, Andrew!"


def test_greet_rejects_empty_name() -> None:
    with pytest.raises(ValueError):
        greet("")
