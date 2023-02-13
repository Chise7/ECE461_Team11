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
rm_py=src/url/responsive_maintainer.py
bus_py=src/url/bus_factor.py
ramp_py=src/url/ramp_up.py
correct_py=src/url/correctness.py
license_py=src/url/license.py

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
	$(python) -m $(pytest) -m "rm" $(coverage) $(rm_py)
test-rm-valid:
	$(python) -m $(pytest) -m "rm and valid" $(coverage) $(rm_py)
test-rm-invalid:
	$(python) -m $(pytest) -m "rm and invalid" $(coverage) $(rm_py)
test-rm-weekly:
	$(python) -m $(pytest) -m "rm and weekly" $(coverage) $(rm_py)
test-rm-yearly:
	$(python) -m $(pytest) -m "rm and yearly" $(coverage) $(rm_py)

# Bus factor tests
test-bus:
	$(python) -m $(pytest) -m "bus" $(coverage) $(bus_py)
test-bus-valid:
	$(python) -m $(pytest) -m "bus and valid" $(coverage) $(bus_py)
test-bus-invalid:
	$(python) -m $(pytest) -m "bus and invalid" $(coverage) $(bus_py)

# Correctness tests
test-correct:
	$(python) -m $(pytest) -m "correct" $(coverage) $(correct_py)
test-correct-valid:
	$(python) -m $(pytest) -m "correct and valid" $(coverage) $(correct_py)
test-correct-invalid:
	$(python) -m $(pytest) -m "correct and invalid" $(coverage) $(correct_py)

# Ramp up tests
test-ramp:
	$(python) -m $(pytest) -m "ramp" $(coverage) $(ramp_py)
test-ramp-valid:
	$(python) -m $(pytest) -m "ramp and valid" $(coverage) $(ramp_py)
test-ramp-invalid:
	$(python) -m $(pytest) -m "ramp and invalid" $(coverage) $(ramp_py)

# License tests
test-license:
	$(python) -m $(pytest) -m "license" $(coverage) $(license_py)
test-license-valid:
	$(python) -m $(pytest) -m "license and valid" $(coverage) $(license_py)
test-license-invalid:
	$(python) -m $(pytest) -m "license and invalid" $(coverage) $(license_py)

# .PHONY targets
.PHONY: tree cloc clean
.PHONY: test-run-build test-run-install test-run-test test-run-url
.PHONY: test-py test-py-valid test-py-invalid
.PHONY: test-rm test-rm-valid test-rm-invalid test-rm-weekly test-rm-yearly
.PHONY: test-bus test-bus-valid test-bus-invalid
.PHONY: test-correct test-correct-valid test-correct-invalid
.PHONY: test-ramp test-ramp-valid test-ramp-invalid
.PHONY: test-license test-license-valid test-license-invalid