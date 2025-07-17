from ..client import RackspaceClient
from ..utils.output_json import output_json
from requests import get

def search_mailboxes(args):
    rackspace_client = RackspaceClient()

    url = f"https://api.emailsrvr.com/v1/customers/{rackspace_client.customer_id}/domains/{args.domain}/rs/mailboxes?size=250"

    if args.fields:
        field_list = args.fields.split()
        if not isinstance(field_list,list):
            raise TypeError("Fields argument was not input correctly. Please make sure its a comma separated list.\n-f size,currentUsage,enabled,createdDate")
        else:
            url = url + f"&fields={args.fields}"

    if args.page:
        url = url + f"&offset={args.page}"

    request = get(url,headers=RackspaceClient().auth_header)

    print(
        output_json(
            request.status_code,
            args.command,
            f"{args.domain}",
            request.json() if request.status_code == 200 else request.text)
        )