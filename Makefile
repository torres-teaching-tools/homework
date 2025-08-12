# --- Student Makefile ---
REPO ?= torres-teaching-tools/jasper-cli
SPEC ?= git+https://github.com/$(REPO)@main

.PHONY: jasper-install jasper-update jasper-uninstall

jasper-install:
	python3 -m pip install --user pipx || true
	python3 -m pipx ensurepath
	pipx install "$(SPEC)" || true

jasper-update:
	pipx upgrade jasper-cli || pipx reinstall "$(SPEC)"

jasper-uninstall:
	pipx uninstall jasper-cli || true
