# Folders Module

The folders module of ```bitsightpy``` can be used to organize your portfolio to better understand the security performance of certain groups of companies, such as IT vendors.

To get started, import the module and load your API key:

```py
from bitsightpy import folders

key = '<API_KEY>'
```

>**Head's Up!:** Some Bitsight API parameters contain a period in their name. Due to Python rules, these periods have been changed to underscores when a user defines them in a call. The underlying base API call function handles the conversion back to a period. For example, ```risk_vector.slug``` is defined by the user as ```risk_vector_slug```.

### Get Folders API

```get_folders``` lets you get a list of all folders in your subscription, filtering by ```exclude_subscription_folders```.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```exclude_subscription_folders``` | ```bool``` = ```False``` | ❌ |

**Example Output:**

```json
[
  {
    "guid":"ffffffff-4444-4444-ffff-444444444444",
    "name":"My Folder",
    "owner":"jane.doe@example.com",
    "owner_name":"Jane Doe",
    "owner_guid":"bbbbbbbb-4444-4444-bbbb-444444444444",
    "content_expiry_days":null,
    "description":"Companies to monitor.",
    "contains_all_companies":false,
    "order":93760,
    "companies":[
      "33333333-cccc-cccc-3333-cccccccccccc",
      "22222222-dddd-2222-2222-dddddddddddd"
    ],
    "is_selected":false,
    "is_deletable":true,
    "customer_global":false,
    "can_edit_properties":true,
    "shared_options":{
      "is_shared":false,
      "user_can_share":true,
      "shared_with_all_users":false,
      "group_can_edit_contents":false,
      "group_can_edit_properties":false,
      "shared_with":[
        {
          "can_edit_folder_contents":true,
          "email":"john.doe@example.com",
          "can_edit_folder_properties":true
        }
      ],
      "user_can_edit_contents":true
    },
    "subscription_type":null,
    "email_enabled":false,
    "content_subscription_types":[
      "continuous_monitoring"
      "companies_count":2
    ]
  }
]
```

### Create a New Folder API

```create_folder``` lets you create a new folder. Folders can be used to organize your portfolio to better understand the security performance of certain groups of companies, such as IT vendors.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```name``` | ```str``` | ✅ |
| ```description``` | ```str``` | ❌ |
| ```content_expiry_days``` | ```int``` | ❌ |

**Example Output:**

```json
{
    "guid": "11111111-1111-1111-1111-111111111111",
    "name": "Test Folder",
    "owner": "some.dude@somecompany.com",
    "owner_guid": "22222222-2222-2222-2222-222222222222s",
    "content_expiry_days": 1,
    "description": "This is a test folder.",
    "contains_all_companies": false,
    "order": 537440,
    "companies": [],
    "territories": [],
    "is_my_company": false,
    "is_selected": false,
    "is_deletable": true,
    "customer_global": false,
    "can_edit_properties": true,
    "shared_options": {
        "is_shared": false,
        "user_can_share": true,
        "shared_with_all_customer_users": false,
        "shared_with_all_users": false,
        "group_can_edit_contents": false,
        "group_can_edit_properties": false,
        "shared_with": [],
        "shared_with_groups": [],
        "user_can_edit_contents": true
    },
    "subscription_type": null,
    "email_enabled": false,
    "content_subscription_types": [],
    "companies_count": 0
}
```

### Delete a Folder API

```delete_folder``` lets you delete a folder.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```folder_guid``` | ```str``` | ✅ |


Returns an HTTP ```204``` if successful.


### Edit Folder API

```edit_folder``` lets you edit various folder properties.

