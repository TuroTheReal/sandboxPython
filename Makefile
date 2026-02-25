.PHONY: all install run test clean shell

VENV   := .venv
PYTHON := $(VENV)/bin/python
TEST   := $(VENV)/bin/pytest
PIP    := $(VENV)/bin/pip

all: install

# Setup venv
install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "✅ Setup complete"

# Lancer un fichier: make run FILE=transaction_assure_project/incomes.py
run:
	@test -n "$(FILE)" || (echo "❌ Usage: make run FILE=<chemin/vers/fichier.py>" && exit 1)
	$(PYTHON) $(FILE)

# Tester un fichier: make test FILE=transaction_assure_project/test_incomes.py
test:
	@test -n "$(FILE)" || (echo "❌ Usage: make test FILE=<chemin/vers/test_file.py>" && exit 1)
	$(TEST) $(FILE) -v

# Clean
clean:
	rm -rf $(VENV)

# Activer le venv pour session interactive
shell:
	@echo "Run: source $(VENV)/bin/activate"
