from os import environ
from version import VERSION

class RackspaceClient():
    def __init__(self,api_header) -> None:
        self.api_header = api_header or environ.get("RACKSPACE_API_HEADER")
        self.auth_header = None

    def set_header(self):
        self.auth_header = {"X-Api-Signature": f"{self.api_header}","User-Agent":f"rackmailcli/{VERSION}","Accept":"application/json"}