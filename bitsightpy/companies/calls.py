"""
calls.py - Contains the user-facing functions for the companies API endpoints
"""

from typing import Union
from csv import DictReader

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


def get_asset_risk_matrix(key: str, company_guid: str) -> dict:
    """
    Get data from Bitsight's asset risk matrix. This data includes
    counts and severities for each asset under a given ```company_guid```,
    including findings within the last 60 days. Findings are grouped
    by the importance of the asset in a 3x3 or 4x4 matrix.

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()``` for getting company guids.

    Returns:
        dict: A dictionary containing the API response.
    """

    return call_api(
        key=key,
        module="companies",
        endpoint="get_asset_risk_matrix",
        params={"guid": company_guid},
    ).json()


def get_ratings_tree(key: str, company_guid: str) -> dict:
    """
    Get a company's ratings tree, which includes the company's
    subsidiaries and the ratings of those subsidiaries and any
    subsidiaries of the subsidiaries.

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()``` for getting company guids.

    Returns:
        dict: A dictionary containing the API response.
    """

    return call_api(
        key=key,
        module="companies",
        endpoint="get_ratings_tree",
        params={"guid": company_guid},
    ).json()


def get_ips_by_country(key: str, country_guid: str) -> dict:
    """
    Get the number of IPs a company has by country.

    Args:
        key (str): Your BitSight API key.
        country_guid (str): A country guid. See ```bitsightpy.portfolio.get_details()``` for getting country guids.

    Returns:
        dict: A dictionary containing the API response.
    """

    return call_api(
        key=key,
        module="companies",
        endpoint="get_ips_by_country",
        params={"guid": country_guid},
    ).json()


def get_nist_csf(key: str, company_guid: str) -> dict:
    """
    Get a high-level summary of a company's alignment with NIST CSF
    using Bitsight risk vectors and existing evidence.

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()``` for getting company guids.

    Returns:
        dict: A dictionary containing the API response.
    """

    return call_api(
        key=key,
        module="companies",
        endpoint="get_nist_csf",
        params={"guid": company_guid, "format": "json"},
    ).json()


def preview_report_industry_comparison(key: str, company_guid: str) -> dict:
    """
    Get a synopsis comparing a company's rating to industry peers.

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()``` for getting company guids.

    Returns:
        dict: A dictionary containing the API response.
    """

    return call_api(
        key=key,
        module="companies",
        endpoint="preview_report_industry_comparison",
        params={"guid": company_guid, "format": "json"},
    ).json()


def get_products_in_ratings_tree(
    key: str, company_guid: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get service provider products that are used by a company in a ratings tree

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()``` for getting company guids.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional keyword arguments for the API call.

    :Kwargs:
        fields (str): Comma-separated string of fields to include in the response.
        limit (int): The number of results to return per page.
        offset (int): The number of results to skip before returning. API handles pagination, so you don't really need to use this.
        q (str): A full-text search query.
        sort (str): The field to sort by. Default is 'name'. To sort in descending order, add a '-' before the field name.


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

    while True:
        kwargs["guid"] = str(company_guid)  # account for call_api .pop-ing guid
        response = call_api(
            key=key,
            module="companies",
            endpoint="get_products_in_ratings_tree",
            params=kwargs,
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


def get_ratings_history(key: str, company_guid: str) -> list[dict]:
    """
    Get a ```pandas.DataFrame``` of a company's ratings history over the past year.

    Each line contains:
    - Every day for 1 year, starting on day 1 of the current month
    - Risk vector letter grades
    - Percentile ranks, rounded to the nearest 10

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()``` for getting company guids.

    Returns:
        list[dict]: the CSV results parsed into a list of dictionaries.
    """

    response = call_api(
        key=key,
        module="companies",
        endpoint="get_ratings_history",
        params={"guid": company_guid, "format": "csv"},
    )

    # Load the CSV response
    reader = DictReader(response.text.splitlines())

    return list(reader)


def get_risk_vectors_summary(key: str, company_guid: str) -> list[dict]:
    """
    Get a summary of a company's risk vector performance. Data includes:

    - Risk vector grades
    - Industry comparisons
    - Event counts during the past 12 months
    - The average number of days to resolve a finding
    - Record count
    - Finding grade distribution
    - Latest 10 finding details
    - Remediation suggestions

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()``` for getting company guids.

    Returns:
        list[dict]: A list of dictionaries containing the API response.
    """

    response = call_api(
        key=key,
        module="companies",
        endpoint="get_risk_vectors_summary",
        params={"guid": company_guid, "format": "csv"},
    )

    # Load the CSV response
    reader = DictReader(response.content.decode("utf-8-sig").splitlines())

    return list(reader)


def get_company_requests_summary(key: str) -> dict:
    """
    Get a summary of requests your organization has made to Bitsight.

    Args:
        key (str): Your BitSight API key.

    Returns:
        dict: A dictionary containing the API response.
    """

    return call_api(
        key=key,
        module="companies",
        endpoint="get_company_requests_summary",
    ).json()


def compare_client_to_underwriting_guidelines(key: str, company_guid: str) -> dict:
    """
    Get a comparison of a client's risk vectors to your underwriting guidelines.

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()```.

    Returns:
        dict: A dictionary containing the API response.
    """

    return call_api(
        key=key,
        module="companies",
        endpoint="compare_client_to_underwriting_guidelines",
        params={"guid": company_guid},
    ).json()


def highlight_primary(
    key: str, company_guid: str, guid: str, custom_id: str = None
) -> int:
    """
    Highlight a primary organization or assign a custom ID for a portfolio company

    Args:
        key (str): Your BitSight API key.
        company_guid (str): The guid of the company to edit.
        guid (str): The guid of the primary organization.
        custom_id (str, optional): A custom ID to assign to the company. Defaults to None.
    """

    # Required to check if custom_id is a string or not because None/null value will delete
    # the custom_id from the company in the BitSight platform
    post_data = (
        {"guid": guid} if not custom_id else {"guid": guid, "custom_id": custom_id}
    )

    return call_api(
        key=key,
        module="companies",
        endpoint="highlight_primary",
        params={"guid": company_guid},
        post_data=post_data,
    ).status_code


def get_products(
    key: str, company_guid: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get a list of enterprise products used at the domains of a particular company.

    Args:
        key (str): Your BitSight API key.
        company_guid (str): A company guid. See ```bitsightpy.portfolio.get_details()``` for getting company guids.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional keyword arguments for the API call.

    :Kwargs:
        fields (str): Comma-separated string of fields to include in the response.
        limit (int): The number of results to return per page.
        offset (int): The number of results to skip before returning. API handles pagination, so you don't really need to use this.
        q (str): A full-text search query.
        sort (str): The field to sort by. Default is 'name'. To sort in descending order, add a '-' before the field name.

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

    while True:
        kwargs["guid"] = str(company_guid)  # account for call_api .pop-ing guid
        response = call_api(
            key=key,
            module="companies",
            endpoint="get_products",
            params=kwargs,
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
