PYTHON = python
PYTEST = $(PYTHON) -m pytest

test:
	$(PYTEST) ./tests

style:
	$(PYTHON) -m flake8 ./mostx

mypy:
	$(PYTHON) -m mypy ./mostx
