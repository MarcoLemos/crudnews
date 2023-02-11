FROM python:3.11

# Configure Poetry
ENV POETRY_VERSION=1.3.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin" 
ENV CONTAINER Yes

WORKDIR .

# Install dependencies
COPY poetry.lock pyproject.toml .env ./
RUN poetry install --without dev --no-root

# Run the app

COPY crudnews ./crudnews
CMD ["poetry","run","uvicorn","crudnews.main:app", "--host", "0.0.0.0", "--port", "8080" ]