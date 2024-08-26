"""
cli.py - Command line functionality for bitsightpy.

Use this to quickly pull data from the Bitsight API from the command line.
"""

from argparse import ArgumentParser
from json import dumps, dump
from os import path

from bitsightpy.finding_details import get_finding_details
from bitsightpy.portfolio import get_details


def parse_kwargs(kwargs_list):
    kwargs = {}
    if kwargs_list:
        for item in kwargs_list:
            key, value = item.split("=")
            kwargs[key] = value
    return kwargs


def get_findings(args):
    """
    Get findings for a given company.
    """
    findings = get_finding_details(
        key=args.key,
        company_guid=args.company,
        page_count=int(args.page_count) if args.page_count != "all" else "all",
        **parse_kwargs(args.kwargs)
    )

    if args.output:
        with open(args.output, "w") as f:
            dump(findings, f, indent=2)
    else:
        print(dumps(findings, indent=2))


def get_portfolio(args):
    """
    Get your Bitsight portfolio.
    """
    portfolio = get_details(args.key)

    if args.output:
        with open(args.output, "w") as f:
            dump(portfolio, f, indent=2)
    else:
        print(dumps(portfolio, indent=2))


def main():
    """
    Main entry point for the CLI.
    """
    parser = ArgumentParser(description="Bitsight API CLI.")
    subparsers = parser.add_subparsers(dest="command")

    findings_parser = subparsers.add_parser(
        "findings", help="Get findings for a given company."
    )
    findings_parser.add_argument(
        "company", help="The company guid to get findings for."
    )
    findings_parser.add_argument(
        "--output",
        help="The file to write the findings to. If not provided, prints to stdout.",
    )
    findings_parser.add_argument(
        "--key",
        help="The Bitsight API key. If not provided, looks for the BITSIGHT_API_KEY environment variable.",
        required=True,
    )
    findings_parser.add_argument(
        "-pC",
        "--page_count",
        help="The number of pages to retrieve. Defaults to 'all'.",
        default="all",
    )
    findings_parser.add_argument(
        "-kW",
        "--kwargs",
        nargs="*",
        help="Additional keyword arguments to pass to the API call, formatted in key=value pairs.",
    )
    findings_parser.set_defaults(func=get_findings)

    portfolio_parser = subparsers.add_parser(
        "portfolio", help="Get your Bitsight portfolio."
    )
    portfolio_parser.add_argument(
        "--output",
        help="The file to write the portfolio to. If not provided, prints to stdout.",
    )
    portfolio_parser.add_argument(
        "--key",
        help="Your Bitsight API key.",
        required=True,
    )
    portfolio_parser.set_defaults(func=get_portfolio)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
