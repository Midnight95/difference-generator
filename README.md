[![Actions Status](https://github.com/Midnight95/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Midnight95/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/be96f5a8223ebfec8e9f/maintainability)](https://codeclimate.com/github/Midnight95/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/be96f5a8223ebfec8e9f/test_coverage)](https://codeclimate.com/github/Midnight95/python-project-50/test_coverage)
[![Github Actions Status](https://github.com/Midnight95/python-project-50/workflows/Python%20CI/badge.svg)](https://github.com/Midnight95/python-project-50/actions)

# Difference generator

## Installation

Clone the repo and use Makefile or just install the package with pip using `pip3 install git+https://github.com/Midnight95/python-project-50.git` command.

## Description
A Python package that allows users to compare differences between two files.

Supported file formats: `yml` and `json`

### Usage
Show help: `gendiff -h`

Compare files: `gendiff -f FORMAT first_file second_file`

To choose formatters use `-f --format` flag with:`plain` `stylish` `json`

The default formatter is `stylish`

## Usage examples

### On linear yml files
[![asciicast](https://asciinema.org/a/PRoYiW2Eoa0N4lgVR4fQH4oCp.svg)](https://asciinema.org/a/PRoYiW2Eoa0N4lgVR4fQH4oCp)

### Nested json file
[![asciicast](https://asciinema.org/a/znBu8UnTY3dEfXH5o0lCFGBZz.svg)](https://asciinema.org/a/znBu8UnTY3dEfXH5o0lCFGBZz)

### Plain formatter
[![asciicast](https://asciinema.org/a/o4B6FhVryx93swjLzoWjBumdJ.svg)](https://asciinema.org/a/o4B6FhVryx93swjLzoWjBumdJ)

### Json formatter
[![asciicast](https://asciinema.org/a/iHelHo5A6bTl4Ry76sFWGnflI.svg)](https://asciinema.org/a/iHelHo5A6bTl4Ry76sFWGnflI)
