# Makefile

VENV_NAME=venv
PYTHON=${VENV_NAME}/bin/python
PIP=${VENV_NAME}/bin/pip

venv:
	python3 -m venv $(VENV_NAME)

dev-compose:
	docker-compose -f docker-compose.yml up --build

install: venv
	$(PIP) install -r requirements.txt

update_requirements: venv
	$(PIP) freeze > requirements.txt

clean:
	rm -rf $(VENV_NAME)
	rm -f requirements.txt

.PHONY: venv install update_requirements clean dev-compose
