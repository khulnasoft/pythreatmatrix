# Changelog

## [5.0.2](https://github.com/khulnasoft/pythreatmatrix/releases/tag/5.0.2)

Fixed previous broken release

## [5.0.1](https://github.com/khulnasoft/pythreatmatrix/releases/tag/5.0.1)

- Updated documentation
- Removed old endpoints

## [5.0.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/5.0.0)

- Fixes for Playbook Analysis

## [4.4.7](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.4.7)

- Fixed Running Playbook without TLP set

## [4.4.6](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.4.6)

- Readded default TLP for analysis as TLP:CLEAR for "classic" analyses only (the ones that do not leverage a Playbook)

## [4.4.5](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.4.5)

- Default TLP for analysis is not TLP:CLEAR anymore. For instance, this prevents the client to overwrite the TLP configuration of a Playbook.

## [4.4.4](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.4.4)

- Little fixes

## [4.4.3](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.4.3)

- Fixed client results management in case of errors
- Removed support for Python 3.7

## [4.4.2](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.4.2)

- Added support for TLP:CLEAR

## [4.4.1](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.4.1)

- Analyzing a File with a Playbook now works correctly
- other little bug fixing

## [4.4.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.4.0)

- this version supports the usage of a proxy while connecting to ThreatMatrix via Python code.

## [4.3.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.3.0)

- this version supports the new Playbooks feature released with ThreatMatrix v4.1.0

## [4.2.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.2.0)

