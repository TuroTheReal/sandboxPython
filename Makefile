.PHONY: all install run test clean

VENV := .venv
PYTHON := $(VENV)/bin/python
TEST := $(VENV)/bin/pytest
PIP := $(VENV)/bin/pip

all: install

# Setup venv (pas d'activation)
install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "✅ Setup complete"

# Run (appel direct au python du venv)
run:
	$(PYTHON) assure.py

test:
	.venv/bin/pytest test_assure.py -v

# Clean
clean:
	rm -rf $(VENV)

# Dev: active venv pour session interactive
shell:
	@echo "Activating venv..."
	@echo "Run: source $(VENV)/bin/activate"