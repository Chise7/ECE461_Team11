cloc:
	cloc --exclude-dir=.pytest_cache,.vscode,sample-files,target,venv .

clean:
	cargo clean

.PHONY: cloc clean