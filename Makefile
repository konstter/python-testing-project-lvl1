build:
	poetry build

install:
	package-install

test:
	poetry run pytest

.PHONY: build test
