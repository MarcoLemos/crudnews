POETRY = poetry run
.PHONY: install shell run format test sec docs img


install:
	@poetry install
shell:
	@poetry shell
format:
	@${POETRY} isort .
	@${POETRY} blue .
test:
	@${POETRY} pytest
cover:
	@${POETRY} pytest --cov=.
sec:
	@${POETRY} pip-audit
docs:
	@${POETRY} mkdocs serve
img:
	docker-compose --env-file .env up -d mongo
imgd:
	docker-compose --env-file .env down