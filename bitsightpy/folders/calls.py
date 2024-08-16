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
        description (str): Change the description to the folder.
        content_expiry_days (int): In how many days the folder should expire.
        is_shared (bool): Whether the folder is shared.
        shared_with_all_users (bool): Whether the folder is shared with all users.
        email (str): The email address to share the folder with.
        can_edit_folder_properties (bool): Whether the user specified in 'email' can edit the folder properties.
        can_edit_folder_contents (bool): Whether the user specified in 'email' can edit the folder contents.
        group_can_edit_contents (bool): Whether all users in your group can edit companies in the folder.
        group_can_edit_properties (bool): Whether all users in your group can edit the folder properties.

    Returns:
        int: 204 if successful.
    """

    payload = {}

    # Add simple key-value pairs to the payload:
    for k in ["name", "description", "content_expiry_days"]:
        if kwargs.get(k):
            payload[k] = kwargs[k]

    # Construct the shared_options object:
    shared_options = {}

    if "is_shared" in kwargs:
        shared_options["is_shared"] = kwargs["is_shared"]
    if "shared_with_all_users" in kwargs:
        shared_options["shared_with_all_users"] = kwargs["shared_with_all_users"]
    if "group_can_edit_contents" in kwargs:
        shared_options["group_can_edit_contents"] = kwargs["group_can_edit_contents"]
    if "group_can_edit_properties" in kwargs:
        shared_options["group_can_edit_properties"] = kwargs[
            "group_can_edit_properties"
        ]

    # Construct the shared_with dictionary if email is provided:
    shared_with = {}
    if "email" in kwargs:
        shared_with["email"] = kwargs["email"]
    if "can_edit_folder_properties" in kwargs:
        shared_with["can_edit_folder_properties"] = kwargs["can_edit_folder_properties"]
    if "can_edit_folder_contents" in kwargs:
        shared_with["can_edit_folder_contents"] = kwargs["can_edit_folder_contents"]

    # Add shared_options to the payload if it has any keys:
    if shared_options:
        payload["shared_options"] = shared_options

    # Add shared_with to shared_options if it has any keys:
    if shared_with:
        payload["shared_options"]["shared_with"] = shared_with

    # Pluck the folder guid and place it in params so call_api() can format the URL:
    params = {"guid": folder_guid}

    # And finally, make the API call:
    return call_api(
        key=key,
        module="folders",
        endpoint="edit_folder",
        post_data=payload,
        params=params,
    ).status_code