>**Head's Up!:** This endpoint accepts multiple ```email```, ```can_edit_folder_properties``` and ```can_edit_folder_contents``` kwargs, specified like: ```email[X]```, ```can_edit_folder_properties[X]``` and ```can_edit_folder_contents[X]``` where X is an integer. This process is done to build the JSON payload the API endpoint expects dynamically and to save the user from crafting a list of dictionaries to pass in as a kwarg. See the example request below for more details.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```folder_guid``` | ```str``` | ✅ |
| ```name``` | ```str``` | ❌ |
| ```content_expiry_days``` | ```int``` | ❌ |
| ```description``` | ```str``` | ❌ |
| ```is_shared``` | ```bool``` | ❌ |
| ```shared_with_all_users``` | ```bool``` | ❌ |
| ```email[X]``` where X is an integer | ```str``` | ❌ |
| ```can_edit_folder_properties[X]``` where X is an integer | ```bool``` | ❌ |
| ```can_edit_folder_contents[X]``` where X is an integer | ```bool``` | ❌ |
| ```group_can_edit_contents``` | ```bool``` | ❌ |
| ```group_can_edit_properties``` | ```bool``` | ❌ |

Returns the following int:

| Return | Description |
| -- | -- |
| ```200``` | Folder edited successfully. |
| ```401``` | Unauthorized. |
| ```404``` | Folder not found. |

**Example Request:**

```py

result = folders.edit_folder(
  key=key,
  folder_guid='11111111-1111-1111-1111-111111111111',
  name='Test Folder (Edited)',
  description='This is a test folder that has been edited.',
  content_expiry_days=2,
  is_shared=True,
  shared_with_all_users=False,
  # Build the permissions for the first user to be shared with:
  email='my.email@company.com',
  can_edit_folder_properties=True,
  group_can_edit_contents=True,
  # Build the permissions for the second user to be shared with:
  email1='second.email@company.com',
  can_edit_folder_properties1=True,
  group_can_edit_contents1=True
)
```

**Example Output:**

```bash
200
```

### Manage Shared Folder Permissions API

```manage_shared_folder_perms``` lets you manage user permissions for shared folders.

>**Head's Up!:** You must be the folder owner to manage permissions.

>**Head's Up!:** This endpoint accepts multiple ```email```, ```can_edit_folder_properties``` and ```can_edit_folder_contents``` kwargs, specified like: ```email[X]```, ```can_edit_folder_properties[X]``` and ```can_edit_folder_contents[X]``` where X is an integer. This process is done to build the JSON payload the API endpoint expects dynamically and to save the user from crafting a list of dictionaries to pass in as a kwarg. See the example request below for more details.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```folder_guid``` | ```str``` | ✅ |
| ```is_shared``` | ```bool``` | ❌ |
| ```group_can_edit_contents``` | ```bool``` | ❌ |
| ```shared_with_all_users``` | ```bool``` | ❌ |
| ```email``` | ```str``` | ❌ |
| ```can_edit_folder_contents``` | ```bool``` | ❌ |
| ```can_edit_folder_properties``` | ```bool``` | ❌ |

**Example Request:**

```py
result = bitsightpy.folders.manage_shared_folder_perms(
    key=key,
    folder_guid=folder_guid,
    is_shared=True,
    shared_with_all_users=False,
    group_can_edit_contents=True,
    email="email.1@company.com",
    can_edit_folder_properties=True,
    can_edit_folder_contents=True,
    email1="email.2@company.com",
    can_edit_folder_properties1=False,
    can_edit_folder_contents1=False
)
```

**Example Output:**

```json
{
  "guid": "11111111-1111-1111-1111-111111111111",
  "name": "My Folder",
  "owner": "some.email@company.com",
  "owner_name": "Bob Bobson",
  "owner_guid": "11111111-1111-1111-1111-111111111111",
  "content_expiry_days": 1,
  "description": "My Folder Description",
  "contains_all_companies": false,
  "order": 1234567,
  "companies": [],
  "territories": [],
  "is_my_company": false,
  "is_selected": false,
  "is_deletable": true,
  "customer_global": false,
  "can_edit_properties": true,
  "shared_options": {
    "is_shared": true,
    "user_can_share": true,
    "shared_with_all_customer_users": false,
    "shared_with_all_users": false,
    "group_can_edit_contents": false,
    "group_can_edit_properties": false,
    "shared_with": [
      {
        "email": "email.1@company.com",
        "can_edit_folder_contents": true,
        "can_edit_folder_properties": true
      },
      {
        "email": "email.2@company.com",
        "can_edit_folder_contents": false,
        "can_edit_folder_properties": false
      }
    ],
    "shared_with_groups": [],
    "user_can_edit_contents": true
  },
  "subscription_type": null,
  "email_enabled": false,
  "content_subscription_types": [],
  "companies_count": 0
}
```

