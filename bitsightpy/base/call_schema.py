"""
call_schema.py - Contains expected params/form data/headers/etc. for
each Bitsight API endpoint.
"""

from frozendict import frozendict

"""
Other than get_endpoints, dict is structred as follows:

dict[module][function] = {...}
"""

CALL_SCHEMA = frozendict(
    {
        "get_endpoints": {
            "get_endpoints": {
                "endpoint": "",
                "params": [],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
        },
        "users": {
            "get_users": {
                "endpoint": "ratings/v2/users",
                "params": [
                    "limit",
                    "offset",
                    "q",
                    "sort",
                    "email",
                    "email_q",
                    "formal_name_q",
                    "group_guid",
                    "guid",
                    "is_available_for_contact",
                    "is_company_api_token",
                    "roles_slug",
                    "status",
                ],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": True,
                "convert_unders_to_periods": ["roles_slug", "group_guid"],
            },
            "create_user": {
                "endpoint": "ratings/v2/users",
                "params": [],
                "post_data": [
                    "status",
                    "group",
                    "roles",
                    "friendly_name",
                    "is_company_api_token",
                    "is_available_for_contact",
                    "formal_name",
                    "email",
                    "features",
                    "value",
                ],
                "use_requests_json": True,
                "method": ["POST"],
                "pagination": False,
            },
            "get_user_details": {
                "endpoint": "ratings/v2/users/{guid}",
                "params": ["guid"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "edit_user": {
                "endpoint": "ratings/v2/users/{guid}",
                "params": ["guid"],
                "post_data": [
                    "group",
                    "roles",
                    "friendly_name",
                    "is_company_api_token",
                    "is_available_for_contact",
                    "formal_name",
                    "email",
                    "features",
                    "value",
                ],
                "use_requests_json": True,
                "method": ["PATCH"],
                "pagination": False,
            },
            "delete_user": {
                "endpoint": "ratings/v2/users/{guid}",
                "params": ["guid"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["DELETE"],
                "pagination": False,
            },
            "turn_on_2fa": {
                "endpoint": "ratings/v2/users/{guid}/require-mfa",
                "params": ["guid"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["POST"],
                "pagination": False,
            },
            "resend_activation": {
                "endpoint": "ratings/v2/users/{guid}/resend-activation-email",
                "params": ["guid"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["POST"],
                "pagination": False,
            },
            "reset_2fa": {
                "endpoint": "ratings/v2/users/{guid}/reset-mfa",
                "params": ["guid"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["POST"],
                "pagination": False,
            },
            "get_quota": {
                "endpoint": "v1/users/quota",
                "params": [],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_company_views": {
                "endpoint": "ratings/v1/users/{guid}/company-views",
                "params": ["limit", "guid", "days_back", "folder"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
        },
        "insights": {
            "get_insights": {
                "endpoint": "ratings/v1/insights",
                "params": ["company", "start", "end", "score_delta_lt"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_change_explanations": {
                "endpoint": "ratings/v1/insights/rating-changes",
                "params": [
                    "limit",
                    "offset",
                    "company",
                    "date_gte",
                    "date_lt",
                    "score_delta_gte",
                    "score_delta_lt",
                ],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": True,
            },
        },
        "portfolio": {
            "get_details": {
                "endpoint": "ratings/v2/portfolio",
                "params": [
                    "fields",
                    "format",
                    "limit",
                    "offset",
                    "q",
                    "sort",
                    "countries",
                    "exclude_subscription_type_slug",
                    "filter_group",
                    "risk_vectors_grade",
                    "risk_vectors_slug",
                    "software_category",
                    "software_name",
                    "folder",
                    "industry_name",
                    "industry_slug",
                    "infections",
                    "life_cycle_slug",
                    "open_ports",
                    "products",
                    "product_types",
                    "providers",
                    "rating",
                    "rating_gt",
                    "rating_gte",
                    "rating_lt",
                    "rating_lte",
                    "relationship_slug",
                    "security_incident_categories",
                    "subscriptions_type_slug",
                    "tier",
                    "type",
                    "vendor_action_plan",
                    "vulnerabilities",
                ],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": True,
                "convert_unders_to_periods": [
                    "exclude_subscription_type_slug",
                    "risk_vectors_grade",
                    "risk_vectors_slug",
                    "software_category",
                    "software_name",
                    "industry_name",
                    "industry_slug",
                    "life_cycle_slug",
                    "relationship_slug",
                    "subscriptions_type_slug",
                ],
            },
            "get_summary": {
                "endpoint": "ratings/v2/portfolio/summaries",
                "params": ["folder", "tier"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_public_disclosures": {
                "endpoint": "ratings/v1/portfolio/breaches",
                "params": [
                    "company",
                    "start",
                    "end",
                    "folder",
                    "severity",
                    "severity_gte",
                    "severity_gt",
                    "severity_lte",
                    "severity_lt",
                    "tier",
                ],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_contacts": {
                "endpoint": "ratings/v1/portfolio/contacts",
                "params": [],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "assign_contact": {
                "endpoint": "ratings/v1/portfolio/contacts",
                "params": [],
                "post_data": [
                    "company_guid",
                    "friendly_name",
                    "formal_name",
                    "email",
                    "phone_number",
                ],
                "use_requests_json": True,
                "method": ["POST"],
                "pagination": False,
            },
            "edit_contact": {
                "endpoint": "ratings/v1/portfolio/contacts/{guid}",
                "params": ["guid"],
                "post_data": [
                    "guid",
                    "company_guid",
                    "friendly_name",
                    "formal_name",
                    "email",
                    "phone_number",
                ],
                "use_requests_json": True,
                "method": ["PATCH"],
                "pagination": False,
            },
            "get_geographic_ipspace": {
                "endpoint": "ratings/v1/portfolio/countries",
                "params": [],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_custom_identifiers": {
                "endpoint": "ratings/v1/portfolio/entity-custom-ids",
                "params": [],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "customize_company_id": {
                "endpoint": "ratings/v1/portfolio/entity-custom-ids",
                "params": [],
                "post_data": ["guid", "name", "custom_id"],
                "use_requests_json": True,
                "method": ["POST"],
                "pagination": False,
            },
            "bulk_manage_ids": {
                "endpoint": "ratings/v1/portfolio/entity-custom-ids/bulk",
                "params": [],
                "post_data": ["add", "delete"],
                "use_requests_json": True,
                "method": ["POST"],
                "pagination": False,
            },
            "portfolio_api_filters": {
                "endpoint": "ratings/v1/portfolio/filters",
                "params": [
                    "exclude_alerts_only",
                    "fields",
                    "folder",
                    "format",
                    "quarters_back",
                    "rating_date",
                    "show_event_evidence",
                    "show_ips",
                    "tier",
                ],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "portfolio_unique_identifiers": {
                "endpoint": "ratings/v1/portfolio/guids",
                "params": [],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_portfolio_products": {
                "endpoint": "ratings/v1/portfolio/products",
                "params": ["fields", "limit", "offset", "q", "sort"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": True,
            },
            "get_product_usage": {
                "endpoint": "ratings/v1/portfolio/products/{guid}/companies",
                "params": ["fields", "limit", "offset", "q", "sort", "guid"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": True,
            },
            "get_product_types": {
                "endpoint": "ratings/v1/portfolio/product-types",
                "params": ["fields", "limit", "offset", "q", "sort"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": True,
            },
            "get_service_providers": {
                "endpoint": "ratings/v1/portfolio/providers",
                "params": ["fields", "limit", "offset", "q", "sort"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": True,
            },
            "get_service_provider_dependents": {
                "endpoint": "ratings/v1/portfolio/providers/{guid}/companies",
                "params": ["fields", "limit", "offset", "q", "sort", "guid"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": True,
            },
            "get_service_provider_products": {
                "endpoint": "ratings/v1/portfolio/providers/{guid}/products",
                "params": [
                    "fields",
                    "limit",
                    "offset",
                    "q",
                    "sort",
                    "guid",
                    "relationship_type",
                ],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": True,
            },
            "get_security_rating_company_details": {
                "endpoint": "ratings/v1/portfolio/ratings",
                "params": ["expand", "period", "start_date", "end_date"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_security_rating_country_details": {
                "endpoint": "ratings/v1/portfolio/ratings",
                "params": ["expand", "period", "start_date", "end_date"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_risk_vector_grades": {
                "endpoint": "ratings/v1/portfolio/risk-vectors/grades",
                "params": [
                    "limit",
                    "offset",
                    "company_guid",
                    "folder",
                    "period",
                    "tier",
                ],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": True,
                "convert_unders_to_periods": ["company_guid"],
            },
            "get_portfolio_statistics": {
                "endpoint": "ratings/v1/portfolio/statistics",
                "params": ["folder", "rating_date", "tier", "types"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
        },
        "folders": {
            "get_folders": {
                "endpoint": "ratings/v1/folders",
                "params": ["exclude_subscription_folders"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "create_folder": {
                "endpoint": "ratings/v1/folders",
                "params": [],
                "post_data": ["name", "description", "content_expiry_days"],
                "use_requests_json": True,
                "method": ["POST"],
                "pagination": False,
            },
            "delete_folder": {
                "endpoint": "ratings/v1/folders/{guid}",
                "params": ["guid"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["DELETE"],
                "pagination": False,
            },
            "edit_folder": {
                "endpoint": "ratings/v1/folders/{guid}",
                "params": ["guid"],
                "post_data": [  # Can be refactored at some point. See manage_shared_folder_perms for a framework.
                    "name",
                    "description",
                    "content_expiry_days",
                    "description",
                    "is_shared",
                    "shared_with_all_users",
                    "email",
                    "can_edit_folder_properties",
                    "can_edit_folder_contents",
                    "group_can_edit_contents",
                    "group_can_edit_properties",
                    "shared_options",
                ],
                "use_requests_json": True,
                "method": ["PATCH"],
                "pagination": False,
            },
            "manage_shared_folder_perms": {
                "endpoint": "ratings/v1/folders/{guid}",
                "params": ["guid"],
                "post_data": ["shared_options"],
                "use_requests_json": True,
                "method": ["PATCH"],
                "pagination": False,
            },
            "add_companies_to_folder": {
                "endpoint": "ratings/v1/folders/{guid}/companies",
                "params": ["guid"],
                "post_data": ["add_companies"],
                "use_requests_json": True,
                "method": ["PATCH"],
                "pagination": False,
            },
        },
        "companies": {
            "get_company_details": {
                "endpoint": "ratings/v1/companies/{guid}",
                "params": ["guid", "fields"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_findings_statistics": {
                "endpoint": "ratings/v1/companies/{guid}/findings/statistics",
                "params": ["guid", "fields", "expand"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_findings_summaries": {
                "endpoint": "ratings/v1/companies/{guid}/findings/summaries",
                "params": ["guid", "fields", "expand"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_country_details": {
                "endpoint": "ratings/v1/companies/{guid}",
                "params": ["guid"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_assets": {
                "endpoint": "ratings/v1/companies/{guid}/assets",
                "params": [
                    "guid",
                    "limit",
                    "offset",
                    "q",
                    "sort",
                    "asset",
                    "combined_override_importance",
                    "expand",
                    "findings_total_count",
                    "findings_total_count_lt",
                    "findings_total_count_lte",
                    "findings_total_count_gt",
                    "findings_total_count_gte",
                    "hosted_by_isnull",
                    "importance_categories",
                    "importance_overrides",
                    "ip_address",
                    "is_ip",
                    "origin_subsidiary_isnull",
                    "overrides_isnull",
                    "tags_contains",
                    "tags_isnull",
                    "countries",
                    "country_codes",
                    "hosted_by_guid",
                    "origin_subsidiary_guid",
                    "product_name-version",
                    "product_support",
                    "product_vendor",
                    "services",
                    "threat_evidence_certainty",
                    "threat_exposure_detection",
                    "threat_guid",
                    "threat_severity_level",
                ],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": True,
                "convert_unders_to_periods": [
                    "combined_override_importance",
                    "findings_total_count",
                    "findings_total_count_lt",
                    "findings_total_count_lte",
                    "findings_total_count_gt",
                    "findings_total_count_gte",
                    "hosted_by_guid",
                    "origin_subsidiary_guid",
                    "product_name-version",
                    "product_support",
                    "product_vendor",
                    "threat_evidence_certainty",
                    "threat_exposure_detection",
                    "threat_guid",
                    "threat_severity_level",
                ],
            },
            "get_asset_risk_matrix": {
                "endpoint": "ratings/v1/companies/{guid}/assets/statistics",
                "params": ["guid", "fields", "expand"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_ratings_tree": {
                "endpoint": "ratings/v1/companies/{guid}/company-tree",
                "params": ["guid"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
            "get_ips_by_country": {
                "endpoint": "ratings/v1/companies/{guid}/countries",
                "params": ["guid"],
                "post_data": {},
                "use_requests_json": False,
                "method": ["GET"],
                "pagination": False,
            },
        },
    }
)
