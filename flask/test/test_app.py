from aws_xray_sdk.core import xray_recorder

from app import HelloWorld

xray_recorder.begin_segment("Test")


def test_hello_world():
    response = HelloWorld().get()
    assert response == {"hello": "world"}
