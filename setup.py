import os
import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Read the version from the pythreatmatrix package
with open(os.path.join("pythreatmatrix", "version.py"), "r") as f:
    exec(f.read())

GITHUB_URL = "https://github.com/khulnasoft/pythreatmatrix"

# Get requirements from files
requirements = (HERE / "requirements.txt").read_text().split("\n")
requirements_test = (HERE / "test-requirements.txt").read_text().split("\n")

# This call to setup() does all the work
setup(
    name="pythreatmatrix",
    version=__version__,
    description="Robust Python SDK and CLI for ThreatMatrix's API",
    long_description=README,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    author="Matteo Lodi",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
    install_requires=requirements,
    project_urls={
        "Documentation": GITHUB_URL,
        "Funding": "https://liberapay.com/KhulnaSoft/",
        "Source": GITHUB_URL,
        "Tracker": f"{GITHUB_URL}/issues",
    },
    keywords="threatmatrix sdk python command line osint threat intel malware",
    extras_require={
        "dev": requirements_test + requirements,
        "test": requirements_test + requirements,
    },
    entry_points={
        "console_scripts": [
            "pythreatmatrix=pythreatmatrix.main:cli",
        ],
    },
)
