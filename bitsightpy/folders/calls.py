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


def create_folder(key: str, name: str, description: str = None, content_expiry_days: int = None) -> dict:
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
        "content_expiry_days": content_expiry_days
    }

    return call_api(
        key=key, module="folders", endpoint="create_folder", post_data=post_data
    ).json()