### Add Companies to a Folder API

```add_companies_to_folder``` adds companies to an existing folder.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```add_companies``` | ```Union[list[str], str]``` as a list of company guids or a single string company guid | ✅ |
| ```folder_guid``` | ```str``` as a folder guid | ✅ |

**Example Request:**

```py
# Example with list value for add_companies
result = bitsightpy.folders.add_companies_to_folder(
  key=key,
  folder_guid=folder_guid,
  add_companies=["company_guid1", "company_guid2", ...]
)

# Example with single string value for add_companies:
result = bitsightpy.folders.add_companies_to_folder(
  key=key,
  folder_guid=folder_guid,
  add_companies="company_guid1"
)
```

**Example Output**:

```json
{
  "not_added": [
    "company_guid1"
  ],
  "added": [
    "company_guid2"
  ],
  "companies": [
    "company_guids", "now_in", "the_folder", //...
  ],
  "detail": "<Company name with company_guid1> was added to <folder name with folder_guid>."
}
```

### Remove Companies from a Folder API

```remove_companies_from_folder``` removes companies from an existing folder.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```remove_companies``` | ```Union[list[str], str]``` as a list of company guids or a single string company guid | ✅ |
| ```folder_guid``` | ```str``` as a folder guid | ✅ |

**Example Request:**

```py
# Example with list value for remove_companies
result = bitsightpy.folders.remove_companies_from_folder(
  key=key,
  folder_guid=folder_guid,
  remove_companies=["company_guid1", "company_guid2", ...]
)
```

**Example Response:**

```json
{
  "remove_companies":[
    "company_guid1",
    "company_guid2"
  ]
}
```

### Get Findings in a Folder API

```get_findings_from_folder``` gets findings for a folder.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```folder_guid``` | ```str``` | ✅ |
| ```_type``` | ```str``` | ❌ |
| ```confidence``` | ```Literal["LOW", "HIGH"]``` | ❌ |

**Example Request:**

```py
result = bitsightpy.folders.get_findings_from_folder(
  key=key,
  folder_guid=folder_guid,
  confidence="HIGH"
)
```

**Example Response:**


```json
[
  {
    "start_date":"2024-01-01",
    "end_date":"2024-01-30",
    "stats":[
      {
        "id":"CVE-2021-44228",
        "name":"CVE-2021-44228",
        "count":1,
        "severity":"HIGH",
        "severity_category":"HIGH",
        "confidence":"HIGH"
      }
    ]
  }
]
```

### Get Ratings Graph of a Folder API

```get_ratings_graph_from_folder``` gets the ratings graph for a folder.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```folder_guid``` | ```str``` | ✅ |

>**Head's Up!:** The response will contain a list of dictionaries with the following keys: ```y``` and ```x```. ```y``` is the median Bitsight rating of the companies in the folder, as displayed in the vertical axis of the graph on the Bitsight webpage. ```x``` is the date when the median rating of companies in the folder were established, as displayed in the horizontal axis of the graph on the Bitsight webpage.

**Example Request:**

```py
result = bitsightpy.folders.get_ratings_graph_from_folder(
  key=key,
  folder_guid=folder_guid
)
```

**Example Response:**

```json
{
  "name":"My Folder",
  "ratings":[
    {
      "y":690,
      "x":"2024-07-22"
    }
  ]
}
```