from ..client import RackspaceClient
from ..utils.generate_random_string import generate_random_string
from requests import put

def set_password(args):
    rackspace_client = RackspaceClient()

    if args.password:
        password = args.password
    else:
        password = generate_random_string()

    url = f"https://api.emailsrvr.com/v1/customers/{rackspace_client.customer_id}/domains/{args.domain}/rs/mailboxes/{args.email}"
    request = put(url,headers=RackspaceClient().auth_header,json={"password":password})

    if request.status_code == 200:
        print(f"Rackspace API returned 200, password for {args.email}{args.domain} changed to {password}")
    else:
        print(request.text)
        print(f"Status Code: {request.status_code}")