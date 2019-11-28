import json


def get_boilerplate(event, context):
    body = "Hello, world from Boilerplate!"
    ret = {"boilerplate": body}
    headers = {}
    return {"statusCode": 200, "headers": headers, "body": json.dumps(ret)}
