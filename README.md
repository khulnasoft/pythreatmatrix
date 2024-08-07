# PyThreatMatrix

[![PyPI version](https://badge.fury.io/py/pythreatmatrix.svg)](https://badge.fury.io/py/pythreatmatrix)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/pythreatmatrix.svg)](https://pypi.python.org/pypi/pythreatmatrix/)

[![Pull request automation](https://github.com/khulnasoft/pythreatmatrix/actions/workflows/pull_request_automation.yml/badge.svg)](https://github.com/khulnasoft/pythreatmatrix/actions/workflows/pull_request_automation.yml)
[![codecov](https://codecov.io/gh/khulnasoft/pythreatmatrix/branch/master/graph/badge.svg?token=JF62UMZ0U6)](https://codecov.io/gh/khulnasoft/pythreatmatrix)
[![CodeFactor](https://www.codefactor.io/repository/github/khulnasoft/pythreatmatrix/badge)](https://www.codefactor.io/repository/github/khulnasoft/pythreatmatrix)

Robust Python **SDK** and **Command Line Client** for interacting with [ThreatMatrix](https://github.com/khulnasoft/ThreatMatrix)'s API.

## Features

- Easy one-time configuration with self documented help and hints along the way.
- Request new analysis for observables and files.
  - Select which analyzers you want to run for every analysis you perform.
  - Choose whether you want to HTTP poll for the analysis to finish or not.
- List all jobs or view one job in a prettified tabular form.
- List all tags or view one tag in a prettified tabular form.
- Tabular view of the `analyzer_config.json` and `connector_config.json` from ThreatMatrix with RegEx matching capabilities.

## Demo

[![pythreatmatrix asciicast](https://asciinema.org/a/z7L93lsIzOQ0Scve7hMl30mJJ.svg)](https://asciinema.org/a/z7L93lsIzOQ0Scve7hMl30mJJ?t=5)

## Installation

```bash
$ pip3 install pythreatmatrix
```

For development/testing, `pip3 install pythreatmatrix[dev]`

## Quickstart

### As Command Line Client

On successful installation, The `pythreatmatrix` entryscript should be directly invokable. For example,

```bash
$ pythreatmatrix
Usage: pythreatmatrix [OPTIONS] COMMAND [ARGS]...

Options:
  -d, --debug  Set log level to DEBUG
  --version    Show the version and exit.
  -h, --help   Show this message and exit.

Commands:
  analyse                Send new analysis request
  analyzer-healthcheck   Send healthcheck request for an analyzer...
  config                 Set or view config variables
  connector-healthcheck  Send healthcheck request for a connector
  get-analyzer-config    Get current state of `analyzer_config.json` from...
  get-connector-config   Get current state of `connector_config.json` from...
  jobs                   Manage Jobs
  tags                   Manage tags
```

### As a library / SDK

```python
from pythreatmatrix import ThreatMatrix
obj = ThreatMatrix("<your_api_key>", "<your_threatmatrix_instance_url>", "optional<path_to_pem_file>", "optional<proxies>")
```

For more comprehensive documentation, please see https://pythreatmatrix.readthedocs.io/.

## Changelog

View [CHANGELOG.md](https://github.com/khulnasoft/pythreatmatrix/blob/master/.github/CHANGELOG.md).

## FAQ

#### Generate API key

You need a valid API key to interact with the ThreatMatrix server.
Keys should be created from the admin interface of [ThreatMatrix](https://github.com/khulnasoft/threatmatrix): you have to go in the _Durin_ section (click on `Auth tokens`) and generate a key there.

#### Incompatibility after version 3.0

We did a complete rewrite of the PyThreatMatrix client and CLI both for the version `3.0.0`. We very much recommend you to update to the latest version to enjoy all new features.

#### (old auth method) JWT Token Authentication

> this auth was available in ThreatMatrix versions <1.8.0 and pythreatmatrix versions <2.0.0

From the admin interface of ThreatMatrix, you have to go in the _Outstanding tokens_ section and generate a token there.

You can use it by pasting it into the file [api_token.txt](api_token.txt).
