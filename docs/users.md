# Users Module

The users module of ```bitsightpy``` lets you manipulate accounts in your Bitsight environment.

To get started, import the module and load your API key:

```py
from bitsightpy import users

key = '<API_KEY>'
```

>**Head's Up!:** Some Bitsight API parameters contain a period in their name. Due to Python rules, these periods have been changed to underscores when a user defines them in a call. The underlying base API call function handles the conversion back to a period. For example, ```risk_vector.slug``` is defined by the user as ```risk_vector_slug```.

### Get Users API

```get_users``` lets you get a list of all users in your subscription, filtering by kwargs.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```page_count``` | ```Union[int >= 1, 'all'] = 'all'``` | ❌ |
| ```limit``` | ```int >= 1 = 100``` | ❌ |
| ```offset``` | ```int >=1 = 100``` | ❌ |
| ```q``` | ```str``` | ❌ |
| ```sort``` | ```str``` | ❌ |
| ```email``` | ```str``` | ❌ |
| ```email_q``` | ```str``` | ❌ |
| ```formal_name_q``` | ```str``` | ❌ |
| ```group_guid``` | ```str``` | ❌ |
| ```guid``` | ```str``` | ❌ |
| ```is_available_for_contact``` | ```bool``` | ❌ |
| ```is_company_api_token``` | ```bool``` | ❌ |
| ```roles_slug``` | ```list[dict]``` such as ```[{'slug': 'customer_user'}]``` or ```[{'slug': 'customer_admin'}]``` | ❌ |
| ```status``` | ```Literal['Activated', 'Created', 'Deactivated']``` | ❌ |


### Create User API

```create_user``` creates a user in your Bitsight subscription.

>**Head's Up!:** Your account must be listed as an admin to create users.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```email``` | ```str``` | ✅ |
| ```roles``` | ```list[dict]``` = ```[{'slug': 'customer_user'}]``` | ❌ |
| ```status``` | ```Literal['Activated', 'Created', 'Deactivated']``` = ```'Activated'``` | ❌ |
| ```group``` (guid) | ```str``` | ❌ |
| ```friendly_name``` | ```str``` | ❌ |
| ```is_company_api_token``` | ```bool``` | ❌ |
| ```is_available_for_contact``` | ```bool``` | ❌ |
| ```formal_name``` | ```str``` | ❌ |
| ```features``` | ```list[dict]``` such as ```[{'slug': 'wfh-ro', 'value': True}]``` | ❌ |
| ```value``` | ```bool``` | ❌ |

### Get User Details API

```get_user_details``` pull all details of a single user in your subscription.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```guid``` | ```str``` | ✅ |


### Edit User API

```edit_user``` edits a user in your subscription.

>**Head's Up!:** Your account must be listed as an admin to edit users.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```guid``` | ```str``` | ✅ |

### Delete User API

```delete_user``` deletes a user in your subscription.

>**Head's Up!:** Your account must be listed as an admin to delete users.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```guid``` | ```str``` | ✅ |

### Turn On 2FA API

```turn_on_2fa``` enforces two factor authentication on an account.

>**Head's Up!:** Your account must be listed as an admin to enforce 2FA on accounts.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```guid``` | ```str``` | ✅ |

### Resend Activation Email API

```resend_activation``` will trigger the platform to resend the activation email to a user if they have not activated their account yet.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```guid``` | ```str``` | ✅ |

### Reset 2FA API

```reset_2fa``` will delete the current 2FA setup of a user.

>**Head's Up!:** Your account must be listed as an admin to reset 2FA.

| Arg | Data Type | Required |
| -- | -- | -- |
| ```key``` | ```str``` | ✅ |
| ```guid``` | ```str``` | ✅ |