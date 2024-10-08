# Getting Started

To start using ```bitsightpy```, you will need an API key from Bitsight. Refer to Bitsight documentation on how to get one.

## Installing from PyPI

For the latest (hopefully stable) version, you can install from PyPI:

```bash
pip install bitsightpy
```

## Installing From GitHub (Bleeding Edge)

If you want the latest and greatesr, or want to contribute, you can install from GitHub:

```bash
git clone https://github.com/0x41424142/bitsightpy.git
cd bitsightpy

#Using pip:
pip install .

#Or use poetry:
poetry shell
poetry install
```

## Bitsightpy CLI

```bitsightpy``` comes with a CLI script that you can use to interact with various Bitsight API endpoints. Supported endpoints are listed below in the help output.

```bash
usage: bitsightpy [-h] {findings,portfolio,alerts} ...

bitsightpy CLI tool. Pulls alerts, portfolio, and findings from the Bitsight API.

positional arguments:
  {findings,portfolio,alerts}
    findings            Get findings for a given company.
    portfolio           Get your Bitsight portfolio.
    alerts              Get a list of your Bitsight alerts.

options:
  -h, --help            show this help message and exit
```

### Portfolio CLI

```bash
usage: bitsightpy portfolio [-h] [--output OUTPUT] --key KEY

Get your Bitsight portfolio.

options:
  -h, --help       show this help message and exit
  --output OUTPUT  The file to write the portfolio to. If not provided, prints to stdout.
  --key KEY        Your Bitsight API key.

# Example, writing to stdout
bitsightpy portfolio --key <API_KEY>
```

### Findings CLI

```bash
usage: bitsightpy findings [-h] [--output OUTPUT] --key KEY [-pC PAGE_COUNT] [-kW [KWARGS ...]] company

Get findings for a given company.

positional arguments:
  company               The company guid to get findings for.

options:
  -h, --help            show this help message and exit
  --output OUTPUT       The file to write the findings to. If not provided, prints to stdout.
  --key KEY             The Bitsight API key. If not provided, looks for the BITSIGHT_API_KEY environment variable.
  -pC PAGE_COUNT, --page_count PAGE_COUNT
                        The number of pages to retrieve. Defaults to 'all'.
  -kW [KWARGS ...], --kwargs [KWARGS ...]
                        Additional keyword arguments to pass to the API call, formatted in key=value pairs.

# Example, writing to a file
bitsightpy findings --key <API_KEY> <COMPANY_GUID> --output findings.json -pC 5 --kwargs affects_rating=True risk_category="Compromised Systems"
```

### Alerts CLI

```bash
usage: bitsightpy alerts [-h] [--output OUTPUT] --key KEY [-pC PAGE_COUNT] [-kW [KWARGS ...]]

Get a list of your Bitsight alerts.

options:
  -h, --help            show this help message and exit
  --output OUTPUT       The file to write the alerts to. If not provided, prints to stdout.
  --key KEY             Your Bitsight API key.
  -pC PAGE_COUNT, --page_count PAGE_COUNT
                        The number of pages to retrieve. Defaults to 'all'.
  -kW [KWARGS ...], --kwargs [KWARGS ...]
                        Additional keyword arguments to pass to the API call, formatted in key=value pairs.

# Example, pulling all vulnerability alerts:
bitsightpy alerts --key <API_KEY> --kwargs alert_type=VULNERABILITY
```