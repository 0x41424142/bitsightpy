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