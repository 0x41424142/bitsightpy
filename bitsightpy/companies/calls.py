"""
calls.py - Contains the user-facing functions for the companies API endpoints
"""

from typing import Union

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


def get_findings_statistics(
    key: str, company_guid: str, fields: list[str] = None, expand: str = None
) -> list[dict]:
    """
    Get statistics on findings for a specific company.

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()``` for getting company guids.
        fields (list[str], optional): Only include these specific fields in output. Defaults to None.
        expand (str, optional): expand and show more details. Defaults to None. Example values: ```"first_seen_count"```, ```"last_seen_count"```, ```"first_seen"```, ```"active_count"```, ```"resolved_count"```.

    Returns:
        list[dict]: The JSON response from the API.
    """

    params = {"guid": str(company_guid)}

    if fields and type(fields) != list:
        raise TypeError("fields must be a list of strings.")

    if fields:
        params["fields"] = fields

    if expand:
        params["expand"] = expand

    return call_api(
        key=key, module="companies", endpoint="get_findings_statistics", params=params
    ).json()


def get_findings_summaries(
    key: str, company_guid: str, fields: list[str] = None, expand: str = None
) -> dict:
    """
    Get summarized findings data for a specific company in your ratings tree.

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()``` for getting company guids.
        fields (list[str], optional): Only include these specific fields in output. Defaults to None.
        expand (str, optional): expand and show more details. Defaults to None. Example values: ```"findings_severity_counts"```.

    Returns:
        dict: The JSON response from the API.
    """

    params = {"guid": str(company_guid)}

    if fields and type(fields) != list:
        raise TypeError("fields must be a list of strings.")

    if fields:
        params["fields"] = fields

    if expand:
        params["expand"] = expand

    return call_api(
        key=key, module="companies", endpoint="get_findings_statistics", params=params
    ).json()


def get_country_details(key: str, guid: str) -> dict:
    """
    Get 1 year of Bitsight data for a specific country.

    Args:
        key (str): The API token to use for authentication.
        guid (str): The guid of a country or company. See ```bitsightpy.portfolio.get_details()``` for getting company and country guids.

    Returns:
        dict: A dictionary containing the API response.
    """

    return call_api(
        key=key,
        module="companies",
        endpoint="get_country_details",
        params={"guid": guid},
    ).json()


def get_assets(
    key: str, company_guid: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get a company's asset information (domains and IP addresses),
    including asset importance and the number of findings.

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()``` for getting company guids.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional keyword arguments for the API call.

    Returns:
        list[dict]: A list of dictionaries containing the API response.
    """

    # Check that page_count is valid
    if page_count != "all" and type(page_count) != int and page_count < 1:
        raise ValueError(
            f"page_count must be a positive integer or 'all', not {type(page_count)}"
        )

    responses = []
    pulled = 0

    # Account for if the user passes an ipaddress.IPV4Address object in the ip_address parameter
    if "ip_address" in kwargs:
        kwargs["ip_address"] = str(kwargs["ip_address"])

    while True:
        kwargs["guid"] = str(company_guid)  # account for call_api .pop-ing guid
        response = call_api(
            key=key, module="companies", endpoint="get_assets", params=kwargs
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
