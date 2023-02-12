tree:
	tree -I venv -I sample-files
cloc:
	cloc --exclude-dir=.pytest_cache,.vscode,sample-files,target,venv,URL_Fields .
clean:
	cargo clean

# Full test suite
test: test-valid test-invalid
test-valid: test-rm-valid test-bus-valid test-correctness-valid test-license-valid
test-invalid: test-rm-invalid test-bus-invalid test-correctness-invalid test-license-invalid

# Responsive maintainer tests
test-rm:
	pytest --pyargs src/url/tests/test_responsive_maintainer.py -s -v
test-rm-valid:
	pytest --pyargs src/url/tests/test_responsive_maintainer.py -m valid -s -v
test-rm-invalid:
	pytest --pyargs src/url/tests/test_responsive_maintainer.py -m invalid -s -v
test-rm-weekly:
	pytest --pyargs src/url/tests/test_responsive_maintainer.py -m weekly -s -v
test-rm-yearly:
	pytest --pyargs src/url/tests/test_responsive_maintainer.py -m yearly -s -v

# Bus factor tests
test-bus:
	pytest --pyargs src/url/tests/test_bus_factor.py -s -v
test-bus-valid:
	pytest --pyargs src/url/tests/test_bus_factor.py -m valid -s -v
test-bus-invalid:
	pytest --pyargs src/url/tests/test_bus_factor.py -m invalid -s -v

# Correctness tests
test-correctness:
	pytest --pyargs src/url/tests/test_correctness.py -s -v
test-correctness-valid:
	pytest --pyargs src/url/tests/test_correctness.py -m valid -s -v
test-correctness-invalid:
	pytest --pyargs src/url/tests/test_correctness.py -m invalid -s -v

# Ramp up tests
test-ramp:
	pytest --pyargs src/url/tests/test_ramp_up.py -s -v
test-ramp-valid:
	pytest --pyargs src/url/tests/test_ramp_up.py -m valid -s -v
test-ramp-invalid:
	pytest --pyargs src/url/tests/test_ramp_up.py -m invalid -s -v

# License tests
test-license:
	pytest --pyargs src/url/tests/test_license.py -s -v
test-license-valid:
	pytest --pyargs src/url/tests/test_license.py -m valid -s -v
test-license-invalid:
	pytest --pyargs src/url/tests/test_license.py -m invalid -s -v

# .PHONY targets
.PHONY: tree cloc clean
.PHONY: test test-valid test-invalid
.PHONY: test-rm test-rm-valid test-rm-invalid test-rm-weekly test-rm-yearly
.PHONY: test-bus test-bus-valid test-bus-invalid
.PHONY: test-correctness test-correctness-valid test-correctness-invalid
.PHONY: test-ramp test-ramp-valid test-ramp-invalid
.PHONY: test-license test-license-valid test-license-invalid