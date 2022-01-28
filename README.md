# Page loader. A simple project for testing

The package downloads content from a specified webpage to a specified directory. It's managed from bash.

### Tests and linter status:
[![Actions Status](https://github.com/konstter/python-testing-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/konstter/python-testing-project-lvl1/actions)
[![codecov](https://codecov.io/gh/konstter/python-testing-project-lvl1/branch/main/graph/badge.svg?token=0MKQGZTTJB)](https://codecov.io/gh/konstter/python-testing-project-lvl1)
[![flake8](https://github.com/konstter/python-testing-project-lvl1/actions/workflows/lint.yml/badge.svg)](https://github.com/konstter/python-testing-project-lvl1/actions/workflows/lint.yml)

### Depencies:
- Python 3.x
- requests

### Develop depencies:
- Pytest 6.2.5 with requests-mock and pytest-cov

## Usage:

```bash
# Install. Start from the root directory
pip install --user dist/*.whl

# It downloads https://ru.hexlet.io/courses to current directory
page-loader

# page-loader [-h] [-o OUTPUT] [-w WEBPAGE]

# Show help
page-loader -h

# with options

page-loader -o /var/tmp -w https://google.com

```
