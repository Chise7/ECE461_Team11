tree:
	tree -I venv -I sample-files
cloc:
	cloc --exclude-dir=.pytest_cache,.vscode,sample-files,target,venv,URL_Fields .
clean:
	cargo clean

pytest_flags=-s -v

# Full test suite
test:
	pytest $(pytest_flags)
test-valid:
	pytest -m "valid" $(pytest_flags)
test-invalid:
	pytest -m "invalid" $(pytest_flags)

# Responsive maintainer tests
test-rm:
	pytest -m "rm" $(pytest_flags)
test-rm-valid:
	pytest -m "rm and valid" $(pytest_flags)
test-rm-invalid:
	pytest -m "rm and invalid" $(pytest_flags)
test-rm-weekly:
	pytest -m "rm and weekly" $(pytest_flags)
test-rm-yearly:
	pytest -m "rm and yearly" $(pytest_flags)

# Bus factor tests
test-bus:
	pytest -m "bus" $(pytest_flags)
test-bus-valid:
	pytest -m "bus and valid" $(pytest_flags)
test-bus-invalid:
	pytest -m "bus and invalid" $(pytest_flags)

# Correctness tests
test-correct:
	pytest -m "correct" $(pytest_flags)
test-correct-valid:
	pytest -m "correct and valid" $(pytest_flags)
test-correct-invalid:
	pytest -m "correct and invalid" $(pytest_flags)

# Ramp up tests
test-ramp:
	pytest -m "ramp" $(pytest_flags)
test-ramp-valid:
	pytest -m "ramp and valid" $(pytest_flags)
test-ramp-invalid:
	pytest -m "ramp and invalid" $(pytest_flags)

# License tests
test-license:
	pytest -m "license" $(pytest_flags)
test-license-valid:
	pytest -m "license and valid" $(pytest_flags)
test-license-invalid:
	pytest -m "license and invalid" $(pytest_flags)

# .PHONY targets
.PHONY: tree cloc clean
.PHONY: test test-valid test-invalid
.PHONY: test-rm test-rm-valid test-rm-invalid test-rm-weekly test-rm-yearly
.PHONY: test-bus test-bus-valid test-bus-invalid
.PHONY: test-correct test-correct-valid test-correct-invalid
.PHONY: test-ramp test-ramp-valid test-ramp-invalid
.PHONY: test-license test-license-valid test-license-invalid