build:
	cargo build

release:
	cargo build --release

cloc:
	cloc --exclude-dir=.pytest_cache,.vscode,sample-files,target,venv .

.PHONY: build release cloc