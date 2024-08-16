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
