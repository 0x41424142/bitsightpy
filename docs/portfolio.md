# Portfolio Module

The portfolio module of ```bitsightpy``` provides interactions with the companies you have subscribed to.

To get started, import the module and load your API key:

```py
from bitsightpy import portfolio

key = '<API_KEY>'
```

>**Head's Up!:** Some Bitsight API parameters contain a period in their name. Due to Python rules, these periods have been changed to underscores when a user defines them in a call. The underlying base API call function handles the conversion back to a period. For example, ```risk_vector.slug``` is defined by the user as ```risk_vector_slug```.

### Get Portfolio Details API

```get_details``` lets you pull information about companies you have subscribed to.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```page_count``` | ```Union[int >= 1, 'all']``` = ```'all'``` | ❌ |
| ```fields``` | ```str ``` | ❌ |
| ```format ``` | ```str``` | ❌ |
| ```limit``` | ```int``` = 100 | ❌ |
| ```offset``` | ```int``` | ❌ |
| ```q``` | ```str``` | ❌ |
| ```sort``` | ```str``` | ❌ |
| ```countries``` | ```str``` like ```"US,CA"``` | ❌ |
| ```exclude_subscription_type_slug``` | ❌ |
| ```filter_group``` | ```str``` | ❌ |
| ```risk_vectors_grade``` | ```str``` like 'A' or 'B' | ❌ |
| ```risk_vectors_slug``` | ```str```  like ```'botnet_infections'```| ❌ |
| ```software_category``` | ```Literal['Supported', 'Unsupported', 'Unknown']``` | ❌ |
| ```software_name``` | ```str``` | ❌ |
| ```folder``` | ```str``` as a folder guid | ❌ |
| ```industry_name``` | ```str``` | ❌ |
| ```industry_slug``` | ```str``` | ❌ |
| ```infections``` | ```list[str]``` | ❌ |
| ```life_cycle_slug``` | ```str``` | ❌ |
| ```open_ports``` | ```list[str]``` like ```["SIP", "Port 8080"]``` | ❌ |
| ```products``` | ```list[str]``` | ❌ |
| ```product_types``` | ```list[str]``` | ❌ |
| ```providers``` | ```str``` | ❌ |
| ```rating``` | ```int``` where ```250 <= rating <= 900``` | ❌ |
| ```rating_gt``` | ```int``` | ❌ | 
| ```rating_gte``` | ```int``` | ❌ |
| ```rating_lt``` | ```int``` | ❌ | 
| ```rating_lte``` | ```int``` | ❌ | 
| ```relationship_slug``` | ```str``` | ❌ |
| ```security_incident_categories``` | ```list[str]``` | ❌ |
| ```subscription_type_slug``` | ```list[str]``` | ❌ |
| ```tier``` | ```str``` as a tier guid | ❌ |
| ```type``` | ```str``` | ❌ |
| ```vendor_action_plan``` | ```Literal['monitor', 'review', 'escalate']``` | ❌ |
| ```vulnerabilities``` | ```list[str]``` | ❌ |

### Get Portfolio Summary API

```get_summary``` provides a summary of companies in your portfolio. It also can help by getting lists of values that you can then pass to ```get_details```.


| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```folder``` | ```str``` as a folder guid | ❌ |
| ```tier``` | ```str``` as a tier guid | ❌ |

### Get Public Disclosures API

