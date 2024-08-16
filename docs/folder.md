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