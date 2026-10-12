"""Smoke test: the project layout imports cleanly. Real tests arrive in S1-12."""

import importlib

import pytest

MODULES = [
    "app",
    "app.tenants",
    "app.prompt_builder",
    "app.llm_client",
    "app.executor",
    "app.guardrails",
    "app.auth",
    "app.charts",
    "app.routes",
]


@pytest.mark.parametrize("name", MODULES)
def test_module_imports(name):
    assert importlib.import_module(name) is not None
