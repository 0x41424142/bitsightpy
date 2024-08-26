# bitsightpy - A Python SDK for Interacting With [Bitsight](https://bitsight.com) APIs

![Logo](https://raw.githubusercontent.com/0x41424142/bitsightpy/main/imgs/logo.png)


[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black) ![Development Status](https://img.shields.io/badge/in%20development-8A2BE2?style=for-the-badge)  ![PyPI - Latest Version](https://img.shields.io/pypi/v/bitsightpy?style=for-the-badge&logo=pypi&logoColor=yellow) ![Python Versions](https://img.shields.io/pypi/pyversions/bitsightpy?style=for-the-badge&logo=python&logoColor=yellow) ![GitHub Stars](https://img.shields.io/github/stars/0x41424142/bitsightpy?style=for-the-badge) ![PyPI - Downloads](https://img.shields.io/pypi/dm/bitsightpy?style=for-the-badge&logo=pypi&logoColor=yellow)

![Black Formatter Status](https://github.com/0x41424142/bitsightpy/actions/workflows/black.yml/badge.svg?event=push) ![CodeQL Scan Status](https://github.com/0x41424142/bitsightpy/actions/workflows/codeql.yml/badge.svg?branch=main)

```py
from bitsightpy.portfolio import get_details

key = '<API_TOKEN>'

portfolio_details = get_details(key)
>>>[
    {
        'guid': '11111111-1111-1111-1111-111111111111', 
        'custom_id': None, 
        'name': 'Some Company', 
        'rating': 750, 
        'industry': {'name': 'Technology', 'slug': 'technology'}, 
        ...
    }, 
...]
```

## Currently Supported Modules/Calls

| Module | Status |
| -- | -- |
| ```users``` | ✅ Fully Implemented |
| ```insights``` | ✅ Fully Implemented |
| ```portfolio``` | ✅ Fully Implemented |
| ```folders``` | ✅ Fully Implemented |
| ```finding_details``` | ✅ Fully Implemented |
| ```alerts``` | ✅ Fully Implemented |
| ```companies``` | 🏗️ In Progress |


# Disclaimer

This SDK tool is an independent project and is not an official product of Bitsight. It has been developed and maintained solely by the names listed in the GitHub contributors list. Bitsight has neither endorsed nor approved this SDK.

Users of this SDK are advised to use it at their own risk and discretion.

For official tools and support, please refer to the [official Bitsight resources and documentation](https://help.bitsighttech.com/hc/en-us).
