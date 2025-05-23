import argparse
from version import VERSION


if __name__ == "__main__":
    main_parser = argparse.ArgumentParser(prog="rackmailcli",description="CLI to interact with Rackspace's Hosted Email API",)
    main_parser.add_argument("--version",action="version",version=f"{main_parser.prog} V.{VERSION}")

    # This is store two arguments, we can add this as a parent to sub parsers so they will use the --email and --domain arguments.
    global_command_parser = argparse.ArgumentParser(add_help=False)
    global_command_parser.add_argument("-e","--email",action="store",metavar="email",dest="email")
    global_command_parser.add_argument("-d","--domain",action="store",metavar="domain",dest="domain")

    subparsers = main_parser.add_subparsers(dest="command")
    
    main_parser.parse_args()