"""
calls.py - Stores the user-facing functions for interacting with the company finding details API.
"""

from typing import Literal, Union, Optional

from bitsightpy.base.call_api import call_api, do_paginated_call


def get_finding_details(
    key: str, company_guid: str, page_count: Union[int, "all"] = "all", **kwargs
) -> list[dict]:
    """
    Return an organization's finding details, including risk types that affect
    or will affect security ratings such as compromised systems, diligence (except
    domain squatting), and user behavior (file sharing).

    Args:
        key (str): The API token to use for authentication.
        company_guid (str): The guid of the entity to retrieve findings for.
        page_count (Union[int, 'all']): The number of pages to retrieve. Defaults to 'all'.
        **kwargs: Additional keyword arguments to pass to call_api.

    ## Kwargs:

        limit (int): The maximum number of findings to return per page. Defaults to 100.
        offset (int): The number of findings to skip before returning results. Defaults to 100.
        fields (str): The fields to return in the response. Defaults to all fields.
        sort (str): The field to sort by.
        q (str): A full text search query to filter findings by.
        risk_category (Literal['Compromised Systems', 'Diligence', 'User Behavior']): Filter by the risk category. Comma-separated string for multiple values.
        risk_vector (Literal['botnet_infections', 'spam_propagation', 'malware_servers', 'unsolicited_comm', 'potentially_exploited', 'spf', 'dkim', 'ssl_configurations', 'open_ports', 'application_security', 'patching_cadence', 'insecure_systems', 'server_software', 'desktop_software', 'mobile_software', 'dnssec', 'mobile_application_security', 'web_appsec', 'dmarc', 'file_sharing']): Filter by the risk vector. Comma-separated string for multiple values.
        affects_rating (bool): Whether to return findings that affect the security rating.
        affects_rating_details (Literal['AFFECTS_RATING', 'LIFETIME_EXPIRED']): The type of findings to return.
        assets_asset (Literal['Domain', 'IP Address']): Filter by the type of asset.
        assets_category (Literal['low', 'medium', 'high', 'critical', None]): Filter by the importance category of the asset.
        assets_combined_importance (str): Filter by multiple `assets_category` values as a comma-separated string. Ex. 'low,medium'.
        assets_hosted_by (str): Filter by a hosting provider guid.
        attributed_companies_guid (list[str]): Filter by attributed company guids.
        attributed_companies_name (list[str]): Filter by attributed company names.
        details_cvss_base_gte (int 0-10): Filter by CVSS base score greater than or equal to this value.
        details_cvss_base_lte (int 0-10): Filter by CVSS base score less than or equal to this value.
        details_grade (Literal['GOOD', 'FAIR', 'BAD', 'WARN', 'NEUTRAL', 'NA']): Filter by the grade of the finding. Incompatible with `grade_<lt/gt>` filters.
        details_grade_gt (Literal['NEUTRAL', 'BAD', 'WARN', 'FAIR', 'GOOD']): Filter by findings with a grade greater than this value. Incompatible with `grade` filter.
        details_grade_lt (Literal['NEUTRAL', 'BAD', 'WARN', 'FAIR', 'GOOD']): Filter by findings with a grade less than this value. Incompatible with `grade` filter.
        details_infection_family (str): Filter by the infection family as a comma-separated string.
        details_observed_ips_contains (str): Filter by observed IP address.
        details_vulnerabilities_severity (Literal['minor', 'moderate', 'material', 'severe']): Filter by the severity of the vulnerability.
        evidence_key (Literal['Domain', 'IP Address']): Filter by the type of evidence.
        expand (Literal['attributed_companies', 'remediation_history', 'assets.tag_details', 'tag_details']): Drill down to more details on a specific field. tag_details = finding tags. asset.tag_details = asset tags.
        remediation_assignments (str): Filter by the assignee of the remediation by the user guid. See `users.get_users` for more information.
        risk_vector_label (str): Filter by the risk vector label as a comma-separated string. See https://help.bitsighttech.com/hc/en-us/articles/360043082833-API-Fields-Risk-Types
        severity (float 1-10): Filter by the severity of the finding as a decimal.
        severity_gt (float 1-10): Filter by the severity of the finding greater than this value.
        severity_lt (float 1-10): Filter by the severity of the finding less than this value.
        severity_lte (float 1-10): Filter by the severity of the finding less than or equal to this value.
        severity_gte (float 1-10): Filter by the severity of the finding greater than or equal to this value.
        severity_category (Literal['Minor', 'Moderate', 'Material', 'Severe']): Filter by the severity category of the finding.
        tags_contains (str): Filter by tags as a comma-separated string.
        unsampled (bool): Whether to return unsampled findings.
        vulnerabilities (str): Filter by the CVE ID of the vulnerability as a comma-separated string.

        DATE FILTERS:
        first_seen (str): Filter by the first date the finding was seen. Format: YYYY-MM-DD. Incompatible with `first_seen_lt/gt/lte/gte` filters.
        first_seen_gt (str): Filter by the first date the finding was seen after this date. Format: YYYY-MM-DD. Incompatible with `first_seen` filter.
        first_seen_lt (str): Filter by the first date the finding was seen before this date. Format: YYYY-MM-DD. Incompatible with `first_seen` filter.
        first_seen_gte (str): Filter by the first date the finding was seen on or after this date. Format: YYYY-MM-DD. Incompatible with `first_seen` filter.
        first_seen_lte (str): Filter by the first date the finding was seen on or before this date. Format: YYYY-MM-DD. Incompatible with `first_seen` filter.
        last_remediation_status_date (str): Filter by the last date the finding was remediated. Format: YYYY-MM-DD. Incompatible with `last_remediation_status_date_lt/gt` filters.
        last_remediation_status_date_gt (str): Filter by the last date the finding was remediated after this date. Format: YYYY-MM-DD. Incompatible with `last_remediation_status_date` filter.
        last_remediation_status_date_lt (str): Filter by the last date the finding was remediated before this date. Format: YYYY-MM-DD. Incompatible with `last_remediation_status_date` filter.
        last_remediation_status_date_gte (str): Filter by the last date the finding was remediated on or after this date. Format: YYYY-MM-DD. Incompatible with `last_remediation_status_date` filter.
        last_remediation_status_date_lte (str): Filter by the last date the finding was remediated on or before this date. Format: YYYY-MM-DD. Incompatible with `last_remediation_status_date` filter.
        last_remediation_status_label (Literal['No Status', 'Open', 'To Do', 'Work In Progress', 'Resolved', 'Risk Accepted']): Filter by the last remediation status label.
        last_seen (str): Filter by the last date the finding was seen. Format: YYYY-MM-DD. Incompatible with `last_seen_lt/gt/lte/gte` filters.
        last_seen_gt (str): Filter by the last date the finding was seen after this date. Format: YYYY-MM-DD. Incompatible with `last_seen` filter.
        last_seen_lt (str): Filter by the last date the finding was seen before this date. Format: YYYY-MM-DD. Incompatible with `last_seen` filter.
        last_seen_gte (str): Filter by the last date the finding was seen on or after this date. Format: YYYY-MM-DD. Incompatible with `last_seen` filter.
        last_seen_lte (str): Filter by the last date the finding was seen on or before this date. Format: YYYY-MM-DD. Incompatible with `last_seen` filter.

    Returns:
        list[dict]: The findings for the specified company.
    """

    kwargs["guid"] = company_guid

    # This endpoint has a ton of param names with periods in them,
    # in all different places. The backend call_api function
    # will convert the ones where just the last underscore is
    # replaced with a period. The rest will be handled here.

    special_params = {
        "assets.combined_importance": "assets_combined_importance",
        "assets.hosted_by": "assets_hosted_by",
        "details.cvss_base_gte": "details_cvss_base_gte",
        "details.cvss_base_lte": "details_cvss_base_lte",
        "details.grade_gt": "details_grade_gt",
        "details.grade_lt": "details_grade_lt",
        "details.infection.family": "details_infection_family",
        "details.observed_ips_contains": "details_observed_ips_contains",
        "details.vulnerabilities.severity": "details_vulnerabilities_severity",
    }

    # Iterate over user-provided kwargs and replace the key names with the
    # version that Bitsight expects.
    for k, value in special_params.items():
        if value in kwargs.keys():
            kwargs[k] = kwargs.pop(value)

    return do_paginated_call(
        key=key,
        module="finding_details",
        endpoint="get_finding_details",
        page_count=page_count,
        **kwargs
    )
