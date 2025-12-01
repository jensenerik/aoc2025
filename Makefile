.PHONY: lint
lint:
	poetry run ruff check
	poetry run mypy --strict  --allow-untyped-decorators .

.PHONY: fmt
fmt:
	poetry run ruff format
