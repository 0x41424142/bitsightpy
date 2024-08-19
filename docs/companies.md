# Companies Module

The companies module of ```bitsightpy``` can be used to retrieve information about all companies in your portfolio, including; their most recent rating, rating history, current risk vector grades. It also includes details about a company in your portfolio (several informational keys and an array of objects) and an optional quick reference to your organization's company GUID (if “My Company” is set).

To get started, import the module and load your API key:

```py
from bitsightpy import companies

key = '<API_KEY>'
```

>**Head's Up!:** Some Bitsight API parameters contain a period in their name. Due to Python rules, these periods have been changed to underscores when a user defines them in a call. The underlying base API call function handles the conversion back to a period. For example, ```risk_vector.slug``` is defined by the user as ```risk_vector_slug```.

### Get Company Details API

```get_company_details``` returns a company's details, including their rating, rating history, risk vector grades, company information & relationship details. 

You can use ```bitsightpy.portfolio.get_details()``` to get a list of companies and their guids.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company_guid``` | ```str``` as a company guid | ✅ |
| ```fields``` | ```list[str]``` (include specific fields in the output) | ❌ |

**Example Output:**

```json
{
  "guid":"a940bb61-33c4-42c9-9231-c8194c305db3",
  "custom_id":"MyCo",
  "name":"Saperix, Inc.",
  "description":"Saperix Technologies LLC develops risk analysis software solutions.",
  "ipv4_count":4172,
  "people_count":300,
  "shortname":"Saperix",
  "industry":"Technology",
  "industry_slug":"technology",
  "sub_industry":"Computer & Network Security",
  "sub_industry_slug":"computer_network_security",
  "homepage":"http://www.saperix.com",
  "primary_domain":"saperix.com",
  "type":"CURATED",
  "display_url":"https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/overview/",
  "rating_details":{
    […]
    "data_breaches":{
      "name":"Security Incidents",
      "rating":800,
      "grade":"B",
      "percentile":70,
      "grade_color":"#526d96",
      "category":"Public Disclosures",
      "category_order":3,
      "beta":false,
      "order":19,
      "display_url":"https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/rating-details/?vector=news"
    }
  },
  "ratings":[
    […]
    {
      "rating_date":"2021-06-01",
      "rating":490,
      "range":"Basic",
      "rating_color":"#b24053"
    }
  ],
  "search_count":9270,
  "subscription_type":"Total Risk Monitoring",
  "sparkline":"https://api.bitsighttech.com/ratings/v1/companies/a940bb61-33c4-42c9-9231-c8194c305db3/sparkline?size=small",
  "subscription_type_key":"continuous_monitoring",
  "subscription_end_date":null,
  "confidence":"HIGH",
  "bulk_email_sender_status":"NONE",
  "service_provider":false,
  "customer_monitoring_count":232,
  "available_upgrade_types":[ ],
  "has_company_tree":true,
  "has_preferred_contact":true,
  "is_bundle":false,
  "rating_industry_median":"below",
  "primary_company":{
    "guid":"eed24cfa-c3ea-4467-aefa-89648881e277",
    "name":"Saperix Corporate"
   },
   "permissions":{
    "can_manage_primary_company":true,
    "can_annotate":true,
    "can_view_ip_attributions":true,
    "can_view_infrastructure":true,
    "can_view_forensics":true,
    "can_download_company_report":true,
    "can_view_company_reports":true,
    "can_view_service_providers":true,
    "can_request_self_published_entity":true,
    "has_control":true
  },
  "is_primary":false,
    "is_unsampled_allowed":true,
  "in_spm_portfolio":true,
  "is_mycomp_mysubs_bundle":false,
  "company_features":[
    {
      "name":"Risk Quantification",
      "slug":"risk-quantification"
    }
  ],
  "compliance_claim":{
    "trust_page":"https://saperix.com/compliance",
    "certifications":[
      […]
      {
        "name":"NIST CSF",
        "slug":"nist-csf"
      }
    ]
  },
  "related_companies":[ ]
}
```

### Get Findings Statistics API

```get_findings_statistics``` returns stats on findings for a specific company.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company_guid``` | ```str``` as a company guid | ✅ |
| ```fields``` | ```list[str]``` (include specific fields in the output) | ❌ |
| ```expand``` | ```str``` such as ```'first_seen_count```, ```first_seen```, ```last_seen_count```, ```resolved_count```, ```active_count```. ⚠️ ONLY VALID IF YOUR SUBSCRIPTION HAS ATTACK SURFACE ANALYTICS ENABLED. | ❌ |

