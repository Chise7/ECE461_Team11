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
test_file=tests/test_cases.txt
rm_cov=--cov=src/url/responsive_maintainer.py
bus_cov=--cov=src/url/bus_factor.py
ramp_cov=--cov=src/url/ramp_up.py
correct_cov=--cov=src/url/correctness.py
license_cov=--cov=src/url/license.py

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
	$(python) -m $(pytest)
test-py-valid:
	$(python) -m $(pytest) -m "valid"
test-py-invalid:
	$(python) -m $(pytest) -m "invalid"

# Responsive maintainer tests
test-rm:
	$(python) -m $(pytest) -m "rm" $(rm_cov)
test-rm-valid:
	$(python) -m $(pytest) -m "rm and valid" $(rm_cov)
test-rm-invalid:
	$(python) -m $(pytest) -m "rm and invalid" $(rm_cov)
test-rm-weekly:
	$(python) -m $(pytest) -m "rm and weekly" $(rm_cov)
test-rm-yearly:
	$(python) -m $(pytest) -m "rm and yearly" $(rm_cov)

# Bus factor tests
test-bus:
	$(python) -m $(pytest) -m "bus" $(bus_cov)
test-bus-valid:
	$(python) -m $(pytest) -m "bus and valid" $(bus_cov)
test-bus-invalid:
	$(python) -m $(pytest) -m "bus and invalid" $(bus_cov)

# Correctness tests
test-correct:
	$(python) -m $(pytest) -m "correct" $(correct_cov)
test-correct-valid:
	$(python) -m $(pytest) -m "correct and valid" $(correct_cov)
test-correct-invalid:
	$(python) -m $(pytest) -m "correct and invalid" $(correct_cov)

# Ramp up tests
test-ramp:
	$(python) -m $(pytest) -m "ramp" $(ramp_cov)
test-ramp-valid:
	$(python) -m $(pytest) -m "ramp and valid" $(ramp_cov)
test-ramp-invalid:
	$(python) -m $(pytest) -m "ramp and invalid" $(ramp_cov)

# License tests
test-license:
	$(python) -m $(pytest) -m "license" $(license_cov)
test-license-valid:
	$(python) -m $(pytest) -m "license and valid" $(license_cov)
test-license-invalid:
	$(python) -m $(pytest) -m "license and invalid" $(license_cov)

# .PHONY targets
.PHONY: tree cloc clean
.PHONY: test-run-build test-run-install test-run-test test-run-url
.PHONY: test-py test-py-valid test-py-invalid
.PHONY: test-rm test-rm-valid test-rm-invalid test-rm-weekly test-rm-yearly
.PHONY: test-bus test-bus-valid test-bus-invalid
.PHONY: test-correct test-correct-valid test-correct-invalid
.PHONY: test-ramp test-ramp-valid test-ramp-invalid
.PHONY: test-license test-license-valid test-license-invalid