tree:
	tree -I venv -I sample-files

cloc:
	cloc --exclude-dir=.pytest_cache,.vscode,sample-files,target,venv,URL_Fields .

clean:
	cargo clean

test_rm:
	pytest --pyargs src/url/tests/test_responsive_maintainer.py -s -v

.PHONY: tree cloc clean
.PHONY: test_rm