**Example Output:**

```json
[
  {
    "start_date": "2022-12-01",
    "end_date": "2023-01-01",
    "count": 47,
    "first_seen_count": 1,
    "last_seen_count": 1,
    "active_count": 0,
    "resolved_count": 0
  }
]
```

### Get Findings Summaries API

```get_findings_summaries``` returns summarized findings data for a specific company in your ratings tree.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company_guid``` | ```str``` as a company guid | ✅ |
| ```fields``` | ```list[str]``` (include specific fields in the output) | ❌ |
| ```expand``` | ```str``` such as ```'findings_severity_counts'```. ⚠️ ONLY VALID IF YOUR SUBSCRIPTION HAS ATTACK SURFACE ANALYTICS ENABLED. | ❌ |

**Example Output:**

```json
{
  "findings_count": 10,
  "findings_risk_vector_counts": [
    {
      "count": 2,
      "risk_vector": {
        "slug": "spf"
      }
    },
    {
      "count": 8,
      "risk_vector": {
        "slug": "dkim"
      }
    }
  ]
}
```

### Get Country Details API

```get_country_details``` pulls 1 year of Bitsight data on an entity.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```guid``` | ```str``` as a company or country guid | ✅ |

**Example Request:**

```py
result = bitsightpy.companies.get_country_details(
  key=api_token,
  guid='country_guid'
)
```

**Example Response:**

```json
{
  "guid": "11111111-1111-1111-1111-111111111111",
  "custom_id": null,
  "name": "Name",
  "description": " ",
  "ipv4_count": 0,
  "people_count": 1234567,
  "industry": null,
  "homepage": null,
  "primary_domain": null,
  "type": "COUNTRY",
  "display_url": null,
  "rating_details": {
    […]
  },
  "ratings": [
    […]
  ],
  "search_count": 0,
  "subscription_type": "Countries",
  "subscription_type_key": "countries",
  "subscription_end_date": null,
  "confidence": "LOW",
  "bulk_email_sender_status": "NONE",
  "service_provider": false,
  "customer_monitoring_count": 3
}
```

### Get Assets API

```get_assets``` returns a company's asset information (domains & IPs), including asset importance and number of findings.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company_guid``` | ```str``` as a company guid | ✅ |
| ```page_count``` | ```Union[int, 'all']``` = ```'all'``` Number of pages to return. Defaults to 'all' | ❌ |
| ```limit``` | ```int``` = 100 (number of assets to return per page) | ❌ |
| ```offset``` | ```int``` = 100 (number of assets to skip) | ❌ |
| ```q``` | ```str``` (search query) | ❌ |
| ```sort``` | ```str``` | ❌ |
| ```asset``` | ```str``` as a domain name | ❌ |
| ```combined_overrides_importance``` | ```str``` as a comma-separated string of importances. Example: "medium,none" | ❌ |
| ```expand``` | ```Literal['tag_details', 'delegated_security_controls']```. Can be a comma-separated string of the two options. | ❌ |
| ```findings_total_count``` | ```int``` | ❌ |
| ```findings__total_count_lt``` | ```int``` | ❌ |
| ```findings__total_count_gt``` | ```int``` | ❌ |
| ```findings__total_count_lte``` | ```int``` | ❌ |
| ```findings__total_count_gte``` | ```int``` | ❌ |
| ```hosted_by_isnull``` | ```bool``` | ❌ |
| ```importance_categories``` | ```str``` as a comma-separated string of importance categories. Example: "critical,high" | ❌ |
| ```importance_overrides``` | ```str``` as a comma-separated string of importances. Example: "medium,none" | ❌ |
| ```ip_address``` | ```Union[str, ipaddress.IPv4Address]``` | ❌ |
| ```is_ip``` | ```bool``` (True = only return IP addresses, False = only return domains) | ❌ |
| ```origin_subsidiary_isnull``` | ```bool``` | ❌ |
| ```overrides_isnull``` | ```bool``` | ❌ |
| ```tags_contains``` | ```list[str]``` Example: ["tag1", "tag2"] | ❌ |
| ```tags_isnull``` | ```bool``` | ❌ |


The following kwargs are only valid if your subscription has Attack Surface Analytics enabled:

