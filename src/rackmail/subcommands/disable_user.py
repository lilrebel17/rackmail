from ..client import RackspaceClient
from requests import put

def disable_user(args):
    rackspace_client = RackspaceClient()

    url = f"https://api.emailsrvr.com/v1/customers/{rackspace_client.customer_id}/domains/{args.domain}/rs/mailboxes/{args.email}"
    request = put(url,headers=RackspaceClient().auth_header,json={"enabled":False})

    if request.status_code == 200:
        print("Rackspace API returned 200, account was disabled.")
    else:
        print(request.text)
        print(f"Status Code: {request.status_code}")