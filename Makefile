tree:
	tree -I venv -I sample-files
cloc:
	cloc --exclude-dir=Repo-Analysis,.pytest_cache,.vscode,sample-files,target,venv,URL_Fields .
clean:
	cargo clean
	pip uninstall -y -r requirements.txt

run=coverage run
# run=python3
pytest_flags=-s -v
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
	$(run) -m pytest $(pytest_flags)
test-py-valid:
	$(run) -m pytest -m "valid" $(pytest_flags)
test-py-invalid:
	$(run) -m pytest -m "invalid" $(pytest_flags)

# Responsive maintainer tests
test-rm:
	$(run) -m pytest -m "rm" $(pytest_flags)
test-rm-valid:
	$(run) -m pytest -m "rm and valid" $(pytest_flags)
test-rm-invalid:
	$(run) -m pytest -m "rm and invalid" $(pytest_flags)
test-rm-weekly:
	$(run) -m pytest -m "rm and weekly" $(pytest_flags)
test-rm-yearly:
	$(run) -m pytest -m "rm and yearly" $(pytest_flags)

# Bus factor tests
test-bus:
	$(run) -m pytest -m "bus" $(pytest_flags)
test-bus-valid:
	$(run) -m pytest -m "bus and valid" $(pytest_flags)
test-bus-invalid:
	$(run) -m pytest -m "bus and invalid" $(pytest_flags)

# Correctness tests
test-correct:
	$(run) -m pytest -m "correct" $(pytest_flags)
test-correct-valid:
	$(run) -m pytest -m "correct and valid" $(pytest_flags)
test-correct-invalid:
	$(run) -m pytest -m "correct and invalid" $(pytest_flags)

# Ramp up tests
test-ramp:
	$(run) -m pytest -m "ramp" $(pytest_flags)
test-ramp-valid:
	$(run) -m pytest -m "ramp and valid" $(pytest_flags)
test-ramp-invalid:
	$(run) -m pytest -m "ramp and invalid" $(pytest_flags)

# License tests
test-license:
	$(run) -m pytest -m "license" $(pytest_flags)
test-license-valid:
	$(run) -m pytest -m "license and valid" $(pytest_flags)
test-license-invalid:
	$(run) -m pytest -m "license and invalid" $(pytest_flags)

# .PHONY targets
.PHONY: tree cloc clean
.PHONY: test-run-build test-run-install test-run-test test-run-url
.PHONY: test-py test-py-valid test-py-invalid
.PHONY: test-rm test-rm-valid test-rm-invalid test-rm-weekly test-rm-yearly
.PHONY: test-bus test-bus-valid test-bus-invalid
.PHONY: test-correct test-correct-valid test-correct-invalid
.PHONY: test-ramp test-ramp-valid test-ramp-invalid
.PHONY: test-license test-license-valid test-license-invalid