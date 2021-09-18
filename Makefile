PYTHON = python

test:
	$(PYTHON) -m pytest ./tests

type:
	$(PYTHON) -m mypy --strict ./mostx

all: type test
