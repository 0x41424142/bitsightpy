"""
get_endpoints.py - Contains the user-facing base function to get a dictionary of all available BitSight API endpoints.
"""

from .base import call_api

def get_endpoints(key: str) -> dict:
    """
    Get a list of all available BitSight API endpoints.

    Args:
        key (str): The API token to use for authentication.

    Returns:
        dict: A dictionary containing the available endpoints.
    """
    return call_api(key=key, module="get_endpoints").json()