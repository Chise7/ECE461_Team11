tree:
	tree -I venv -I sample-files
cloc:
	cloc --exclude-dir=Repo-Analysis,.$(pytest)_cache,.vscode,sample-files,target,venv,URL_Fields .
clean:
	cargo clean
	pip uninstall -y -r requirements.txt

python=python3
pytest_flags=-s -v
pytest=pytest $(pytest_flags)
coverage=--cov=url
test_file=tests/test_cases.txt

# End-to-end tests
test-run-build:
	./run build
test-run-install:
	./run install
test-run-test:
	./run test
test-run-url:
	./run $(test_file)

# Run all python unit tests
test-py:
	$(python) -m $(pytest) $(coverage)
test-py-valid:
	$(python) -m $(pytest) -m "valid" $(coverage)
test-py-invalid:
	$(python) -m $(pytest) -m "invalid" $(coverage)

# Responsive maintainer tests
test-rm:
	$(python) -m $(pytest) -m "rm" $(coverage)
test-rm-valid:
	$(python) -m $(pytest) -m "rm and valid" $(coverage)
test-rm-invalid:
	$(python) -m $(pytest) -m "rm and invalid" $(coverage)
test-rm-weekly:
	$(python) -m $(pytest) -m "rm and weekly" $(coverage)
test-rm-yearly:
	$(python) -m $(pytest) -m "rm and yearly" $(coverage)

# Bus factor tests
test-bus:
	$(python) -m $(pytest) -m "bus" $(coverage)
test-bus-valid:
	$(python) -m $(pytest) -m "bus and valid" $(coverage)
test-bus-invalid:
	$(python) -m $(pytest) -m "bus and invalid" $(coverage)

# Correctness tests
test-correct:
	$(python) -m $(pytest) -m "correct" $(coverage)
test-correct-valid:
	$(python) -m $(pytest) -m "correct and valid" $(coverage)
test-correct-invalid:
	$(python) -m $(pytest) -m "correct and invalid" $(coverage)

# Ramp up tests
test-ramp:
	$(python) -m $(pytest) -m "ramp" $(coverage)
test-ramp-valid:
	$(python) -m $(pytest) -m "ramp and valid" $(coverage)
test-ramp-invalid:
	$(python) -m $(pytest) -m "ramp and invalid" $(coverage)

# License tests
test-license:
	$(python) -m $(pytest) -m "license" $(coverage)
test-license-valid:
	$(python) -m $(pytest) -m "license and valid" $(coverage)
test-license-invalid:
	$(python) -m $(pytest) -m "license and invalid" $(coverage)

# .PHONY targets
.PHONY: tree cloc clean
.PHONY: test-run-build test-run-install test-run-test test-run-url
.PHONY: test-py test-py-valid test-py-invalid
.PHONY: test-rm test-rm-valid test-rm-invalid test-rm-weekly test-rm-yearly
.PHONY: test-bus test-bus-valid test-bus-invalid
.PHONY: test-correct test-correct-valid test-correct-invalid
.PHONY: test-ramp test-ramp-valid test-ramp-invalid
.PHONY: test-license test-license-valid test-license-invalid