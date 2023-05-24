.DEFAULT_GOAL := help

export PYTHONPATH
export PIPENV_VENV_IN_PROJECT=1

PYTHON := python3
PIP := $(PYTHON) -m pip
PIPENV := $(PYTHON) -m pipenv
PYLINT := $(PIPENV) run pylint
BLACK := $(PIPENV) run black
MYPY := $(PIPENV) run mypy
ISORT := $(PIPENV) run isort

app_name = fast-api-app:0.0.1
app_root = server
tests_src = $(app_root)/tests
docker_run = docker run --rm --mount type=bind,source="$(shell pwd)/",target=/root/ $(app_name)


.PHONY: help
help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


### Local commands ###

.PHONY: install
install:
	$(PYTHON) -m pip install pip==22.3.1
	$(PIP) install --user pipenv
	$(PIPENV) --python 3.11

.PHONY: venv
venv:
	$(PIP) install -U pipenv
	$(PIPENV) shell

.PHONY: install-packages
install-packages:
	pipenv install --dev

.PHONY: lint
lint:
	$(PYLINT) -E $(APP_DIR) || pylint-exit $$?

.PHONY: format
format:
	$(BLACK) $(APP_DIR)
	$(ISORT) $(APP_DIR)

.PHONY: check-typing
check-typing:
	$(MYPY) $(APP_DIR)

.PHONY: lint-and-format
lint-and-format: ## Lint, format and static-check
	$(PYLINT) -E $(APP_DIR) || pylint-exit $$?
	$(MYPY) $(APP_DIR)
	$(BLACK) $(APP_DIR)
	$(ISORT) $(APP_DIR)

.PHONY: run
run: ## Run FastAPI app
	$(PYTHON) $(APP_DIR)/main.py

### Docker commands ###

.PHONY: build-docker-image
build-docker-image: ## Build the docker image and install python dependencies
	docker build --no-cache -t $(app_name) .
	$(docker_run) pipenv install --dev
	$(docker_run) pre-commit install

.PHONY: format
format: ## Format code
	$(docker_run) pipenv run format

.PHONY: lint
lint: ## Lint the code
	$(docker_run) pipenv run lint

.PHONY: test
test: ## Run tests
	$(docker_run) pipenv run test

# Consider using test-dev or test-deploy instead
.PHONY: testcov
testcov:
	pytest $(tests_src)
	@echo "building coverage html"
	@coverage html
	@echo "opening coverage html in browser"
	@open htmlcov/index.html

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf `find . -type d -name '*.egg-info' `
	rm -rf `find . -type d -name 'pip-wheel-metadata' `
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build
