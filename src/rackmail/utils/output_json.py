import json

def output_json(status:int,command:str,email:str,text:str):
    data = {
        "Command": command,
        "Email": email,
        "Status": status,
        "Result": "Success" if status == 200 else "Failure",
        "Text": text
    }

    return json.dumps(data)