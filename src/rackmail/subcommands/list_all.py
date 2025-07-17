from ..client import RackspaceClient
from ..utils.output_json import output_json
from requests import get

def search_mailboxes(args):
    rackspace_client = RackspaceClient()

    base_route = f"https://api.emailsrvr.com/v1/customers/{rackspace_client.customer_id}/domains/{args.domain}/rs/mailboxes?size=250"

    if args.fields:
        field_list = args.fields.split()
        print(field_list)
        if not isinstance(field_list,list):
            raise TypeError("Fields argument was not input correctly. Please make sure its a comma separated list.\n-f size,currentUsage,enabled,createdDate")
        else:
            url = f"{base_route}&fields={args.fields}"
    else:
        url = base_route

    print(url)

    request = get(url,headers=RackspaceClient().auth_header)

    print(
        output_json(
            request.status_code,
            args.command,
            f"{args.domain}",
            request.json() if request.status_code == 200 else request.text)
        )