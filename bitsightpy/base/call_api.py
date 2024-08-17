"""
call_api.py - Contains the base-level call to the Bitsight API via requests.Request.
"""

from typing import Literal, Optional, Union
from urllib.parse import parse_qs

from requests import request, Response
from requests.exceptions import HTTPError

from .call_schema import CALL_SCHEMA


def call_api(
    key: str,
    module: str,
    endpoint: str = None,
    params: Optional[dict] = None,
    post_data: Optional[dict] = None,
    headers: Optional[dict] = None,
    override_method: Literal["GET", "POST", "PUT", "DELETE"] = None,
) -> Response:
    """
    Base-level function to call a Bitsight API endpoint.

    Args:
        key (str): The API token to use for authentication.
        module (str): The module to call. Must be a valid module in the schema.
        endpoint (str): The endpoint to call.
        params (Optional[dict], optional): URL parameters. Defaults to None.
        post_data (Optional[dict], optional): POST form data. Defaults to None.
        headers (Optional[dict], optional): Headers to include in the request. Defaults to None.
        method (Literal["GET", "POST", "PUT", "DELETE"]): Override the default method for the endpoint.

    Returns:
        Response: requests.Response object containing the API response.

    Raises:
        requests.exceptions.HTTPError: If the API call fails.
    """

    # Make sure module is a valid module in the schema
    if module not in CALL_SCHEMA.keys():
        raise ValueError(f"Invalid module: {module}")

    # Make sure endpoint is a valid endpoint in the schema
    if endpoint not in CALL_SCHEMA[module].keys():
        raise ValueError(
            f"Invalid endpoint for module {module}: {endpoint}. Acceptable endpoints are {CALL_SCHEMA[module].keys()}"
        )

    # Make sure override method is a valid method for the endpoint
    if override_method and override_method not in CALL_SCHEMA[endpoint]["method"]:
        raise ValueError(
            f"Invalid method for endpoint {endpoint}: {override_method}. Acceptable methods are {CALL_SCHEMA[module][endpoint]['method']}"
        )

    # Make sure any GET params are valid for the endpoint
    if params:
        for param in params.keys():
            if param not in CALL_SCHEMA[module][endpoint]["params"]:
                raise ValueError(
                    f"Invalid param for endpoint {endpoint}: {param}. Acceptable params are {CALL_SCHEMA[module][endpoint]['params']}"
                )

    # Make sure any POST data is valid for the endpoint
    if post_data:
        for data in post_data.keys():
            if data not in CALL_SCHEMA[module][endpoint]["post_data"]:
                raise ValueError(
                    f"Invalid post_data for endpoint {endpoint}: {data}. Acceptable post_data are {CALL_SCHEMA[module][endpoint]['post_data']}"
                )

    # Make sure post_data is a dict if it's not None
    if post_data and type(post_data) != dict:
        raise ValueError(f"post_data must be a dict, not {type(post_data)}")

    # Make sure params is a dict if it's not None
    if params and type(params) != dict:
        raise ValueError(f"params must be a dict, not {type(params)}")

    # Check if the endpoint uses request's json feature:
    use_requests_json = CALL_SCHEMA[module][endpoint][
        "use_requests_json"
    ]

    base_url = "https://api.bitsighttech.com/"
    auth_token = (key, "")
    url = base_url + CALL_SCHEMA[module][endpoint]["endpoint"]

    # Special case for endpoints that have dynamic URL structure, such as get_user_details with {guid}
    if "{guid}" in url:
        url = url.format(guid=params.pop("guid"))

    # Lastly, check if the endpoint requires us to format some parameters back to <param_name>.slug format
    # instead of <param_name>_slug format:
    if CALL_SCHEMA[module][endpoint].get("convert_unders_to_periods"):
        for param in CALL_SCHEMA[module][endpoint]["convert_unders_to_periods"]:
            if params.get(param):
                # Get last occurrence of the underscore and replace it with a period
                new_param_name = param.rsplit("_", 1)[0] + "." + param.rsplit("_", 1)[1]
                params[new_param_name] = params.pop(param)

    # Create the request object
    response = request(
        method=override_method or CALL_SCHEMA[module][endpoint]["method"][0],
        url=url,
        params=params,
        data=post_data if not use_requests_json else None,
        json=post_data if use_requests_json else None,
        headers=headers,
        auth=auth_token,
    )

    # Raise an exception if the request failed
    if response.status_code in range(400, 600):
        raise HTTPError(
            f"Request failed with status code {response.status_code}: {response.text}"
        )

    return response


def check_for_pagination(response: Response) -> Union[None, str]:
    """
    Check if the API response contains pagination information.

    Args:
        response (Response): The response object from the API call.

    Returns:
        Union[None, str]: The URL for the next page of results, if any.
    """
    data = response.json()
    next_url = data.get("links").get("next")
    if next_url:
        params = parse_qs(next_url.split("?")[1])
        return params

    return None
