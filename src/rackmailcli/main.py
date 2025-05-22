import argparse
from version import VERSION

if __name__ == "__main__":
    main_parser = argparse.ArgumentParser(
        prog="rackmailcli",
        description="CLI to interact with Rackspace's Hosted Email API",
    )

    main_parser.add_argument("--version",action="version",version=f"{main_parser.prog} V.{VERSION}")
    main_parser.parse_args()