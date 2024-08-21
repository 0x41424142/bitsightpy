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
        description (str): Change the description of the folder.
        content_expiry_days (int): In how many days the folder should expire.
        is_shared (bool): Whether the folder is shared.
        shared_with_all_users (bool): Whether the folder is shared with all users.
        email[X] (str): The email address to share the folder with, where X is a number (e.g., email1, email2).
        can_edit_folder_properties[X] (bool): Whether the user X can edit the folder properties, where X matches the email number (e.g., email1 is married to can_edit_folder_properties1).
        can_edit_folder_contents[X] (bool): Whether the user X can edit the folder contents, where X matches the email number (e.g., email1 is married to can_edit_folder_contents1).
        group_can_edit_contents (bool): Whether all users in your group can edit companies in the folder.
        group_can_edit_properties (bool): Whether all users in your group can edit the folder properties.

    Returns:
        int: 204 if successful.
    """

    """
    Final dict structure to send to the API:

    {
        "name": str,
        "content_expiry_days": int,
        "description": str,
        "shared_options" {
            "is_shared": bool,
            "shared_with_all_users": bool,
            "group_can_edit_contents": bool,
            "group_can_edit_properties": bool,
            "shared_with": [
                {
                    "email": str,
                    "can_edit_folder_properties": bool,
                    "can_edit_folder_contents": bool
                },
                ...
            ]
        }
    }
    """

    payload = {}

    # Add simple key-value pairs to the payload:
    for k in ["name", "description", "content_expiry_days"]:
        if kwargs.get(k):
            payload[k] = kwargs[k]

    # Construct the shared_options object:
    shared_options = {}

    for k in [
        "is_shared",
        "shared_with_all_users",
        "group_can_edit_contents",
        "group_can_edit_properties",
    ]:
        if k in kwargs:
            shared_options[k] = kwargs[k]

    # Construct the shared_with list if email is provided:
    shared_with = []

    # Find all the email1, email2, etc. keys and add them to shared_with:
    for k in kwargs:
        if "email" in k:
            shared_with.append(
                {
                    "email": kwargs[k],
                    "can_edit_folder_properties": (
                        kwargs.get(f"can_edit_folder_properties{k[-1]}")
                        if f"can_edit_folder_properties{k[-1]}" in kwargs
                        else kwargs.get("can_edit_folder_properties")
                    ),  # account for no number
                    "can_edit_folder_contents": (
                        kwargs.get(f"can_edit_folder_contents{k[-1]}")
                        if f"can_edit_folder_contents{k[-1]}" in kwargs
                        else kwargs.get("can_edit_folder_contents")
                    ),  # account for no number
                }
            )

    # Add shared_options to the payload
    if shared_options:
        payload["shared_options"] = shared_options

    # Add shared_with to shared_options if it has any keys
    if shared_with:
        payload["shared_options"]["shared_with"] = shared_with

    # Pluck the folder guid and place it in params so call_api() can format the URL
    params = {"guid": folder_guid}

    # And finally, make the API call
    return call_api(
        key=key,
        module="folders",
        endpoint="edit_folder",
        post_data=payload,
        params=params,
    ).status_code


def manage_shared_folder_perms(key: str, folder_guid: str, **kwargs) -> dict:
    """
    Manage user permissions for shared folders

    Args:
        key (str): Your BitSight API key.
        folder_guid (str): The unique identifier of the folder.
        **kwargs: The attributes to change.

    :Kwargs:
        is_shared (bool): Whether the folder is shared.
        group_can_edit_contents (bool): Whether all users in your group can edit companies in the folder.
        shared_with_all_users (bool): Whether the folder is shared with all users.
        email[X] (str): The email address to share the folder with, where X is a number (e.g., email1, email2).
        can_edit_folder_properties[X] (bool): Whether the user X can edit the folder properties, where X matches the email number (e.g., email1 is married to can_edit_folder_properties1).
        can_edit_folder_contents[X] (bool): Whether the user X can edit the folder contents, where X matches the email number (e.g., email1 is married to can_edit_folder_contents1).

    Returns:
        dict: The updated folder object's details.
    """

    """
    Like edit_folder above, this function constructs a payload to send to the API. The payload is constructed like this:

    {
        "shared_options" : {
            "is_shared" : bool,
            "group_can_edit_contents" : bool,
            "shared_with_all_users" : bool,
            "shared_with_users" : [
                {
                    "email" : str,
                    "can_edit_folder_properties" : bool,
                    "can_edit_folder_contents" : bool
                },
                ...
            ]
        }
    }
    """
    payload = {}

    # Construct the shared_options object:
    shared_options = {}

    for k in ["is_shared", "shared_with_all_users", "group_can_edit_contents"]:
        if k in kwargs:
            shared_options[k] = kwargs[k]

    # Construct the shared_with_users list if email[X] is provided:
    shared_with_users = []

    # Find all the email, email1, email2, etc. keys and add them to shared_with_users:
    for k in kwargs:
        if "email" in k:
            shared_with_users.append(
                {
                    "email": kwargs[k],
                    "can_edit_folder_properties": (
                        kwargs.get(f"can_edit_folder_properties{k[-1]}")
                        if f"can_edit_folder_properties{k[-1]}" in kwargs
                        else kwargs.get("can_edit_folder_properties")
                    ),  # account for no number
                    "can_edit_folder_contents": (
                        kwargs.get(f"can_edit_folder_contents{k[-1]}")
                        if f"can_edit_folder_contents{k[-1]}" in kwargs
                        else kwargs.get("can_edit_folder_contents")
                    ),  # account for no number
                }
            )

    # Add shared_options to the payload
    if shared_options:
        payload["shared_options"] = shared_options

    # Add shared_with_users to shared_options if it has any keys
    if shared_with_users:
        payload["shared_options"]["shared_with_users"] = shared_with_users

    # Pluck the folder guid and place it in params so call_api() can format the URL
    params = {"guid": folder_guid}

    # And finally, make the API call
    return call_api(
        key=key,
        module="folders",
        endpoint="manage_shared_folder_perms",
        post_data=payload,
        params=params,
    ).json()


def add_companies_to_folder(
    key: str, folder_guid: str, company_guids: list[str]
) -> dict:
    """
    Add companies to a folder.

    Args:
        key (str): Your BitSight API key.
        folder_guid (str): The unique identifier of the folder.
        company_guids (list[str]): A list of company guids to add to the folder.

    Returns:
        dict: A summary of actions taken.
    """

    payload = {"company_guids": company_guids}

    params = {"guid": folder_guid}

    # And finally, make the API call
    return call_api(
        key=key,
        module="folders",
        endpoint="add_companies_to_folder",
        post_data=payload,
        params=params,
    ).json()


def add_companies_to_folder(
    key: str, folder_guid: str, add_companies: Union[list[str], str]
) -> dict:
    """
    Add companies to a folder.

    Args:
        key (str): Your BitSight API key.
        folder_guid (str): The unique identifier of the folder. See get_folders() for a list of folders.
        add_companies (Union[list[str], str]): A list of company guids or a single company guid string to add to the folder. See portfolio.get_details() for a list of companies.

    Returns:
        dict: A summary of actions taken.
    """

    if isinstance(add_companies, str):
        add_companies = [add_companies]

    return call_api(
        key=key,
        module="folders",
        endpoint="add_companies_to_folder",
        post_data={"add_companies": add_companies},
        params={"guid": folder_guid},
    ).json()


def remove_companies_to_folder(
    key: str, folder_guid: str, remove_companies: Union[list[str], str]
) -> dict:
    """
    Remove companies from a folder.

    Args:
        key (str): Your BitSight API key.
        folder_guid (str): The unique identifier of the folder. See get_folders() for a list of folders.
        remove_companies (Union[list[str], str]): A list of company guids or a single company guid string to remove from the folder. See portfolio.get_details() for a list of companies.

    Returns:
        dict: A summary of actions taken.
    """

    if isinstance(remove_companies, str):
        remove_companies = [remove_companies]

    return call_api(
        key=key,
        module="folders",
        endpoint="remove_companies_from_folder",
        post_data={"remove_companies": remove_companies},
        params={"guid": folder_guid},
    ).json()


def get_findings_from_folder(
    key: str,
    folder_guid: str,
    _type: str = None,
    confidence: Literal["LOW", "HIGH"] = None,
) -> list[dict]:
    """
    Get risk findings for a folder.

    Args:
        key (str): Your BitSight API key.
        folder_guid (str): The unique identifier of the folder. See get_folders() for a list of folders.
        _type (str, optional): The type of finding. Defaults to None.
        confidence (Literal['LOW', 'HIGH'], optional): The confidence level of the finding. Defaults to None.

    Returns:
        list[dict]: A list of dictionaries containing finding information.
    """

    params = {"guid": folder_guid}

    if _type:
        params["type"] = _type

    if confidence:
        params["confidence"] = confidence

    return call_api(
        key=key, module="folders", endpoint="get_findings_from_folder", params=params
    ).json()


def get_ratings_graph_from_folder(key: str, folder_guid: str) -> dict:
    """
    Get ratings graph data for a folder.

    Args:
        key (str): Your BitSight API key.
        folder_guid (str): The unique identifier of the folder. See get_folders() for a list of folders.

    Returns:
        dict: A dictionary containing the ratings graph data.

    NOTE:
        ```x``` is the date when the median rating of companies in the folder were established, as displayed in the horizontal axis of the graph on the Bitsight webpage
        ```y``` is the median Bitsight rating of the companies in the folder, as displayed in the vertical axis of the graph on the Bitsight webpage.
    """

    return call_api(
        key=key,
        module="folders",
        endpoint="get_ratings_graph_from_folder",
        params={"guid": folder_guid},
    ).json()


def get_products_from_folder(
    key: str, folder_guid: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get service provider products that companies in a folder use.

    Args:
        key (str): Your BitSight API key.
        folder_guid (str): The unique identifier of the folder. See get_folders() for a list of folders.
        page_count (Union[int, 'all'], optional): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        fields (str): A comma-separated string of fields to include in the response. Defaults to all fields.
        limit (int): The number of products to return in a single response.
        offset (int): The number of products to skip.
        q (str): A full-text search query to filter products by.
        sort (str): The field to sort by.

    Returns:
        list[dict]: A list of dictionaries containing product information.
    """

    # Check that page_count is valid
    if page_count != "all" and type(page_count) != int and page_count < 1:
        raise ValueError(
            f"page_count must be a positive integer or 'all', not {type(page_count)}"
        )

    responses = []
    pulled = 0

    while True:
        kwargs["guid"] = str(folder_guid)  # account for call_api .pop-ing guid
        response = call_api(
            key=key,
            module="folders",
            endpoint="get_products_from_folder",
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


def get_product_types_from_folder(
    key: str, folder_guid: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Get a list of products that are used by all companies in a folder.

    Args:
        key (str): Your BitSight API key.
        folder_guid (str): The unique identifier of the folder. See get_folders() for a list of folders.
        page_count (Union[int, 'all'], optional): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        fields (str): A comma-separated string of fields to include in the response. Defaults to all fields.
        limit (int): The number of products to return in a single response.
        offset (int): The number of products to skip.
        q (str): A full-text search query to filter products by.
        sort (str): The field to sort by.

    Returns:
        list[dict]: A list of dictionaries containing product information.
    """

    # Check that page_count is valid
    if page_count != "all" and type(page_count) != int and page_count < 1:
        raise ValueError(
            f"page_count must be a positive integer or 'all', not {type(page_count)}"
        )

    responses = []
    pulled = 0

    while True:
        kwargs["guid"] = str(folder_guid)  # account for call_api .pop-ing guid
        response = call_api(
            key=key,
            module="folders",
            endpoint="get_product_types_from_folder",
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


def get_product_usage(
    key: str,
    folder_guid: str,
    product_guid: str,
    page_count: Union[int, "all"] = "all",
    **kwargs,
) -> list[dict]:
    """
    Get a list of third parties that use a particular product type.

    Args:
        key (str): Your BitSight API key.
        folder_guid (str): The unique identifier of the folder. See get_folders() for a list of folders.
        product_guid (str): The unique identifier of the product type. See companies.get_products() for a list of products.
        page_count (Union[int, 'all'], optional): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional optional keyword arguments to pass to the API.

    :Kwargs:
        fields (str): A comma-separated string of fields to include in the response. Defaults to all fields.
        limit (int): The number of products to return in a single response.
        offset (int): The number of products to skip.
        q (str): A full-text search query to filter products by.
        sort (str): The field to sort by.

    Returns:
        list[dict]: A list of dictionaries containing product information.
    """

    # Check that page_count is valid
    if page_count != "all" and type(page_count) != int and page_count < 1:
        raise ValueError(
            f"page_count must be a positive integer or 'all', not {type(page_count)}"
        )

    responses = []
    pulled = 0

    while True:
        kwargs["guid"] = str(folder_guid)  # account for call_api .pop-ing guid
        kwargs["product_guid"] = str(product_guid)
        response = call_api(
            key=key,
            module="folders",
            endpoint="get_product_usage",
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