- this version is fully compatible with ThreatMatrix v4 (#165)
- fixed some errors in `jobs view` and `jobs ls`
- updated all dependencies and softened their requirements

## [4.1.5](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.1.5)

- dependencies upgrade
- #163

## [4.1.4](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.1.4)

- Added support for URLs that use TCP as protocol
- Updated linters + formatted code with `isort`

## [4.1.3](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.1.3)

- Library: `ThreatMatrix.ask_analysis_availability` now accepts an argument `minutes_ago`. Use to specify number of minutes to go back when searching for a previous analysis.
- CLI: `-m/--check-minutes-ago` flag in `analyse`.

## [4.1.2](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.1.2)

- Fix `runtime_configuration` bug in `ThreatMatrix.send_observable_analysis_request`

## [4.1.1](https://github.com/khulnasoft/pythreatmatrix/releases/tag/4.1.1)

- Documentation fixes and adjusts
- Soften `click` package dependency to `click>=7.0` to avoid pip conflicts
- Add support for python 3.10

## [4.1.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/v4.1.0)

> **This version supports only ThreatMatrix versions >=3.1.0.**

**Breaking Changes:**:

- Library: The `tags: List[int]` argument has been deprecated in favor of `tags_labels: List[str]` in the methods, `ThreatMatrix.send_observable_analysis_request` and `ThreatMatrix.send_file_analysis_request`. Previously, the `tags` argument would accept a list of tag indices, now the `tags_labels` accepts a list of tag labels (non-existing `Tag` objects are created automatically with a randomly generated color).
- CLI: Due to above change the `-tl/--tags-list` flag in `analyse` now also accepts a list of tag labels.

**Others:**

- Bump dependencies. `click` -> 8.0.1, `rich` -> 10.12, `click-creds` -> 0.0.3.

## [4.0.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/v4.0.0)

> **This version supports only ThreatMatrix versions >=3.0.0 and includes many breaking changes.**

**Changes:**

- Refactored argument names and ordering for `ask_analysis_availability`, `send_file_analysis_request`, `send_observable_analysis_request` methods to comply with latest changes in ThreatMatrix's REST API.
- Deprecate `run_all_available_analyzers` argument/flag.

**New Features:**

- Ability to specify `connectors_requested` when creating a new analysis.
- Ability to request and view "Connector Reports" for a job.
- Ability to request `connector_config.json` file and view in either JSON or tabular format.
- Ability to request download of sample associated with a job.
- Added `kill`, `retry` and `healthcheck` features to analyzers and connectors. See [Managing Analyzers and Connectors](https://threatmatrix.readthedocs.io/en/master/Usage.html#managing-analyzers-and-connectors) section of the documentation.

**Others:**

- Soften peer dependencies/requirements to avoid pip conflicts.
- Better testing across different python versions using tox's matrix.

## [3.1.4](https://github.com/khulnasoft/pythreatmatrix/releases/tag/3.1.4)

- Fix `ThreatMatrix._get_observable_classification` not setting 'generic' classification properly.

## [3.1.3](https://github.com/khulnasoft/pythreatmatrix/releases/tag/3.1.3)

- Fix to allow SSL verification without a specified PEM file

## [3.1.2](https://github.com/khulnasoft/pythreatmatrix/releases/tag/3.1.2)

- Little fixes and adjustments

## [3.1.1](https://github.com/khulnasoft/pythreatmatrix/releases/tag/3.1.1)

- Removed deprecated ask_analysis_result function
- Little fix to a problem in the logs for the ones that use pythreatmatrix as a library
- Tweaked configuration setup, allowing No Certification Validation
- Added dependabot config and updated dependencies
- Added basic testing suite for CLI

## [3.1.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/3.1.0)

With this, pythreatmatrix now supports all API endpoints of ThreatMatrix.

> More info at: https://github.com/khulnasoft/ThreatMatrix/releases/tag/v2.2.0

## [3.0.1](https://github.com/khulnasoft/pythreatmatrix/releases/tag/3.0.1)

This release was created mainly to solve a problem with the installation of the pip package.

Other changes:

- added support for adding tags when requesting a new job
- added support for creating/editing tags
- added support for "generic" classification of observables

## [3.0.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/3.0.0)

_Note: Incompatible with previous versions_

This version brings a complete rewrite of the pythreatmatrix library as well as command line client. We very much recommend you to update to the latest version to enjoy all new features.

- The new CLI is written with [pallets/click](https://github.com/pallets/click) and supports all ThreatMatrix API endpoints. The CLI is well-documented and will help you navigate different commands; you can use it to request new analysis, view an old analysis, view `analyzer_config.json`, view list of tags, list of jobs, etc.
- Complete type-hinting and sphinx docs for the `pythreatmatrix.ThreatMatrix` class with helper member functions for each ThreatMatrix API endpoint.

## [2.0.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/2.0.0)

**This version supports only ThreatMatrix versions >=1.8.0 (about to be released). To interact with previous ThreatMatrix versions programmatically please refer to pythreatmatrix version 1.3.5**

- we forced [black](https://github.com/psf/black) style, added linters and precommit configuration. In this way pythreatmatrix is aligned to ThreatMatrix.
- we have updated the authentication method from a JWT Token to a simple Token. In this way, it is easier to use pythreatmatrix for integrations with other products and there are no more concurrency problems on multiple simultaneous requests.

If you were using pythreatmatrix and ThreatMatrix before this version, you have to:

- update ThreatMatrix to version>=1.8.0
- retrieve a new API token from the Django Admin Interface for your user: you have to go in the _Durin_ section (click on `Auth tokens`) and generate a key there. This token is valid until manually deleted.

## [1.3.5](https://github.com/khulnasoft/pythreatmatrix/releases/tag/1.3.5)

Now optional parameter "runtime_configuration" properly works

Please use this version of pythreatmatrix with version >= 1.5.x of ThreatMatrix

## [1.3.4](https://github.com/khulnasoft/pythreatmatrix/releases/tag/1.3.4)

see [1.3.3](https://github.com/khulnasoft/pythreatmatrix/releases/tag/1.3.3) for details

## [1.3.3](https://github.com/khulnasoft/pythreatmatrix/releases/tag/1.3.3)

Some fixes:

- pythreatmatrix did not work correctly against HTTPS-enabled ThreatMatrix Servers
- fixed parameter name in send_observable_analysis_request

Please use this version of pythreatmatrix with v1.5.x of ThreatMatrix

## [1.3.2](https://github.com/khulnasoft/pythreatmatrix/releases/tag/1.3.2)

Patch Release after [1.3.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/1.3.0).

- renamed `additional_configuration` to `runtime_configuration`.
- Formatting with psf/black formatter.

**Please use this version of pythreatmatrix with v1.5.x of ThreatMatrix.**

## [1.3.1](https://github.com/khulnasoft/pythreatmatrix/releases/tag/1.3.1)

Fixes and improvements to "--show-colors" option

## [1.3.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/1.3.0)

reformatted some code + added support for new parameter "additional_configuration"

## [1.2.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/1.2.0)

PR #16 for details.

## [1.1.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/1.1.0)

Added an option when executing pythreatmatrix as CLI: `-sc` will show the results in a colorful and organized way that helps the user in looking for useful information. By default, the results are still shown in the JSON format. Thanks to tsale to his idea and contribution.

**Example:**

```
python3 threat_matrix_client.py -i <your_threatmatrix_instance> -sc -a VirusTotal_v2_Get_Observable -a HybridAnalysis_Get_Observable -a OTXQuery observable -v www.google.com
```

## [1.0.0](https://github.com/khulnasoft/pythreatmatrix/releases/tag/1.0.0)

For all the details, check the official blog post:

https://www.honeynet.org/2020/07/05/intel-owl-release-v1-0-0/

This version is compatible only with the related (1.x) ThreatMatrix release.

## 0.2.1

## 0.2.0

## 0.1.2

## 0.1.1
