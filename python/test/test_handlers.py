import json

from aws_xray_sdk.core import xray_recorder

from hello_world.handlers import say_hello

xray_recorder.begin_segment("Test")


def test_say_hello():
    response = say_hello({}, None)
    body = json.loads(response["body"])
    assert response["statusCode"] == 200
    assert body["hello"] == "world!"
