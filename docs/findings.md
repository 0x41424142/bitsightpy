# Company Findings Module

The ```finding_details``` module of ```bitsightpy``` returns findings themselves out of Bitsight's API for a company.

To get started, import the module and load your API key:

```py
from bitsightpy import finding_details

key = '<API_KEY>'
```

>**Head's Up!:** Some Bitsight API parameters contain a period in their name. Due to Python rules, these periods have been changed to underscores when a user defines them in a call. The underlying base API call function handles the conversion back to a period. For example, ```risk_vector.slug``` is defined by the user as ```risk_vector_slug```.


## Get Findings API

```get_findings``` returns a company's findings and their details that affect (or will affect) the Bitsight score.  Depending on the value that you pass into the ```risk_vector``` and/or ```risk_category``` parameters, you can filter findings by the type of risk they pose.

>**Head's Up!:** Squatted domain findings are NOT returned by this API call.


| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company_guid``` | ```str``` as a company guid | ✅ |
| ```page_count``` | ```Union[int, 'all'] = 'all'``` | ❌ |
| ```fields``` | ```str``` | ❌ |
| ```limit``` | ```int = 100``` | ❌ |
| ```offset``` | ```int = 100``` | ❌ |
| ```q``` | ```str``` | ❌ |
| ```sort``` | ```str``` | ❌ |
| ```risk_category``` | ```Literal['Compromised Systems', 'Diligence', 'User Behavior']``` as a comma-separated string | ❌ |
| ```risk_vector``` | Comma-separated string with the following values: ```'botnet_infections', 'spam_propagation', 'malware_servers', 'unsolicited_comm', 'potentially_exploited', 'spf', 'dkim', 'dmarc', 'ssl_certificates', 'ssl_configurations', 'open_ports', 'application_security', 'patching_cadence', 'insecure_systems', 'server_software', 'desktop_software', 'mobile_software', 'dnssec', 'mobile_application_security', 'web_appsec', 'file_sharing'``` | ❌ |
| ```affects_rating``` | ```bool``` True = only findings that impact grade | ❌ |
| ```affects_rating_details``` | ```Literal['AFFECTS_RATING', 'LIFETIME_EXPIRED']``` | ❌ |
| ```assets_asset``` | ```Literal['Domain', 'IP Address']``` | ❌ |
| ```assets_category``` | ```Literal['low', 'medium', 'high', 'critical', None]``` | ❌ |
| ```assets_combined_importance``` | ```str``` of ```assets_category``` values | ❌ |
| ```assets_hosted_by``` | ```str``` as a hosting provider guid. See ```portfolio.get_details```| ❌ |
| ```attributed_companies_guid``` | ```str``` as a company guid | ❌ |
| ```attributed_companies_name``` | ```str``` as a company name | ❌ |
| ```details_cvss_base_gte``` | ```float``` [0-10] | ❌ |
| ```details_cvss_base_lte``` | ```float``` [0-10] | ❌ |
| ```details_grade``` | ```Literal['GOOD', 'FAIR', 'WARN', 'BAD', 'NEUTRAL', 'NA']``` ⚠️ INCOMPATIBLE WITH ```grade_lt/gt``` params.| ❌ |
| ```details_grade_gt``` | ```Literal['GOOD', 'FAIR', 'WARN', 'BAD', 'NEUTRAL']``` ⚠️ INCOMPATIBLE WITH ```details_grade``` | ❌ |
| ```details_grade_lt```  | ```Literal['GOOD', 'FAIR', 'WARN', 'BAD', 'NEUTRAL']``` ⚠️ INCOMPATIBLE WITH ```details_grade``` | ❌ |
| ```details_infection_family``` | ```str``` | ❌ |
| ```details_observed_ips_contains``` | ```str``` as an IP address | ❌ |
| ```details_vulnerabilities_severity``` | ```Literal['minor', 'moderate', 'material', 'severe']``` | ❌ |
| ```evidence_key``` | ```Literal['Domain', 'IP Address']``` | ❌ |
| ```expand``` | ```Literal['attributed_companies', 'remediation_history', 'assets.tag_details', 'tag_details']``` | ❌ |
| ```first_seen``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```first_seen_lt/gt/lte/gte``` params. | ❌ |
| ```first_seen_gt``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```first_seen``` | ❌ |
| ```first_seen_gte``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```first_seen``` | ❌ |
| ```first_seen_lt``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```first_seen``` | ❌ |
| ```first_seen_lte``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```first_seen``` | ❌ |
| ```last_remediation_status_date``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```last_remediation_status_date_lt/gt/lte/gte``` params. | ❌ |
| ```last_remediation_status_date_gt``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```last_remediation_status_date``` | ❌ |
| ```last_remediation_status_date_gte``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```last_remediation_status_date``` | ❌ |
| ```last_remediation_status_date_lt``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```last_remediation_status_date``` | ❌ |
| ```last_remediation_status_date_lte``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```last_remediation_status_date``` | ❌ |
| ```last_remediation_status_label``` | ```Literal['No Status', 'Open', 'To Do', 'Work In Progress', 'Resolved', 'Risk Accepted']``` | ❌ |
| ```last_seen``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```last_seen_lt/gt/lte/gte``` params. | ❌ |
| ```last_seen_gt``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```last_seen``` | ❌ |
| ```last_seen_gte``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```last_seen``` | ❌ |
| ```last_seen_lt``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```last_seen``` | ❌ |
| ```last_seen_lte``` | ```str``` in ```YYYY-MM-DD``` format ⚠️ INCOMPATIBLE WITH ```last_seen``` | ❌ |
| ```remediation_assignments``` | ```str``` as a user guid. See ```users.get_users``` | ❌ |
| ```risk_vector_label``` | ```str``` See [slug names](https://help.bitsighttech.com/hc/en-us/articles/360043082833-API-Fields-Risk-Types) | ❌ |
| ```severity``` | ```float``` [1-10] | ❌ |
| ```severity_gt``` | ```float``` [1-10] | ❌ |
| ```severity_lt``` | ```float``` [1-10] | ❌ |
| ```severity_lte``` | ```float``` [1-10] | ❌ |
| ```severity_gte``` | ```float``` [1-10] | ❌ |
| ```severity_category``` | ```Literal['Minor', 'Moderate', 'Material', 'Severe']``` | ❌ |
| ```tags_contains``` | ```str``` ⚠️ INFRASTRUCTURE TAGS! | ❌ |
| ```unsampled``` | ```bool``` True = include unsampled findings | ❌ |
| ```vulnerabilities``` | ```str``` as a comma-separated string of CVE IDs | ❌ |

**Example Request:**

```py
from bitsightpy import finding_details