| Arg | Data Type | Required |
| -- | -- | -- |
| ```countries``` | ```str``` as a comma-separated string of country names. Example: "Canada,Mexico" | ❌ |
| ```country_codes``` | ```str``` as a comma-separated string of country codes. Example: "US,CA" | ❌ |
| ```hosted_by_guid``` | ```str``` as a service provider guid (See ```portfolio.get_service_providers```) | ❌ |
| ```origin_subsidiary_guid``` | ```str``` as an entity guid (See ```portfolio.get_ratings_tree```) | ❌ |
| ```product_name-version``` | ```str``` as a comma separated string of product ```name:version``` pairs (None = unspecified version, Empty = all versions) | ❌ |
| ```product_support``` | ```Literal['current-package', 'current-version', 'incomplete_version', 'obsolete-os-release', 'obsolete-package', 'obsolete-version', 'possible-backports', 'unknown', 'unknown-patch-status]``` | ❌ |
| ```product_vendor``` | ```str``` as a service provider guid (See ```portfolio.get_service_providers```) | ❌ |
| ```services``` | ```str``` as a comma-separated string of service names. | ❌ |
| ```threat_evidence_certainty``` | ```str ['Possible', 'Likely' 'Confirmed']``` as a comma-separated string. | ❌ |
| ```threat_exposure_detection``` | ```str ['Currently', 'Previously']``` as a comma-separated string. | ❌ |
| ```threat_guid``` | ```str``` as a vulnerability guid. | ❌ |
| ```threat_severity_level``` | ```str ['minor', 'moderate', 'material', 'severe']``` | ❌ |

**Example Request:**

```py
result = bitsightpy.companies.get_assets(
  key=api_token,
  company_guid='company_guid',
)
```

**Example Output:**

```json
[
    […]
    {
      "temporary_id":"tN0i7cUlKZ2e3df1d478e1f9d6da100069f0740915e3896db99bdd2f029566e140671c1683",
      "asset":"12.3.456.789",
      "asset_type":"IP",
      "identifier":null,
      "app_grade":null,
      "ip_addresses":[
        "11.2.333.444"
      ],
      "country_code":"A1",
      "country":"Demo Country 1",
      "hosted_by":{
        "guid":"a5e23bf0-38d4-4cea-aa50-19ee75da481d",
        "name":"Fake Company Technologies"
      },
      "importance":0.0,
      "importance_category":"low",
      "longitude":-123.1234,
      "latitude":12.1234,
      "is_ip":true,
      "services":[
        "HTTP",
        "HTTPS"
      ],
      "origin_subsidiary":{
        "guid":"13b3c162-e597-46da-bac9-7dde651a9b2c",
        "name":"Demo, Inc."
      },
      "findings":{
        "total_count":3,
        "counts_by_severity":{
          "severe":0,
          "material":0,
          "moderate":0,
          "minor":3
        }
      },
      "threats":{
        "rolledup_observation_ids":[
          "12345AAbA6Abb_bAAAA7bb==",
          "AAAAbA12bAbAAAbAAbbbbb=="
        ],
        "evidence_keys":[
          "Android 10 / Chrome Mobile WebView 113.0.5672",
          […]
        ]
      },
      "tags":[
        "Guest WiFi",
        "Corporate Network"
      ],
      "tag_details":[
        {
          "guid":"ae87bc30-a3ab-45f7-809f-61ec36978685",
          "name":"Data Center 1",
          "is_inherited":false,
          "is_public":true
        }
      ],
      "overrides":{
        "importance":null
      },
      "combined_overrides":{
        "importance":"low"
      },
      "products":[
        {
          "type":"application",
          "vendor":"examplecompany",
          "product":"productname",
          "version":null,
          "support":"unknown"
        }
      ],
      "is_monitored":false
    }
  ]
```

### Get Asset Risk Matrix API

