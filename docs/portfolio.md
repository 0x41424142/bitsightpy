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

