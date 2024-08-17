"""
calls.py - Contains the user-facing functions for the folders API endpoints
"""

from typing import Literal, Optional, Union

from ..base import call_api, check_for_pagination


def get_folders(key: str, exclude_subscription_folders: bool = False) -> list[dict]:
    """
    Get all folders associated with the authenticated user.

    Args:
        key (str): Your BitSight API key.
        exclude_subscription_folders (bool, optional): Exclude subscription folders. Defaults to False.

    Returns:
        list[dict]: A list of dictionaries containing folder information.
    """

    params = {"exclude_subscription_folders": exclude_subscription_folders}

    return call_api(
        key=key, module="folders", endpoint="get_folders", params=params
    ).json()


def create_folder(
    key: str, name: str, description: str = None, content_expiry_days: int = None
) -> dict:
    """
    Create a new folder. Folders can be used to organize your portfolio to better understand the
    security performance of certain groups of companies, such as IT vendors.

    Args:
        key (str): Your BitSight API key.
        name (str): The name of the folder.
        description (str, optional): Add a description to the folder. Defaults to None.
        content_expiry_days (int, optional): How many days from creation the folder should expire. Defaults to None.

    Returns:
        dict: Details of the new folder, including guid, name, owner, description and more.
    """

    if content_expiry_days and type(content_expiry_days) != int:
        raise TypeError("content_expiry_days must be an integer.")

    post_data = {
        "name": str(name),
        "description": str(description),
        "content_expiry_days": content_expiry_days,
    }

    return call_api(
        key=key, module="folders", endpoint="create_folder", post_data=post_data
    ).json()


def delete_folder(key: str, folder_guid: str) -> int:
    """
    Delete a folder by its unique identifier.

    Args:
        key (str): Your BitSight API key.
        folder_guid (str): The unique identifier of the folder.

    Returns:
        int: 204 if successful.
    """

    params = {"guid": str(folder_guid)}

    return call_api(
        key=key, module="folders", endpoint="delete_folder", params=params
    ).status_code


def edit_folder(key: str, folder_guid: str, **kwargs) -> int:
    """
    Change attributes of a folder.

    Args:
        key (str): Your BitSight API key.
        folder_guid (str): The unique identifier of the folder.
        **kwargs: The attributes to change.

    :Kwargs:
        name (str): The name of the folder.
        description (str): Change the description of the folder.
        content_expiry_days (int): In how many days the folder should expire.
        is_shared (bool): Whether the folder is shared.
        shared_with_all_users (bool): Whether the folder is shared with all users.
        email[X] (str): The email address to share the folder with, where X is a number (e.g., email1, email2).
        can_edit_folder_properties[X] (bool): Whether the user X can edit the folder properties, where X matches the email number (e.g., email1 is married to can_edit_folder_properties1).
        can_edit_folder_contents[X] (bool): Whether the user X can edit the folder contents, where X matches the email number (e.g., email1 is married to can_edit_folder_contents1).
        group_can_edit_contents (bool): Whether all users in your group can edit companies in the folder.
        group_can_edit_properties (bool): Whether all users in your group can edit the folder properties.

    Returns:
        int: 204 if successful.
    """

    """
    Final dict structure to send to the API:

    {
        "name": str,
        "content_expiry_days": int,
        "description": str,
        "shared_options" {
            "is_shared": bool,
            "shared_with_all_users": bool,
            "group_can_edit_contents": bool,
            "group_can_edit_properties": bool,
            "shared_with": [
                {
                    "email": str,
                    "can_edit_folder_properties": bool,
                    "can_edit_folder_contents": bool
                },
                ...
            ]
        }
    }
    """

    payload = {}

    # Add simple key-value pairs to the payload:
    for k in ["name", "description", "content_expiry_days"]:
        if kwargs.get(k):
            payload[k] = kwargs[k]

    # Construct the shared_options object:
    shared_options = {}

    for k in ["is_shared", "shared_with_all_users", "group_can_edit_contents", "group_can_edit_properties"]:
        if k in kwargs:
            shared_options[k] = kwargs[k]

    # Construct the shared_with list if email is provided:
    shared_with = []

    # Find all the email1, email2, etc. keys and add them to shared_with:
    for k in kwargs:
        if "email" in k:
            shared_with.append({
                "email": kwargs[k],
                "can_edit_folder_properties": kwargs.get(f"can_edit_folder_properties{k[-1]}") if f"can_edit_folder_properties{k[-1]}" in kwargs else kwargs.get("can_edit_folder_properties"), #account for no number
                "can_edit_folder_contents": kwargs.get(f"can_edit_folder_contents{k[-1]}") if f"can_edit_folder_contents{k[-1]}" in kwargs else kwargs.get("can_edit_folder_contents") #account for no number
            })

    # Add shared_options to the payload
    if shared_options:
        payload["shared_options"] = shared_options

    # Add shared_with to shared_options if it has any keys
    if shared_with:
        payload["shared_options"]["shared_with"] = shared_with

    # Pluck the folder guid and place it in params so call_api() can format the URL
    params = {"guid": folder_guid}

    # And finally, make the API call
    return call_api(
        key=key,
        module="folders",
        endpoint="edit_folder",
        post_data=payload,
        params=params,
    ).status_code


