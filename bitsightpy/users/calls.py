"""
calls.py - Contains the user-facing functions to call any of the Users BitSight API endpoints.
"""

from typing import Union, Optional, Literal
from urllib.parse import parse_qs

from ..base import call_api, check_for_pagination


def get_users(key: str, page_count: Union[int, "all"] = "all", **kwargs) -> list[dict]:
    """
    Get a list of BitSight users.

    Args:
        key (str): The API token to use for authentication.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        limit (int): Limit the number of results returned. Default is 100.
        offset (int): Offset the results returned. Default is 100.
        q (str): Search query.
        sort (str): Sort results by a field.
        email (str): Filter by email address.
        email_q (str): Search email address.
        formal_name_q (str): Filter by user's full name.
        group_guid (str): Filter by access control group for a user. Comma-separated string of guids.
        guid (str): Filter by GUID.
        is_available_for_contact (bool): Filter by contact availability.
        is_company_api_token (bool): Filter by actual users or company API token accounts (scripting accounts).
        roles_slug (str): Filter by user role(s). Commas separated string of slugs.
        status (Literal['Activated', 'Created', 'Deactivated']): Filter by account status.

    Returns:
        list[dict]: JSON containing the API response.
    """

    # Check that page_count is valid
    if page_count != "all" and type(page_count) != int and page_count < 1:
        raise ValueError(
            f"page_count must be a positive integer or 'all', not {type(page_count)}"
        )

    responses = []
    pulled = 0

    while True:
        response = call_api(
            key=key, module="users", endpoint="get_users", params=kwargs
        )
        data = response.json()

        responses.extend(data["results"])
        pulled += 1

        if page_count != "all" and pulled >= page_count:
            print(f"Reached page limit of {page_count}.")
            break

        new_params = check_for_pagination(response)
        if not new_params:
            break
        else:
            for param in new_params:
                kwargs[param] = new_params[param]

    return responses


def create_user(
    key: str,
    email: str,
    roles: list[dict] = [{"slug": "customer_user"}],
    status: Optional[Literal["Activated", "Created", "Deactivated"]] = "Activated",
    group: list[dict] = None,
    friendly_name: str = None,
    is_company_api_token: bool = None,
    is_available_for_contact: bool = None,
    formal_name: str = None,
    features: list[dict] = None,
    value: bool = None,
) -> dict:
    """
    Create a new BitSight user.

    NOTE: Only admins can create users.

    Args:
        key (str): The API token to use for authentication.
        email (str): The user's email address.
        roles (list[dict]): A role slug for the user. MUST BE A LIST WITH A SINGLE DICT. Defaults to: [{'slug': 'customer_user'}].
        status (Optional[Literal['Activated', 'Created', 'Deactivated']]): The user's status. Default is 'Activated'.
        group (Optional[str]): The user's access control group guid. see: https://help.bitsighttech.com/hc/en-us/articles/360042641293-GET-Access-Control-Groups
        friendly_name (Optional[str]): The user's friendly name.
        is_company_api_token (Optional[bool]): Whether the user is a company API token account (scripting account).
        is_available_for_contact (Optional[bool]): Whether the user is available for contact.
        formal_name (Optional[str]): The user's full name.
        features (Optional[list[dict]]): Features for the user. MUST BE A LIST OF DICTS: [{'slug': 'wfh-ro', 'value': True}].
        value (Optional[bool]): Enable features.

    Returns:
        dict: A dictionary containing the API response.
    """

    post_data = {
        "status": status,
        "group": group,
        "roles": roles,
        "friendly_name": friendly_name,
        "is_company_api_token": is_company_api_token,
        "is_available_for_contact": is_available_for_contact,
        "formal_name": formal_name,
        "email": email,
        "features": features,
        "value": value,
    }

    # Remove any None values from the post_data
    post_data = {k: v for k, v in post_data.items() if v is not None}

    return call_api(
        key=key, module="users", endpoint="create_user", post_data=post_data
    ).json()


def get_user_details(key: str, guid: str) -> dict:
    """
    Get details for a specific BitSight user.

    Args:
        key (str): The API token to use for authentication.
        guid (str): The GUID of the user to retrieve.

    Returns:
        dict: A dictionary containing the API response.
    """

    return call_api(
        key=key, module="users", endpoint="get_user_details", params={"guid": guid}
    ).json()


def edit_user(key, guid: str, **kwargs) -> dict:
    """
    Edit a BitSight user.

    NOTE: Only admins can edit users.

    Args:
        key (str): The API token to use for authentication.
        guid (str): The GUID of the user to edit.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        group (str): The user's access control group guid. see: https://help.bitsighttech.com/hc/en-us/articles/360042641293-GET-Access-Control-Groups
        roles (list[dict]): A role slug for the user. MUST BE A LIST WITH A SINGLE DICT SUCH AS: [{'slug': 'customer_user'}].
        friendly_name (str): The user's friendly name.
        is_company_api_token (bool): Whether the user is a company API token account (scripting account).
        is_available_for_contact (bool): Whether the user is available for contact.
        formal_name (str): The user's full name.
        email (str): The user's email address.
        features (list[dict]): Features for the user. MUST BE A LIST OF DICTS: [{'slug': 'wfh-ro', 'value': True}].
        value (bool): Enable features.

    Returns:
        dict: A dictionary containing the API response.
    """

    return call_api(
        key=key,
        module="users",
        endpoint="edit_user",
        params={"guid": guid},
        post_data=kwargs,
    ).json()


def delete_user(key: str, guid: str) -> int:
    """
    Delete a BitSight user.

    NOTE: Only admins can delete users.

    Args:
        key (str): The API token to use for authentication.
        guid (str): The GUID of the user to delete.

    Returns:
        int: 204 if the user was successfully deleted.
    """

    return call_api(
        key=key, module="users", endpoint="delete_user", params={"guid": guid}
    ).json()


def turn_on_2fa(key: str, guid: str) -> int:
    """
    Require two-factor authentication for a BitSight user.

    NOTE: Only admins can require 2FA for users.

    Args:
        key (str): The API token to use for authentication.
        guid (str): The GUID of the user to require 2FA for.

    Returns:
        Literal[200, 400]: 200 if successful, 400 if user already has 2FA enabled.
    """

    return call_api(
        key=key, module="users", endpoint="turn_on_2fa", params={"guid": guid}
    ).status_code


def resend_activation(key: str, guid: str) -> int:
    """
    Resend the activation email for a BitSight user.

    Args:
        key (str): The API token to use for authentication.
        guid (str): The GUID of the user to resend the activation email to.

    Returns:
        Literal[201, 400]: 201 if successful, 400 if user is already activated.
    """

    return call_api(
        key=key, module="users", endpoint="resend_activation", params={"guid": guid}
    ).status_code


def reset_2fa(key: str, guid: str) -> int:
    """
    Reset the two-factor authentication for a BitSight user.

    NOTE: Only admins can reset 2FA for users.

    Args:
        key (str): The API token to use for authentication.
        guid (str): The GUID of the user to reset 2FA for.

    Returns:
        Literal[200, 400]: 200 if successful, 400 if user does not have 2FA enabled.
    """

    return call_api(
        key=key, module="users", endpoint="reset_2fa", params={"guid": guid}
    ).status_code
