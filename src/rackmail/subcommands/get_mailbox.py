from ..client import RackspaceClient
from requests import get

def get_mailbox(args):
    rackspace_client = RackspaceClient()

    url = f"https://api.emailsrvr.com/v1/customers/{rackspace_client.customer_id}/domains/{args.domain}/rs/mailboxes/{args.email}"
    request = get(url,headers=RackspaceClient().auth_header)

    if request.status_code == 200:
        print(request.text)
    else:
        print(request.text)
        print(f"Status Code: {request.status_code}")