```get_asset_risk_matrix``` returns counts and the severity of security findings for a company, including findings within the last 60 days. Findings are grouped by importance of the asset in a 3x3 or 4x4 matrix.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company_guid``` | ```str``` as a company guid | ✅ |

**Example Request:**

```py
result = bitsightpy.companies.get_asset_risk_matrix(
  key=api_token,
  company_guid='company_guid',
)
```

**Example Response:**

```json
{
  "assets": [
    {
      "asset": "foobar.com",
      "importance": 0,
      "importance_category": "low",
      "stats": {
        "grades": {
          "total": 2,
          "good": 1,
          "fair": 0,
          "warn": 0,
          "bad": 0,
          "neutral": 1,
          "na": 0
        }
      },
      "tags": [ ]
    },
    […]
  ],
  "stats": {
    "critical": {
      "grades": {
        "total": 33,
        "good": 11,
        "fair": 18,
        "warn": 4,
        "bad": 0,
        "neutral": 0,
        "na": 0
      }
    },
    […]
  }
}
```

### Get Ratings Tree API

```get_ratings_tree``` returns a company's ratings tree, including its subsidiaries and those subsidiaries' subsidiaries.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |


**Example Request:**

```py
result = bitsightpy.companies.get_ratings_tree(
  key=api_token,
)
```

**Example Response:**

```json
{
  "guid":"11111111-1111-1111-1111-111111111111",
  "name":"Company, Inc.",
  "rating":500,
  "industry":"Technology",
  "is_service_provider":false,
  "rating_type":"CURATED",
  "is_subscribed":true,
  "is_primary":false,
  "children":[
    […]
  ],
  "is_bundled":false,
  "has_control":true,
  "is_shell":false
}
```

### Get IP Addresses by Country API

```get_ips_by_country``` returns a count of how many IP addresses a company has by country.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company_guid``` | ```str``` as a company guid | ✅ |


**Example Request:**

```py
result = bitsightpy.companies.get_ips_by_country(
  key=api_token,
  company_guid='company_guid',
)
```


**Example Response:**

```json
{
  "ipv4": {
    "US": 2,
    "CA": 1,
    […]
  }
}
```

### Get NIST CSF Report API

```get_nist_csf``` returns a high-level summary of a company's alignment with NIST CSF by using Bitsight's risk vectors and existing data as evidence.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company_guid``` | ```str``` as a company guid | ✅ |


**Example Request:**

```py
result = bitsightpy.companies.get_nist_csf(
  key=api_token,
  company_guid='company_guid',
)
```

**Example Response:**

```json
{
  "requested_by": {
    "company_guid": "11111111-1111-1111-1111-111111111111",
    "company_name": "Company, Inc."
  },
  "company": "Company",
  "functions": [
    {
      "nist_grade": "A",
      "name": "Identify",
      "categories": [
        {
          "nist_grade": "A",
          "description": "The data, personnel, devices, systems, and facilities that enable the organization to achieve business purposes are identified and managed consistent with their relative importance to business objectives and the organization’s risk strategy.",
          "subcategories": [
            {
              "supported": false,
              "name": "ID.AM-1",
              "description": "Physical devices and systems within the organization are inventoried."
            },
            {
              "nist_grade": "A",
              "name": "ID.AM-2",
              "supported": true,
              "summary": "Using Bitsight Security Ratings, an organization can confirm the effectiveness of its policies by quantifying the organization’s security posture.",
              "risk_vectors": [
                {
                  "risk_type": "requirements",
                  "value": "Bitsight Security Ratings"
                }
              ],
              "description": "Software platforms and applications within the organization are inventoried."
            },
            […]
            {
              "supported": false,
              "name": "ID.AM-6",
              "description": "cybersecurity roles and responsibilities for the entire workforce and third-party stakeholders (e.g., suppliers,customers, partners) are established."
            }
          ],
        }
      ]
    }
  ]
}
```

### Preview Report with Industry Comparison API

```preview_report_industry_comparison``` returns a synopsis of a company's security posture compared to its industry peers. It includes a company's rating on the first day of the current quarter, the company's rating on the first day of the previous quarter and risk vectors by industry.


| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company_guid``` | ```str``` as a company guid | ✅ |

**Example Request:**

```py
result = bitsightpy.companies.preview_report_industry_comparison(
  key=api_token,
  company_guid='company_guid',
)
```

**Example Response:**

```json
{
  "company":{
    "company_guid":"eed24cfa-c3ea-4467-aefa-89648881e277",
    "report_date":"July 9, 2019",
    "name":"Company",
    "url":"http://company.com/corporate",
    "industry":"Technology",
    "ratings":[
      {
        "rating_date":"2024-05-01",
        "rating":720,
        "range":"Intermediate",
        "rating_color":"#e8a951",
        "industry_percentile":90
      },
      […]
    ],
    "rating_details":[
      […]
      {
        "category":"Diligence",
        "name":"SPF",
        "industry_comparison":"Below Industry Average",
        "slug":"spf"
      }
    ]
  }
}
```

### Get Products in a Ratings Tree API