```get_public_disclosures``` gives a list of public breaches disclosed by companies in your portfolio.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company``` | ```str``` as a company guid | ❌ |
| ```start``` | ```str``` date formatted like ```YYYYMMDD``` | ❌ |
| ```end``` | ```str``` date formatted like ```YYYYMMDD``` | ❌ |
| ```folder``` | ```str``` as a folder guid | ❌ |
| ```severity``` | ```Literal[0, 1, 2, 3]``` where 0=informational, 3=critical | ❌ |
| ```severity_gte``` | ```Literal[0, 1, 2, 3]``` where 0=informational, 3=critical | ❌ |
| ```severity_gt``` | ```Literal[0, 1, 2, 3]``` where 0=informational, 3=critical | ❌ |
| ```severity_lte``` | ```Literal[0, 1, 2, 3]``` where 0=informational, 3=critical | ❌ |
| ```severity_le``` | ```Literal[0, 1, 2, 3]``` where 0=informational, 3=critical | ❌ |
| ```tier``` | ```str``` as a tier guid | ❌ |

### Get Contacts API

```get_contacts``` returns a list of contacts for the companies in your portfolios.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |

### Assign Contact API

```assign_contact``` allows you to assign a point of contact for a company in your portfolio.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```company_guid``` | ```str``` as a guid | ✅ |
| ```friendly_name``` | ```str``` | ✅ | 
| ```formal_name``` | ```str``` | ✅ |
| ```email``` | ```str``` | ✅ | 
| ```phone_number``` | ```str``` | ❌ |

### Edit Contact API

```edit_contact``` allows you to edit the details of the current contact listed for a company in your portfolio.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```guid``` | ```str``` as the user's guid you are editing | ✅ |
| ```company_guid``` | ```str``` as the company's guid you are editing | ✅ |
| ```friendly_name``` | ```str``` | ✅ | 
| ```formal_name``` | ```str``` | ✅ |
| ```email``` | ```str``` | ✅ | 
| ```phone_number``` | ```str``` | ❌ |

### Get Geographic IP Address Space API

```get_geographic_ipspace``` returns a dictionary showing which countries companies in your portfolio have IP address spaces in.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |

```json
{
  "companies":{
    "a940bb61-33c4-42c9-9231-c8194c305db3":{
      "ipv4":{
      "A1":123
      }
    },
    "countries":{
      "A1":{
        "name":"Demo Country 1"
      },
      "initial_counts":{
        "Demo Country 1":123
      }
    }
  }
}
```

### Get Company Identifiers API

```get_custom_identifiers``` returns a list of custom identifiers & regular Bitsight identifiers for companies in your portfolio.


| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |


```json
[
  {
    "guid": "e998279a-3748-4f3d-8595-217d0807e049",
    "name": "Foo, Inc.",
    "custom_id": "FOO-024",
  },
  {
    "guid": "c1954e2c-b04c-4bb0-8c8f-3581bae3ff3b",
    "name": "Bar Industries",
    "custom_id": "199",
  }
]
```

### Customize a Company's ID API

```customize_company_id``` allows you to create or update a company's ID.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```guid``` | ```str``` as a company guid | ✅ |
| ```name``` | ```str``` | ✅ |
| ```custom_id``` | ```str``` | ❌ |


### Bulk Add/Edit/Delete Company IDs API

```bulk_manage_ids``` lets you add, edit or delete up to 1000 company IDs at once.

>**Head's Up!:** ```add``` and ```delete``` can be specified in the same request and the edit functionality falls under the ```add``` kwarg.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```add``` | ```list[dict]``` with dictionary keys being ```'guid'``` (company guid) and ```custom_id```. ⚠️ ```custom_id``` is case-sensitive! | ❌ |
| ```delete``` | ```list[dict]``` with dictionary key being ```guid``` (company guid) | ❌ |


**Example function usage:**


```python
result = bitsightpy.portfolio.bulk_manage_ids(
    key="your_api_token",
    add=[
        {"guid": "a940bb61-33c4-42c9-9231-c8194c305db3", "custom_id": "abc123"},
        {"guid": "1b3d260c-9e23-4e19-b3a5-a0bcf67d74d9", "custom_id": "newID"}
    ],
    delete=[{"guid":"a5e23bf0-38d4-4cea-aa50-19ee75da481d"}, {"guid":"b5e23bf0-38d4-4cea-aa50-19ee75da481d"}]
)
```

**Example output:**


```json
{
  "added":[
    {
      "guid":"a940bb61-33c4-42c9-9231-c8194c305db3",
      "custom_id":"abc123"
    }
  ],
  "modified":[
    {
      "guid":"1b3d260c-9e23-4e19-b3a5-a0bcf67d74d9",
      "custom_id":"newID"
    }
  ],
  "deleted":[
    {
      "guid":"a5e23bf0-38d4-4cea-aa50-19ee75da481d",
      "custom_id":"12345"
    }
  ]
}
```

### Get Portfolio API Filters

```portfolio_api_filters``` gets infections, open ports, and vulnerabilities in your portfolio.


| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```exclude_alerts_only``` | ```bool``` | ❌ |
| ```fields``` | ```list[Literal['vulnerabilities', 'open_ports', 'infections']]``` | ❌ |
| ```format``` | ```str``` as a folder guid | ❌ |
| ```quarters_back``` | ```int``` | ❌ |
| ```rating_date``` | ```str``` formatted as YYYY-MM-DD | ❌ |
| ```show_event_evidence``` | ```bool``` | ❌ |
| ```show_ips``` | ```bool``` | ❌ |
| ```tier``` | ```list[str]``` where ```str``` is a tier guid OR ```Literal['untiered']``` for untiered companies | ❌ |

### Get Portfolio Unique Identifers API

```portfolio_unique_identifiers``` returns a list of company or country unique identifiers in your portfolio.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |


### Get Portfolio Products API

```get_portfolio_products``` Returns a list of products used by companies in your portfolio.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```page_count``` | ```Union[int >= 1, 'all']``` = ```'all'``` | ❌ |
| ```fields``` | ```str ``` | ❌ |
| ```format ``` | ```str``` | ❌ |
| ```limit``` | ```int``` = 100 | ❌ |
| ```offset``` | ```int``` | ❌ |
| ```q``` | ```str``` | ❌ |
| ```sort``` | ```str``` | ❌ |

### Get Product Usage API

```get_product_usage``` returns a list of 3rd parties that use a particular product.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```guid``` | ```str``` as a product guid | ✅ |
| ```page_count``` | ```Union[int >= 1, 'all']``` = ```'all'``` | ❌ |
| ```fields``` | ```str ``` | ❌ |
| ```format ``` | ```str``` | ❌ |
| ```limit``` | ```int``` = 100 | ❌ |
| ```offset``` | ```int``` | ❌ |
| ```q``` | ```str``` | ❌ |
| ```sort``` | ```str``` | ❌ |

### Get Product Types API

```get_product_types``` Returns a list of product types used by 3rd parties in your portfolio.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```page_count``` | ```Union[int >= 1, 'all']``` = ```'all'``` | ❌ |
| ```fields``` | ```str ``` | ❌ |
| ```format ``` | ```str``` | ❌ |
| ```limit``` | ```int``` = 100 | ❌ |
| ```offset``` | ```int``` | ❌ |
| ```q``` | ```str``` | ❌ |
| ```sort``` | ```str``` | ❌ |

### Get Service Providers API

```get_service_providers``` Returns service providers in your portfolio.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```page_count``` | ```Union[int >= 1, 'all']``` = ```'all'``` | ❌ |
| ```fields``` | ```str ``` | ❌ |
| ```format ``` | ```str``` | ❌ |
| ```limit``` | ```int``` = 100 | ❌ |
| ```offset``` | ```int``` | ❌ |
| ```q``` | ```str``` | ❌ |
| ```sort``` | ```str``` | ❌ |

### Get Companies Dependent on a Specific Service Provider API

```get_service_provider_dependents``` Returns a list of companies that rely on a specific service provider.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```guid``` | ```str``` as a provider guid | ✅ |
| ```page_count``` | ```Union[int >= 1, 'all']``` = ```'all'``` | ❌ |
| ```fields``` | ```str ``` | ❌ |
| ```format ``` | ```str``` | ❌ |
| ```limit``` | ```int``` = 100 | ❌ |
| ```offset``` | ```int``` | ❌ |
| ```q``` | ```str``` | ❌ |
| ```sort``` | ```str``` | ❌ |

### Get Service Provider Products in Your Portfolio

```get_service_provider_products``` Returns a list of products by a specific service provider that are in your portfolio.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```guid``` | ```str``` as a provider guid | ✅ |
| ```relationship_type``` | ```Literal['bitsight', 'self', 'none']``` | ❌ |
| ```page_count``` | ```Union[int >= 1, 'all']``` = ```'all'``` | ❌ |
| ```fields``` | ```str ``` | ❌ |
| ```format ``` | ```str``` | ❌ |
| ```limit``` | ```int``` = 100 | ❌ |
| ```offset``` | ```int``` | ❌ |
| ```q``` | ```str``` | ❌ |
| ```sort``` | ```str``` | ❌ |


### Get Security Rating Details of Companies API

```get_security_rating_company_details``` returns a list of security rating details for companies in your portfolio. Includes the unique identifiers of the companies.

>**Head's Up!:** This API endpoint will return an HTTP 413 error if the amount of data the server has to process to fulfill your request is deemed to be too much

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```expand``` | ```Literal['rating_details']``` ⚠️ Will cause an HTTP 413 error if you request too much data! | ❌ |
| ```period``` | ```Literal['daily', 'monthly', 'latest']``` | ❌ |
| ```start_date``` | ```str``` formatted like ```YYYY-MM-DD``` | ❌ |
| ```end_date``` | ```str``` formatted like ```YYYY-MM-DD``` | ❌ |

**Example Response:**

```json
[
  {
    "guid": "12345678-1234-1234-1234-111111111111",
    "name": "Some Company",
    "ratings": [
      {
        "date": "2023-09-01",
        "rating": 700,
        "percentile": 30,
        "risk_vectors": [
          {
            "name": "Botnet Infections",
            "rating": 800,
            "grade": "A",
            "percentile": 100
          },
          {
            "name": "Spam Propagation",
            "rating": 820,
            "grade": "A",
            "percentile": 100
          }
          // ...
        ]
      }
      // ...
    ]
  }
  // ...
]
```

### Get Security Rating Details of Countries API

`````` returns a list of security rating details for countries in your portfolio. Includes the unique identifiers of the countries.

>**Head's Up!:** This API endpoint will return an HTTP 413 error if the amount of data the server has to process to fulfill your request is deemed to be too much

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```expand``` | ```Literal['rating_details']``` ⚠️ Will cause an HTTP 413 error if you request too much data! | ❌ |
| ```period``` | ```Literal['daily', 'monthly', 'latest']``` | ❌ |
| ```start_date``` | ```str``` formatted like ```YYYY-MM-DD``` | ❌ |
| ```end_date``` | ```str``` formatted like ```YYYY-MM-DD``` | ❌ |

**Example Response:**


```json
[
  {
    "guid": "12345678-1234-1234-1234-111111111111",
    "name": "Some Country",
    "ratings": [
      {
        "date": "2023-09-01",
        "rating": 700,
        "percentile": 30,
        "risk_vectors": [
          {
            "name": "Botnet Infections",
            "rating": 800,
            "grade": "A",
            "percentile": 100
          },
          {
            "name": "Spam Propagation",
            "rating": 550,
            "grade": "D",
            "percentile": 10
          }
          // ...
        ]
      }
      // ...
    ]
  }
  // ...
]


