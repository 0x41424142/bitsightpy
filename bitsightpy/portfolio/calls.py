"""
calls.py - Contains the user-facing base function to get a dictionary of all available Bitsight API endpoints.
"""

from typing import Union

from ..base import call_api, do_paginated_call


def get_details(
    key: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Pull information about the companies in your portfolio.

    Args:
        key (str): The API token to use for authentication.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        countries (str): Filter by country. Comma-separated string of country codes. Example: US,CA
        exclude_subscription_type.slug (list[dict]) Subcription slug names to exclude. Example: [{"slug": "continuous_monitoring"}]
        filter_group (Literal['risk_vectors', 'software']): Filter by various metrics. Used with risk_vectors.slug/grade or software.name/category.
        risk_vectors_slug (str): Filter by risk vector. Example: "botnet_infections". Used in conjunction with filter_group.
        risk_vectors_grade (str): Filter by risk vector grade. Example: "A". Used in conjunction with filter_group. NOTE: This does not include N/A grades.
        software_name (str): Filter by software name. Example: "Apache". Used in conjunction with filter_group.
        software_category (Literal['Supported', 'Unsupported', 'Unknown']): Filter by software category. Used in conjunction with filter_group.
        folder (str): Filter by folder GUID. See https://help.bitsighttech.com/hc/en-us/articles/360020042473-GET-Folder-Details
        industry_name (str): Filter by industry name. See https://help.bitsighttech.com/hc/en-us/articles/360041583394-GET-Industries
        industry_slug (str): Filter by industry slug. See https://help.bitsighttech.com/hc/en-us/articles/360041583394-GET-Industries
        infections (list): Filter by infection type. See https://help.bitsighttech.com/hc/en-us/articles/360053951774-GET-Portfolio-Summary
        life_cycle_slug (str): Filter by life cycle. Example: 'onboarding,null' shows companies in onboarding and null life cycle stages.
        open_ports (list): Filter by open ports. Example: ["Port 8080", "SIP"]
        products (list): Filter by product name. Example: ['Apache', 'nginx'] See https://help.bitsighttech.com/hc/en-us/articles/360053951774-GET-Portfolio-Summary
        product_types (list): Filter by product type. Example: ['Web Server', 'Database'] See https://help.bitsighttech.com/hc/en-us/articles/360053951774-GET-Portfolio-Summary
        providers (str): Name of the service provider.
        rating (int): a 10-point incremental rating where 250 <= rating <= 900.
        rating_gt (int): Filter by rating greater than the provided value.
        rating_gte (int): Filter by rating greater than or equal to the provided value.
        rating_lt (int): Filter by rating less than the provided value.
        rating_lte (int): Filter by rating less than or equal to the provided value.
        relationship_slug (str): Filter by relationship. Example: "vendor"
        security_incident_categories (list): Filter by security incident category.
        subscriptions_type_slug (list): Filter by subscription type. Example: ["continuous_monitoring", "alerts-only"]
        tier (str): Filter by tier guid.
        type (str): Filter by company type. null/None includes companies not in a tier
        vendor_action_plan (Literal['monitor', 'review', 'escalate']): Filter by vendor action plan.
        vulnerabilities (list): Filter by vulnerability name. See https://help.bitsighttech.com/hc/en-us/articles/360053951774-GET-Portfolio-Summary

    Returns:
        list[dict]: JSON containing the API response.
    """

    return do_paginated_call(
        key=key,
        module="portfolio",
        endpoint="get_details",
        page_count=page_count,
        **kwargs,
    )


def get_summary(key: str, folder: str = None, tier: str = None) -> dict:
    """
    Get a summary of your portfolio and acceptable values for ```get_details``` filters.

    Args:
        key (str): The API token to use for authentication.
        folder (str): Filter by folder GUID. Defaults to None. See https://help.bitsighttech.com/hc/en-us/articles/360020042473-GET-Folder-Details
        tier (str): Filter by tier guid. Defaults to None. See https://help.bitsighttech.com/hc/en-us/articles/360021083694-GET-Tiers

    Returns:
        dict: A dictionary containing the API response.
    """

    return call_api(
        key=key,
        module="portfolio",
        endpoint="get_summary",
        params={"folder": folder, "tier": tier},
    ).json()


def get_public_disclosures(key: str, **kwargs) -> list[dict]:
    """
    Get a list of public disclosures for companies in your portfolio.

    Args:
        key (str): The API token to use for authentication.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        company (str): Filter by company GUID. See https://help.bitsighttech.com/hc/en-us/articles/360055740193-GET-Portfolio-Details
        start (str): Filter by start date. Formatted as YYYYMMDD.
        end (str): Filter by end date. Formatted as YYYYMMDD.
        folder (str): Filter by folder GUID. See https://help.bitsighttech.com/hc/en-us/articles/360020042473-GET-Folder-Details
        severity (Literal[0, 1, 2, 3]): Filter by severity. 0 = informational, 3 = severe.
        severity_gte (Literal[0, 1, 2, 3]): Filter by severity greater than or equal to the provided value.
        severity_gt (Literal[0, 1, 2, 3]): Filter by severity greater than the provided value.
        severity_lte (Literal[0, 1, 2, 3]): Filter by severity less than or equal to the provided value.
        severity_lt (Literal[0, 1, 2, 3]): Filter by severity less than the provided value.
        tier (str): Filter by tier guid. See https://help.bitsighttech.com/hc/en-us/articles/360021083694-GET-Tiers

    Returns:
        list[dict]: JSON containing the API response.
    """

    return call_api(
        key=key, module="portfolio", endpoint="get_public_disclosures", params=kwargs
    ).json()


def get_contacts(key: str) -> list[dict]:
    """
    Get a list of contacts for companies in your portfolio.

    Args:
        key (str): The API token to use for authentication.

    Returns:
        list[dict]: JSON containing the API response.
    """

    return call_api(key=key, module="portfolio", endpoint="get_contacts").json()


def assign_contact(
    key: str,
    company_guid: str,
    friendly_name: str,
    formal_name: str,
    email: str,
    phone_number: str = None,
):
    """
    Assigns a point of contact for a company in your portfolio.

    Args:
        key (str): The API token to use for authentication.
        company_guid (str): The GUID of the company to assign a contact to.
        friendly_name (str): The contact's friendly name.
        formal_name (str): The contact's formal name.
        email (str): The contact's email address.
        phone_number (str): The contact's phone number. Defaults to None.
    """

    post_data = {
        "company_guid": company_guid,
        "friendly_name": friendly_name,
        "formal_name": formal_name,
        "email": email,
        "phone_number": phone_number,
    }

    # Remove any None values from the post_data
    post_data = {k: v for k, v in post_data.items() if v is not None}

    return call_api(
        key=key, module="portfolio", endpoint="assign_contact", post_data=post_data
    ).json()


def edit_contact(
    key: str,
    guid: str,
    company_guid: str,
    friendly_name: str,
    formal_name: str,
    email: str,
    phone_number: str = None,
):
    """
    Edit a contact for a company in your portfolio.

    Args:
        key (str): The API token to use for authentication.
        guid (str): The GUID of the contact to edit.
        company_guid (str): The GUID of the company to assign a contact to.
        friendly_name (str): The contact's friendly name.
        formal_name (str): The contact's formal name.
        email (str): The contact's email address.
        phone_number (str): The contact's phone number. Defaults to None.
    """

    post_data = {
        "guid": guid,
        "company_guid": company_guid,
        "friendly_name": friendly_name,
        "formal_name": formal_name,
        "email": email,
        "phone_number": phone_number,
    }

    # Remove any None values from the post_data
    post_data = {k: v for k, v in post_data.items() if v is not None}

    return call_api(
        key=key,
        module="portfolio",
        endpoint="edit_contact",
        post_data=post_data,
        params={"guid": guid},
    ).json()


def get_geographic_ipspace(key: str) -> list[dict]:
    """
    Get a dictionary containing which companies in your portfolio have IP space in which countries.

    Args:
        key (str): The API token to use for authentication.

    Returns:
        list[dict]: JSON containing the API response.
    """

    return call_api(
        key=key, module="portfolio", endpoint="get_geographic_ipspace"
    ).json()


def get_custom_identifiers(key: str) -> list[dict]:
    """
    Get custom company identifiers. This is useful for associating Bitsight data with vendor-related information.

    Args:
        key (str): The API token to use for authentication.

    Returns:
        list[dict]: JSON containing the API response.
    """

    return call_api(
        key=key, module="portfolio", endpoint="get_custom_identifiers"
    ).json()


def customize_company_id(key: str, guid: str, name: str, custom_id: str):
    """
    Create/update a company's custom identifier.

    Args:
        key (str): The API token to use for authentication.
        guid (str): The GUID of the company to assign a custom identifier to. See https://help.bitsighttech.com/hc/en-us/articles/360055740193-GET-Portfolio-Details
        name (str): The name of the custom identifier.
        custom_id (str): The custom identifier.
    """

    post_data = {
        "guid": guid,
        "name": name,
        "custom_id": custom_id,
    }

    # Remove any None values from the post_data
    post_data = {k: v for k, v in post_data.items() if v is not None}

    return call_api(
        key=key,
        module="portfolio",
        endpoint="customize_company_id",
        post_data=post_data,
    ).json()


def bulk_manage_ids(key: str, **kwargs) -> dict:
    """
    Add/Edit/Delete custom identifiers for up to 1000 companies at once.

    Args:
        key (str): The API token to use for authentication.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        add (list[dict]): A list of dictionaries containing the 'guid' and 'custom_id' keys to add. Also used for editing (same format, just changes instead of creates). value under 'guid' should be the GUID of the company to add the value under 'custom_id' to.
        delete (list[dict]): A list of dictionaries containing the 'guid' key to delete. value under 'guid' should be the GUID of the company to delete the custom identifier for.

    Returns:
        dict: A dictionary containing the API response.

    :EXAMPLE:

    ```python
    result = bitsightpy.portfolio.bulk_manage_ids(
        key="your_api_token",
        add=[
            {"guid": "a940bb61-33c4-42c9-9231-c8194c305db3", "custom_id": "abc123"},
            {"guid": "1b3d260c-9e23-4e19-b3a5-a0bcf67d74d9", "custom_id": "newID"}
        ],
        delete=[{"guid":"a5e23bf0-38d4-4cea-aa50-19ee75da481d"}, {"guid":"b5e23bf0-38d4-4cea-aa50-19ee75da481d"}]
    )
    ```
    """
    if "add" not in kwargs and "delete" not in kwargs:
        raise ValueError("You must pass either 'add' or 'delete'.")

    # Make sure that add is a list of dictionaries and that those dictionaries only have 'guid' and 'custom_id' keys
    if "add" in kwargs:
        for item in kwargs["add"]:
            if type(item) != dict:
                raise ValueError(
                    f"add must be a list of dictionaries, not {type(item)}"
                )
            if "guid" not in item or "custom_id" not in item:
                raise ValueError(
                    "Each item in 'add' must have 'guid' and 'custom_id' keys."
                )

    # Make sure that delete is a list of dictionaries and that those dictionaries only have 'guid' keys
    if "delete" in kwargs:
        for item in kwargs["delete"]:
            if type(item) != dict:
                raise ValueError(
                    f"delete must be a list of dictionaries, not {type(item)}"
                )
            if "guid" not in item:
                raise ValueError("Each item in 'delete' must have 'guid' key.")

    post_data = {}

    # Handle 'add' key
    if "add" in kwargs:
        post_data["add"] = kwargs["add"]

    # Handle 'delete' key
    if "delete" in kwargs:
        post_data["delete"] = [{"guid": guid} for guid in kwargs["delete"]]

    return call_api(
        key=key, module="portfolio", endpoint="bulk_manage_ids", post_data=post_data
    ).json()


def portfolio_api_filters(key: str, **kwargs) -> dict:
    """
    Get infections, open ports, vulnerabilities, and stats about both present in your portfolio.

    Args:
        key (str): The API token to use for authentication.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        exclude_alerts_only (bool): Exclude companies with only alerts subscriptions.
        fields (Literal['vulnerabilities', 'open_ports', 'infections']): Filter by field.
        folder (str): Filter by folder GUID. See https://help.bitsighttech.com/hc/en-us/articles/360020042473-GET-Folder-Details
        format (str): Format the response. ⚠️ SDK force-sets this to 'json' and is not changable.
        quarters_back (int): The number of business quarters to include in the response from today.
        rating_date (str): The date to pull ratings from. Formatted as YYYY-MM-DD.
        show_event_evidence (bool): Show only companies that have enhanced event evidence enabled.
        show_ipspace (bool): Show only companies with visible IP space.
        tier (list[str]): Filter by tier guids. See https://help.bitsighttech.com/hc/en-us/articles/360021083694-GET-Tiers
    """

    kwargs["format"] = "json"

    return call_api(
        key=key, module="portfolio", endpoint="portfolio_api_filters", params=kwargs
    ).json()


def portfolio_unique_identifiers(key: str) -> list:
    """
    Get a list of unique identifiers for companies and countries in your portfolio.

    Args:
        key (str): The API token to use for authentication.

    Returns:
        list: A list of unique identifiers.
    """

    return call_api(
        key=key, module="portfolio", endpoint="portfolio_unique_identifiers"
    ).json()


def get_portfolio_products(
    key: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get a list of products and product types in your portfolio.

    Args:
        key (str): The API token to use for authentication.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        fields (str): Include these comma-separated fields in the response. Example: "product_name,product_types"
        limit (int): The number of results to return. Defaults to 100.
        offset (int): The number of results to skip. Defaults to 0.
        q (str): Full text search on all fields.
        sort (str): Sort by field. Example: "product_name"

    Returns:
        list[dict]: JSON containing the API response.
    """

    return do_paginated_call(
        key=key,
        module="portfolio",
        endpoint="get_portfolio_products",
        page_count=page_count,
        **kwargs,
    )


def get_product_usage(
    key: str, guid: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get a list of companies using a specific product.

    Args:
        key (str): The API token to use for authentication.
        guid (str): The GUID of the product to get usage for. See https://help.bitsighttech.com/hc/en-us/articles/360011948334-GET-Products-of-a-Company
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        fields (str): Include these comma-separated fields in the response. Example: "company_name,company_guid"
        limit (int): The number of results to return. Defaults to 100.
        offset (int): The number of results to skip. Defaults to 0.
        q (str): Full text search on all fields.
        sort (str): Sort by field. Example: "company_name"

    Returns:
        list[dict]: JSON containing the API response.
    """

    kwargs["guid"] = guid

    return do_paginated_call(
        key=key,
        module="portfolio",
        endpoint="get_product_usage",
        page_count=page_count,
        **kwargs,
    )


def get_product_types(
    key: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get a list of companies using a specific product.

    Args:
        key (str): The API token to use for authentication.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        fields (str): Include these comma-separated fields in the response. Example: "company_name,company_guid"
        limit (int): The number of results to return. Defaults to 100.
        offset (int): The number of results to skip. Defaults to 0.
        q (str): Full text search on all fields.
        sort (str): Sort by field. Example: "company_name"

    Returns:
        list[dict]: JSON containing the API response.
    """

    return do_paginated_call(
        key=key,
        module="portfolio",
        endpoint="get_product_types",
        page_count=page_count,
        **kwargs,
    )


def get_service_providers(
    key: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get a list service providers in your account.

    Args:
        key (str): The API token to use for authentication.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        fields (str): Include these comma-separated fields in the response. Example: "company_name,company_guid"
        limit (int): The number of results to return. Defaults to 100.
        offset (int): The number of results to skip. Defaults to 0.
        q (str): Full text search on all fields.
        sort (str): Sort by field. Example: "company_name"

    Returns:
        list[dict]: JSON containing the API response.
    """

    return do_paginated_call(
        key=key,
        module="portfolio",
        endpoint="get_service_providers",
        page_count=page_count,
        **kwargs,
    )


def get_service_provider_dependents(
    key: str, guid: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get a list of companies dependent on a specific service provider.

    Args:
        key (str): The API token to use for authentication.
        guid (str): The guid of the service provider to get dependents for. See https://help.bitsighttech.com/hc/en-us/articles/360011817254-GET-Service-Providers-for-a-Specific-Domain
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        fields (str): Include these comma-separated fields in the response. Example: "company_name,company_guid"
        limit (int): The number of results to return. Defaults to 100.
        offset (int): The number of results to skip. Defaults to 0.
        q (str): Full text search on all fields.
        sort (str): Sort by field. Example: "company_name"

    Returns:
        list[dict]: JSON containing the API response.
    """

    kwargs["guid"] = guid

    return do_paginated_call(
        key=key,
        module="portfolio",
        endpoint="get_service_provider_dependents",
        page_count=page_count,
        **kwargs,
    )


def get_service_provider_products(
    key: str, guid: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get a list of companies using a specific product.

    Args:
        key (str): The API token to use for authentication.
        guid (str): the guid of the service provider to get products for. See https://help.bitsighttech.com/hc/en-us/articles/360011817254-GET-Service-Providers-for-a-Specific-Domain
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        relationship_type (Literal['bitsight', 'self' 'none']): Filter by relationship type.
        fields (str): Include these comma-separated fields in the response. Example: "company_name,company_guid"
        limit (int): The number of results to return. Defaults to 100.
        offset (int): The number of results to skip. Defaults to 0.
        q (str): Full text search on all fields.
        sort (str): Sort by field. Example: "company_name"

    Returns:
        list[dict]: JSON containing the API response.
    """

    kwargs["guid"] = guid

    return do_paginated_call(
        key=key,
        module="portfolio",
        endpoint="get_service_provider_products",
        page_count=page_count,
        **kwargs,
    )


def get_security_rating_company_details(key: str, **kwargs) -> list[dict]:
    """
    Get security rating details of the companies in your portfolio. Also includes the guids of the companies.

    Args:
        key (str): The API token to use for authentication.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        expand (Literal['rating_details']): Expand the response. MUST be set to: "rating_details"
        period (Literal['daily', 'monthly', 'latest']): Filter by period.
        start_date (str): Filter by start date. Formatted as YYYY-MM-DD.
        end_date (str): Filter by end date. Formatted as YYYY-MM-DD.

    Returns:
        list[dict]: JSON containing the API response.

    Raises:
        HTTPError: If the request fails, usually due to the expand kwarg asking for too much data.
    """

    return call_api(
        key=key,
        module="portfolio",
        endpoint="get_security_rating_company_details",
        params=kwargs,
    ).json()


def get_security_rating_country_details(key: str, **kwargs) -> list[dict]:
    """
    Get security rating details of the countries in your portfolio. Also includes the guids of the countries.

    Args:
        key (str): The API token to use for authentication.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        expand (Literal['rating_details']): Expand the response. MUST be set to: "rating_details"
        period (Literal['daily', 'monthly', 'latest']): Filter by period.
        start_date (str): Filter by start date. Formatted as YYYY-MM-DD.
        end_date (str): Filter by end date. Formatted as YYYY-MM-DD.

    Returns:
        list[dict]: JSON containing the API response.

    Raises:
        HTTPError: If the request fails, usually due to the expand kwarg asking for too much data.
    """

    return call_api(
        key=key,
        module="portfolio",
        endpoint="get_security_rating_country_details",
        params=kwargs,
    ).json()


def get_risk_vector_grades(
    key: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get risk vector grades for companies in your portfolio.

    Args:
        key (str): The API token to use for authentication.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        limit (int): The number of results to return. Defaults to 100.
        offset (int): The number of results to skip. Defaults to 0.
        company_guid (str): Filter by company GUID. See https://help.bitsighttech.com/hc/en-us/articles/360055740193-GET-Portfolio-Details
        folder (str): Filter by folder GUID. See https://help.bitsighttech.com/hc/en-us/articles/360020042473-GET-Folder-Details
        period (Literal['latest', 'monthly']): Filter by period. Monthly returns 1 year of monthly data.
        tier (str): Filter by tier guid. See https://help.bitsighttech.com/hc/en-us/articles/360021083694-GET-Tiers

    Returns:
        list[dict]: JSON containing the API response.
    """

    return do_paginated_call(
        key=key,
        module="portfolio",
        endpoint="get_risk_vector_grades",
        page_count=page_count,
        params=kwargs,
    )


def get_portfolio_statistics(key: str, **kwargs) -> dict:
    """
    Get high level statistics about your portfolio, including
    the distribution of companies across rating categories (advanced, basic, etc.),
    the highest, lowest, median security ratings, &
    risk vector averages.

    Args:
        key (str): The API token to use for authentication.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        folder (str): Filter by folder GUID. See https://help.bitsighttech.com/hc/en-us/articles/360020042473-GET-Folder-Details
        rating_date (str): The date to pull ratings from. Formatted as YYYY-MM-DD.
        tier (str): Filter by tier guid. See https://help.bitsighttech.com/hc/en-us/articles/360021083694-GET-Tiers
        types (Literal['ratings', 'risk_vector_averages']): Filter by type.

    Returns:
        dict: JSON containing the API response.
    """

    return call_api(
        key=key, module="portfolio", endpoint="get_portfolio_statistics", params=kwargs
    ).json()
