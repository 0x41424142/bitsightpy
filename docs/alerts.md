# Alerts Module

The alerts module of ```bitsightpy``` allows you to view alerts and disclosures in your portfolio.

To get started, import the module and load your API key:

```py
from bitsightpy import alerts

key = '<API_KEY>'
```

## Get Alerts API

```get_alerts``` lets you get a list of all alerts in your subscription, filtering by kwargs.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```page_count``` | ```Union[int >= 1, 'all']``` = ```'all'``` | ❌ |
| ```limit``` | ```int >= 1 = 100``` | ❌ |
| ```offset``` | ```int >= 1``` | ❌ |
| ```q``` | ```str``` as a company name | ❌ |
| ```sort``` | ```Literal['alert_date', 'guid', 'alert_type', 'company_name', 'folder_name', 'trigger', 'severity'] = 'alert_date'``` | ❌ |
| ```alert_date``` | ```str``` in ```YYYY-MM-DD``` format | ❌ |
| ```alert_date_gt``` | ```str``` in ```YYYY-MM-DD``` format | ❌ |
| ```alert_date_gte``` | ```str``` in ```YYYY-MM-DD``` format | ❌ |
| ```alert_date_lt``` | ```str``` in ```YYYY-MM-DD``` format | ❌ |
| ```alert_date_lte``` | ```str``` in ```YYYY-MM-DD``` format | ❌ |
| ```alert_type``` | ```Literal['PERCENT_CHANGE', 'RATING_THRESHOLD', 'RISK_CATEGORY', 'NIST_CATEGORY', 'PUBLIC_DISCLOSURE', 'INFORMATIONAL', 'VULNERABILITY']``` | ❌ |
| ```company_guid``` | ```str``` as a company guid | ❌ |
| ```expand``` | ```Literal['details']``` | ❌ |
| ```folder_guid``` | ```str``` as a folder guid | ❌ |
| ```severity``` | ```Literal['CRITICAL', 'WARN', 'INCREASE', 'INFORMATIONAL']``` | ❌ |


** Example Request:**

```py
from bitsightpy.alerts import get_alerts

key = '<API_KEY>'

# Get first 3 pages of alerts since 2024-08-01:
alerts = get_alerts(key=key, page_count=3, alert_date_gte='2024-08-01')
```

**Example Response:**

```json
[
    {
      "guid":12345678,
      "alert_type":"RISK_CATEGORY",
      "alert_date":"2024-08-10",
      "start_date":"2024-08-09",
      "company_name":"Example, Inc.",
      "company_guid":"11111111-1111-1111-1111-111111111111",
      "company_url":"/company/11111111-1111-1111-1111-111111111111/",
      "folder_guid":"22222222-2222-2222-2222-222222222222",
      "folder_name":"Continuously Monitored",
      "severity":"WARN",
      "trigger":"Insecure Systems"
    }
  ]
```

## Get 4th Party Public Disclosure Affected Companies API

```get_4th_party_disclosures``` lets you get a list of all companies indirectly affected by a 4th party public disclosure.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```alert_guid``` | ```str``` as an alert guid | ✅ |
| ```page_count``` | ```Union[int >= 1, 'all']``` = ```'all'``` | ❌ |
| ```limit``` | ```int >= 1 = 32``` | ❌ |
| ```offset``` | ```int >= 0``` | ❌ |
| ```q``` | ```str``` | ❌ |

>**Head's Up!:** This API will return a ```422``` error if the alert is not a 4th party public disclosure.

**Example Request:**

```py
from bitsightpy.alerts import get_4th_party_disclosures

key = '<API_KEY>'

companies = get_4th_party_disclosures(key=key, alert_guid='12345678')
```

**Example Response:**

```json
{
  "guid": "12345678",
  "alert_type": "PUBLIC_DISCLOSURE",
  "alert_date": "2024-06-04",
  "start_date": "2024-06-03",
  "company_name": "Company, Inc.",
  "company_guid": "11111111-1111-1111-111111111111",
  "company_url": "/company/11111111-1111-1111-111111111111/",
  "folder_guid": "22222222-2222-2222-2222-222222222222",
  "folder_name": "Total Risk Monitoring",
  "severity": "CRITICAL",
  "trigger": "Patching Cadence",
  "details": {
    "category": "General Security Incident",
    "message": "Bad Company disclosed the personal information of an unknown number of individuals to an unauthorized third party.",
    "subcategory": "Human Error",
    "is_direct": false,
    "severity": 0,
    "discovery_date": "2024-06-04",
    "effective_date": "2024-06-03",
    "public_disclosure_guid": "33333333-3333-3333-3333-333333333333",
    "origin_type": "subsidiary",
    "origin_company":{
      "guid": "11111111-1111-1111-111111111111",
      "name": "Perix, SA",
      "display_url": "/company/11111111-1111-1111-111111111111/",
      "is_subscribed": false,
    },
  }
}
```