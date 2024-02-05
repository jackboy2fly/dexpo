# Introduction

**Dexpo** is a simple CLI tool for generating basic reports about a given package using data from the [libraries.io API](https://libraries.io).

**Disclaimer**: Only PyPI and NPM projects are currently supported.

# Requirements

- Python >= 3.11.6
- [libraries.io](https://libraries.io) account

# Getting Started

1. Clone this repo in your dev environment
2. Create a virtual environment `$ python -m venv env` and activate:

- Windows: `PS> env/scripts/activate`
- Linux: `$ env/bin/activate`

3. Install dependencies `pip install -r requirements.txt`
4. Create a [libraries.io](https://libraries.io) account and get your api key from the settings page.
5. You must include your private `--api-key` value as an argument or store it in an environment variable called `LIBRARIESIO_API_KEY`

# Usage

```console
$ python dexpo.py pandas --api-key 123APIKEY456 --platform pypi --report
```
![example](https://github.com/jackboy2fly/dexpo/assets/81083035/62bc80a8-0fa7-468f-8515-0af622e42dc2)