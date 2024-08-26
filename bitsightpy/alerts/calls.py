"""
calls.py - Stores the user-facing functions for interacting with the alerts API.
"""

from typing import Literal, Union, Optional

from bitsightpy.base.call_api import call_api, do_paginated_call


def get_alerts(key: str, page_count: Union[int, "all"] = "all", **kwargs) -> list[dict]:
    """
    Get a list of your existing alerts in Bitsight, filtered by kwargs.

    Args:
        key (str): The API token to use for authentication.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional filters to apply to the alerts.

    ## Kwargs:

        limit (int): The maximum number of alerts to return per page. Defaults to 100.
        offset (int): The number of alerts to skip before returning results.
        sort (str): The field to sort by. Defaults to 'alert_date'. Valid values are: 'alert_date', 'guid' (alert guid), 'alert_type', 'company_name', 'folder_name', 'trigger', 'severity'
        q (str): Search company names.
        alert_date (str): Filter by alert date. Format: 'YYYY-MM-DD'.
        alert_date_gt (str): Filter by alert date greater than this value. Format: 'YYYY-MM-DD'.
        alert_date_lt (str): Filter by alert date less than this value. Format: 'YYYY-MM-DD'.
        alert_date_gte (str): Filter by alert date greater than or equal to this value. Format: 'YYYY-MM-DD'.
        alert_date_lte (str): Filter by alert date less than or equal to this value. Format: 'YYYY-MM-DD'.
        alert_type (Literal['PERCENT_CHANGE', 'RATING_THRESHOLD', 'RISK_CATEGORY', 'NIST_CATEGORY', 'INFORMATIONAL', 'PUBLIC_DISCLOSURE', 'VULNERABILITY']): Filter by alert type.
        company_guid (str): Filter by company guid. See ```portfolio.get_details``` for more information.
        expand (Literal['details']): if 'details', shows additional alert details.
        folder_guid (str): Filter by folder guid. See ```folders.get_folders``` for more information.
        severity (Literal['CRITICAL', 'WARN', 'INCREASE', 'INFORMATIONAL']): Filter by severity.

    Returns:
        list[dict]: A list of alert dictionaries.
    """

    return do_paginated_call(
        key=key, module="alerts", endpoint="get_alerts", page_count=page_count, **kwargs
    )


def get_4th_party_disclosures(
    key: str, alert_guid: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get a list of 4th party disclosures for a given alert.

    Args:
        key (str): The API token to use for authentication.
        alert_guid (str): The alert guid to get 4th party disclosures for.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional filters to apply to the disclosures.

    ## Kwargs:
        limit (int): The maximum number of disclosures to return per page. Defaults to 32.
        offset (int): The number of disclosures to skip before returning results.
        q (str): Full text search query.

    Returns:
        list[dict]: A list of 4th party disclosure dictionaries.
    """

    kwargs["guid"] = alert_guid

    return do_paginated_call(
        key=key,
        module="alerts",
        endpoint=f"get_4th_party_disclosures",
        page_count=page_count,
        **kwargs,
    )
