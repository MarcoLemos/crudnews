POETRY = poetry run
.PHONY: install shell run format test sec docs image cont


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