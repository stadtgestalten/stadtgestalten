LINT_PKG_IGNORE_GLOBAL = -path "./debian/*" -o -path "./build/*" -o -path "./.pybuild/*" -o -path "./scripts/*" \
	-o -path "./.venv/*" -o -path "./gitlab-ci-build-venv/*" -o -path "./docs/*"
LINT_PKG_PEP420 = $(shell find . -mindepth 2 -type f -name "*.py" -not \( $(LINT_PKG_IGNORE_GLOBAL) \) -print0 | \
	xargs -0 -n1 dirname | sort | uniq)

.PHONY: lint
lint: lint_js lint-python lint_packages

.PHONY: lint_js
lint_js: $(STAMP_NODE_MODULES) $(BIN_NPM)
	$(RUN_NODE) "$(BIN_NPM)" run lint

.PHONY: lint_packages
lint_packages:
	# setuptools’ find_packages() does not find PEP420 packages
	# we therefor forbid the use of PEP420 to ease automation
	# see: https://github.com/pypa/setuptools/issues/97
	@EXIT=0; for package in $(LINT_PKG_PEP420); do \
		if [ ! -f "$$package/__init__.py" ]; then \
			EXIT=1; \
			echo "missing __init__.py in $$package" >&2; \
		fi; \
	done && test "$$EXIT" = "0"
	@echo "OK"

.PHONY: test
test: test_js

.PHONY: test_py
test_py: test-python

test-python: test_py_prepare

.PHONY: test_py_prepare
test_py_prepare:
	@# check for duplicate test method names that may overwrite each other
	@duplicate_function_names=$$(find . -mindepth 2 -type f -name tests.py -not \( $(LINT_PKG_IGNORE_GLOBAL) \) \
			| xargs grep -h "def test_" \
			| sed 's/^ \+def //g' | cut -f 1 -d "(" \
			| sort | uniq -d); \
		if [ -n "$$duplicate_function_names" ]; then \
			echo "[ERROR] non-unique test method names found:"; \
			echo "$$duplicate_function_names" | sed 's/^/    /g'; \
			exit 1; \
		fi >&2
	# Our base template includes 'core/_assets.html' which is generated by 'make assets'.
	# Without it any view that renders from the base template will fail when the include
	# is resolved, which breaks a lot of our python-tests. As this template only includes
	# asset metadata and JavaScript & CSS file references, we simply make sure that the file
	# exists during the test run. The content itself is of no relevance to the python-tests.
	touch grouprise/core/templates/core/_assets.html

.PHONY: test_js
test_js: $(STAMP_NODE_MODULES) $(BIN_NPM) lint_js
	$(RUN_NODE) "$(BIN_NPM)" run test

.PHONY: report-python-coverage
coverage_py: $(ACTIVATE_VIRTUALENV) virtualenv-check
	( . "$(ACTIVATE_VIRTUALENV)" && STADTGESTALTEN_PRESET=test "$(PYTHON_BIN)" -m coverage run -m manage test )
	( . "$(ACTIVATE_VIRTUALENV)" && "$(PYTHON_BIN)" -m coverage report )
	( . "$(ACTIVATE_VIRTUALENV)" && "$(PYTHON_BIN)" -m coverage html --directory="$(DIR_BUILD)/coverage-report" )
	@echo "Coverage Report Location: file://$(realpath $(DIR_BUILD))/coverage-report/index.html"
