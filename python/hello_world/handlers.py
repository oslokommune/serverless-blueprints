import json

from aws_xray_sdk.core import patch_all, xray_recorder
from okdata.aws.logging import log_add, logging_wrapper

patch_all()


@logging_wrapper
@xray_recorder.capture("say_hello")
def say_hello(event, context):
    log_add(relevant_information="Hello from Python blueprint!")

    return {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps({"hello": "world!"}),
    }
