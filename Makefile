# Install the pandoc(1) first to run this command
# Ubuntu: sudo apt-get install pandoc
# macOS: brew install pandoc
README.rst: README.md
	pandoc --from=markdown --to=rst --output=README.rst README.md

# Install the package
install:
	python setup.py develop
.PHONY: install

# Upload the package to the pypi server
upload-to-pypi: README.rst
	python setup.py sdist upload
.PHONY: upload-to-pypi

# Upload the package to the test pypi server
upload-to-testpypi: README.rst
	python setup.py sdist upload -r testpypi
.PHONY: upload-to-testpypi

# Run test
test:
	python -m tests.cli_test -v
	python -m tests.ds.model_test -v
.PHONY: test
	