key = '<API_KEY>'
company_guid = '11111111-1111-1111-1111-111111111111'

#severity 5+ findings:
findings = finding_details.get_findings(
    key, 
    company_guid, 
    severity_gte=5
)
```

**Example Response:**

```json
[
    {
      "temporary_id":"A9Jq47BBjea129322347d12e29c54b488752b3b71e",
      "affects_rating":false,
      "assets":[
        {
          "asset":"11.111.111.111",
          "identifier":null,
          "category":"high",
          "importance":0.09,
          "is_ip":true,
          "asset_type":"IP",
          "is_monitored":false
        }
      ],
      "details":{
        "cvss": {
          "base": [
            10.0
          ]
        },
        "check_pass":"",
        "evidence_key":"11.111.111.111:21",
        "first_seen":"2020-01-29",
        "last_seen":"2020-12-20",
        "related_findings":[ ],
        "risk_category":"Diligence",
        "risk_vector":"open_ports",
        "risk_vector_label":"Open Ports",
        "rolledup_observation_id":"_aAAa1AA_a1aAA1A1aaAAa==",
        "severity":10.0,
        "severity_category":"severe",
        "tags":[
          "Remote Office"
        ],
        "tag_details":[
          {
            "guid":"4f99d64c-c3d8-4e08-b346-14f042e97116",
            "name":"Main Web Servers",
            "is_inherited":false,
            "is_public":false
          }
        ],
        "remediation_history":{
          "last_requested_refresh_date":"2024-06-19",
          "last_refresh_status_date":"2024-06-23",
          "last_refresh_status_label":"failed",
          "last_refresh_reason_code":"asset unreachable"
        },
        "asset_overrides":[
          {
            "asset":"11.111.111.111",
            "importance":"high",
            "override_importance":null
          }
        ],
        "duration":"7 days",
        "comments":"User from Cool Company said: \"What's this finding?\" at 2018-11-29 20:30 UTC; John Doe said: \"Not a good one.\" at 2024-08-18 20:30 UTC",
        "remaining_decay":90,
        "remediated":false,
        "impacts_risk_vector_details":"AFFECTS_RATING"
        "attributed_companies":[
          {
            "guid":"44444444-cccc-4444-cccc-444444444444",
            "name":"Cool Company"
          }
        ]
      },
    }
  ]
```
