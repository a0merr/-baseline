.PHONY: install test lint format run docker clean

install:  ## Install deps (incl. dev) and pre-commit hooks
	pip install -e ".[dev]"
	pre-commit install

test:  ## Run the test suite with coverage
	pytest

lint:  ## Check formatting and lint (no changes)
	black --check .
	ruff check .

format:  ## Apply formatting and autofixes
	black .
	ruff check --fix .

run:  ## Run the sample app
	python -m app.main

docker:  ## Build and run the whole stack
	docker compose up --build

clean:  ## Remove caches and build artifacts
	rm -rf .pytest_cache .ruff_cache .coverage htmlcov dist build *.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
