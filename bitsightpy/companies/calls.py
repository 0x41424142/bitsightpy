"""
calls.py - Contains the user-facing functions for the companies API endpoints
"""

from typing import Literal, Optional, Union

from ..base import call_api, check_for_pagination


def get_company_details(key: str, company_guid: str, fields: list[str] = None) -> dict:
    """
    Get a company's details, including their rating, rating history,
    risk vector grades, company information & relationship details.

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()``` for getting company guids.
        fields (list[str], optional): Only include specific fields in the output, such as ["industry_average", "industry_percentile"]. Defaults to None.

    Returns:
        dict: The company's details as a dictionary.
    """

    params = {"guid": str(company_guid)}

    if fields and type(fields) != list:
        raise TypeError("fields must be a list of strings.")

    if fields:
        params["fields"] = fields

    return call_api(
        key=key, module="companies", endpoint="get_company_details", params=params
    ).json()