```get_products_in_ratings_tree``` returns a list of service provider products that are used by companies in a ratings tree.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company_guid``` | ```str``` as a company guid | ✅ |
| ```fields``` | ```str``` as a comma-separated string of fields to include in the output | ❌ |
| ```limit``` | ```int``` | ❌ |
| ```offset``` | ```int``` | ❌ |
| ```q``` | ```str``` (full-text search) | ❌ |
| ```sort``` | ```str``` (sort by a field. use a "-" to reverse order) | ❌ |

**Example Request:**

```py
result = bitsightpy.companies.get_products_in_ratings_tree(
  key=api_token,
  company_guid='company_guid',
)
```


**Example Response:**

```json
[
    {
      "product_guid":"55555555-pppp-rrrr-oooo-dddddddddddd",
      "product_name":"Company Product",
      "product_types":[
        "Order Management"
      ],
      "provider_guid":"a5e23bf0-38d4-4cea-aa50-19ee75da481d",
      "provider_name":"Company Technologies",
      "provider_industry":"Technology",
      "company_count":1,
      "domain_count":2,
      "percent_dependent":8.3,
      "percent_dependent_company":9.1,
      "relative_importance":0.10714285714285714,
      "relative_criticality":"high"
    },
    //...
  ]
```

### Get Ratings History API

```get_ratings_history``` returns a list of dictionaries containing a company's rating history over the past year.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company_guid``` | ```str``` as a company guid | ✅ |


**Example Request:**

```py
result = bitsightpy.companies.get_ratings_history(
  key=api_token,
  company_guid='company_guid',
)
```

**Example Response:**

```py
from json import dumps

#Show one day's data:
dumps(result[0], indent=2)
>>>{
  "Date": "2023-07-04",
  "Bitsight Security Rating": "700",
  "Rating percentile rank": "20",
  "Unsolicited Communications grade": "B",
  "Unsol. Comm. percentile rank": "80",
  "Potentially Exploited grade": "A",
  "Pot. Exploited percentile rank": "100",
  "Botnet Infections grade": "A",
  "Botnet Infections percentile rank": "100",
  "Malware Servers grade": "C",
  "Malware percentile rank": "65",
  "Spam Propagation grade": "A",
  "Spam Propagation percentile rank": "100",
  "SPF grade": "C",
  "SPF percentile rank": "60",
  "DKIM grade": "B",
  "DKIM percentile rank": "70",
  "SSL Configurations grade": "D",
  "SSL Configurations percentile rank": "30",
  "DNSSEC grade*": "B",
  "DNSSEC percentile rank*": "70",
  "Web Application Headers grade": "A",
  "Web Application Headers percentile rank": "90",
  "Insecure Systems grade": "A",
  "Insecure Systems percentile rank": "100",
  "Open Ports grade": "D",
  "Open Ports percentile rank": "20",
  "File Sharing grade": "A",
  "File Sharing percentile rank": "100",
  "SSL Certificates grade": "A",
  "SSL Certificates percentile rank": "90",
  "Patching Cadence grade": "A",
  "Patching Cadence percentile rank": "100",
  "Server Software grade": "A",
  "Server Software percentile rank": "90",
  "Desktop Software grade": "A",
  "Desktop Software percentile rank": "N/A",
  "Mobile Software grade": "N/A",
  "Mobile Software percentile rank": "N/A",
  "Mobile Application Security grade*": "N/A",
  "Mobile Application Security percentile rank*": "N/A",
  "Security Incidents grade": "A",
  "Security Incidents percentile rank": "100",
  "Web Application Security grade*": "D",
  "Web Application Security percentile rank*": "10",
  "DMARC grade*": "B",
  "DMARC percentile rank*": "70",
}
```

### Get Risk Vectors Summary API

```get_risk_vectors_summary``` returns a summary of a company's risk vector performance. Data includes:

- Risk vector grades
- Industry comparisons
- Event counts during the past 12 months
- The average number of days to resolve a finding
- Record count
- Finding grade distribution
- Latest 10 finding details
- Remediation suggestions


**Example Request:**

```py
result = bitsightpy.companies.get_risk_vectors_summary(
  key=api_token,
  company_guid='company_guid',
)
```

**Example Response:**

```py
from json import dumps

dumps(result[0], indent=2)
>>>[
  {
    "Risk Vector Slug": "botnet_infections",
    "Risk Vector": "Botnet Infections",
    "Grade": "A",
    "Industry Comparison": "Top 90%",
    "Event Counts Past Year": "3",
    "Average Days to Resolve": "1.5",
    "Record Count": "",
    "Grade Distribution Good": "",
    "Grade Distribution Fair": "",
    "Grade Distribution Warn": "",
    "Grade Distribution Bad": "",
    "Grade Distribution Neutral": "",
    ...
  },
  ...
]
```