def manage_shared_folder_perms(key: str, folder_guid: str, **kwargs) -> dict:
    """
    Manage user permissions for shared folders

    Args:
        key (str): Your BitSight API key.
        folder_guid (str): The unique identifier of the folder.
        **kwargs: The attributes to change.

    :Kwargs:
        is_shared (bool): Whether the folder is shared.
        group_can_edit_contents (bool): Whether all users in your group can edit companies in the folder.
        shared_with_all_users (bool): Whether the folder is shared with all users.
        email[X] (str): The email address to share the folder with, where X is a number (e.g., email1, email2).
        can_edit_folder_properties[X] (bool): Whether the user X can edit the folder properties, where X matches the email number (e.g., email1 is married to can_edit_folder_properties1).
        can_edit_folder_contents[X] (bool): Whether the user X can edit the folder contents, where X matches the email number (e.g., email1 is married to can_edit_folder_contents1).

    Returns:
        dict: The updated folder object's details.
    """

    """
    Like edit_folder above, this function constructs a payload to send to the API. The payload is constructed like this:

    {
        "shared_options" : {
            "is_shared" : bool,
            "group_can_edit_contents" : bool,
            "shared_with_all_users" : bool,
            "shared_with_users" : [
                {
                    "email" : str,
                    "can_edit_folder_properties" : bool,
                    "can_edit_folder_contents" : bool
                },
                ...
            ]
        }
    }
    """
    payload = {}

    # Construct the shared_options object:
    shared_options = {}

    for k in ["is_shared", "shared_with_all_users", "group_can_edit_contents"]:
        if k in kwargs:
            shared_options[k] = kwargs[k]

    # Construct the shared_with_users list if email[X] is provided:
    shared_with_users = []

    # Find all the email, email1, email2, etc. keys and add them to shared_with_users:
    for k in kwargs:
        if "email" in k:
            shared_with_users.append({
                "email": kwargs[k],
                "can_edit_folder_properties": kwargs.get(f"can_edit_folder_properties{k[-1]}") if f"can_edit_folder_properties{k[-1]}" in kwargs else kwargs.get("can_edit_folder_properties"), #account for no number
                "can_edit_folder_contents": kwargs.get(f"can_edit_folder_contents{k[-1]}") if f"can_edit_folder_contents{k[-1]}" in kwargs else kwargs.get("can_edit_folder_contents") #account for no number
            })

    # Add shared_options to the payload
    if shared_options:
        payload["shared_options"] = shared_options

    # Add shared_with_users to shared_options if it has any keys
    if shared_with_users:
        payload["shared_options"]["shared_with_users"] = shared_with_users

    # Pluck the folder guid and place it in params so call_api() can format the URL
    params = {"guid": folder_guid}

    # And finally, make the API call
    return call_api(
        key=key,
        module="folders",
        endpoint="manage_shared_folder_perms",
        post_data=payload,
        params=params,
    ).json()
