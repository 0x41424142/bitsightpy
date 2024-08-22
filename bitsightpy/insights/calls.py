"""
calls.py - Contains the user-facing functions to call any of the Insights BitSight API endpoints.
"""

from typing import Union

from ..base import call_api, do_paginated_call


def get_insights(key: str, company_guid: str, **kwargs) -> list[dict]:
    """
    Get a list of BitSight insights for a company.

    Args:
        key (str): The API token to use for authentication.
        company_guid (str): The company's guid to get insights for. See https://help.bitsighttech.com/hc/en-us/articles/360055740193-GET-Portfolio-Details
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        start (str): The start date for the insights formatted as YYYY-MM-DD.
        end (str): The end date for the insights formatted as YYYY-MM-DD.
        score_delta_lt (str): Filter by rating change explanations with a score delta less than the provided value. 0 = Include rating changes of 10 points or less. If not specified, results are a deilta lower than -10 points.

    Returns:
        list[dict]: JSON containing the API response.
    """

    return call_api(
        key=key,
        module="insights",
        endpoint="get_insights",
        params={"company": company_guid, **kwargs},
    ).json()


def get_change_explanations(
    key: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get a list of BitSight rating change explanations.

    Args:
        key (str): The API token to use for authentication.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        limit (int): The number of rating change explanations to return. Defaults to 100.
        offset (int): The number of rating change explanations to skip. Defaults to 0.
        company (str): Filter by company GUID. See https://help.bitsighttech.com/hc/en-us/articles/360055740193-GET-Portfolio-Details
        date_gte (str): Filter by date greater than or equal to the provided date. Formatted as YYYY-MM-DD.
        date_lt (str): Filter by date less than the provided date. Formatted as YYYY-MM-DD.
        score_delta_gte (int): Filter by score delta greater than or equal to the provided value.
        score_delta_lt (int): Filter by score delta less than the provided value.

    Returns:
        list[dict]: JSON containing the API response.
    """

    return do_paginated_call(
        key=key,
        module="insights",
        endpoint="get_change_explanations",
        page_count=page_count,
        **kwargs
    )
