# bitsightpy - A Python SDK for Interacting With Bitsight APIs

```bitsightpy``` is an SDK for interacting with [Bitsight](https://bitsight.com) APIs.

![In Development](https://img.shields.io/badge/In%20DEVELOPMENT-8A2BE2?style=for-the-badge)

```py
from bitsightpy.users import get_users

key = '<API_TOKEN>'

users = get_users(key)
>>>[{'friendly_name': 'Alice Johnson', 'email': 'alice.johnson@email.com', ...}, ...]
```

## Currently Supported Modules/Calls

| Module | Status |
| -- | -- |
| ```users``` | ✅ Fully Implemented |
| ```insights``` | ✅ Fully Implemented |
| ```portfolio``` | ✅ Fully Implemented |
| ```companies``` | 🏗️ In Progress |
| ```folders``` | 🏗️ In Progress |