### Get Risk Vector Grades for Companies in Your Portfolio API

```get_risk_vector_grades``` returns a list of risk vector grades for companies in your portfolio.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```page_count``` | ```Union[int >= 1, 'all']``` = ```'all'``` | ❌ |
| ```limit``` | ```int``` = 100 | ❌ |
| ```offset``` | ```int``` | ❌ |
| ```company_guid``` | ```str``` as a company guid | ❌ |
| ```folder_guid``` | ```str``` as a folder guid | ❌ |
| ```period``` | ```Literal['monthly', 'latest']``` ⚠️ ```'monthly``` returns the last year of data | ❌ |
| ```tier_guid``` | ```str``` as a tier guid | ❌ |

**Example Response:**

```json
[
    {
        "grades": [
            {
                "date": "2024-01-01",
                "risk_vectors": [
                    {
                        "risk_vector": {
                            "name": "Security Incidents",
                            "slug": "breach",
                            "risk_category": "Public Disclosures"
                        },
                        "grade": "B",
                        "percentile": 80.0,
                        "rating": 660
                    },
                    {
                        "risk_vector": {
                            "name": "DMARC",
                            "slug": "dmarc",
                            "risk_category": "Diligence"
                        },
                        "grade": "N/A",
                        "percentile": 100.0,
                        "rating": 820
                    },
                    //...
                ] 
                //...
            }
        ],
        "company": {
            "guid": "11111111-1111-1111-1111-111111111111",
            "name": "Some Company"
        }
    }
]
```

### Get Portfolio Statistics API

```get_portfolio_statistics``` returns a list of statistics for your portfolio, including the distribution of companies across rating categories, high/low/median ratings, and risk vector averages.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```folder ``` | ```str``` as a folder guid | ❌ |
| ```rating_date``` | ```str``` formatted as YYYY-MM-DD | ❌ |
| ```tier``` | ```str``` as a tier guid | ❌ |
| ```types``` | ```Literal['ratings', 'risk_vector_averages']``` | ❌ |

**Example Response:**

```json
{
  "risk_vector_averages":[
    […]
    {
      "risk_vector_id":"breach",
      "risk_vector":"Security Incidents",
      "average_grade":"A",
      "companies_below_average":130,
      "percent_companies_below_average":1.13
    }
  ],
  "ratings":{
    "min_rating":300,
    "max_rating":810,
    "median_rating":720,
    "entity_count_by_bucket":{
      "advanced":5228,
      "intermediate":5655,
      "basic":1186
    }
  }
}
```

###