tree:
	tree -I venv -I sample-files

cloc:
	cloc --exclude-dir=.pytest_cache,.vscode,sample-files,target,venv,URL_Fields .

clean:
	cargo clean

test-all: test-rm test-bus test-correctness test-ramp test-license

test-rm:
	pytest --pyargs src/url/tests/test_responsive_maintainer.py -s -v

test-bus:
	pytest --pyargs src/url/tests/test_bus_factor.py -s -v

test-correctness:
	pytest --pyargs src/url/tests/test_correctness.py -s -v

test-ramp:
	pytest --pyargs src/url/tests/test_ramp_up.py -s -v

test-license:
	pytest --pyargs src/url/tests/test_license.py -s -v

.PHONY: tree cloc clean
.PHONY: test-rm test-bus test-correctness test-ramp test-license test-all