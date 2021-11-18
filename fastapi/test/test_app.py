from aws_xray_sdk.core import xray_recorder

import app

xray_recorder.begin_segment("Test")


def test_read_root():
    response = app.read_root()
    assert response == {"hello": "world"}
