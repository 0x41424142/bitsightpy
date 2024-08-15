"""
call_schema.py - Contains expected params/form data/headers/etc. for
each BitSight API endpoint.
"""

from frozendict import frozendict

"""
Other than get_endpoints, dict is structred as follows:

dict[module][function] = {...}
"""

CALL_SCHEMA = frozendict(
    {
        "get_endpoints": {
            "endpoint": "",
            "params": [],
            "post_data": {},
            "use_requests_json_for_post": False,
            "method": ["GET"],
            "pagination": False,
        },
        "users": {
            "get_users": {
                "endpoint": "ratings/v2/users",
                "params": ["limit", "offset", "q", "sort", "email", "email_q", "formal_name_q", "group.guid", "guid", "is_available_for_contact", "is_company_api_token", "roles.slug", "status"],
                "post_data": {},
                "use_requests_json_for_post": False,
                "method": ["GET"],
                "pagination": True,
            },
            "create_user": {
                "endpoint": "ratings/v2/users",
                "params": [],
                "post_data": ["status", "group", "roles", "friendly_name", "is_company_api_token", "is_available_for_contact", "formal_name", "email", "features", "value"],
                "use_requests_json_for_post": True,
                "method": ["POST"],
                "pagination": False,
            },
            "get_user_details": {
                "endpoint": "ratings/v2/users/{guid}",
                "params": ["guid"],
                "post_data": {},
                "use_requests_json_for_post": False,
                "method": ["GET"],
                "pagination": False,
            },
        },
    }
)
