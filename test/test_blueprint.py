import json

import boilerplate.handler as boilerplate_handler


class TestBlueprint:
    def test_get_boilerplate(self):
        response = boilerplate_handler.get_boilerplate({}, {})
        body = json.loads(response["body"])
        assert response["statusCode"] == 200
        assert body["boilerplate"] == "Hello, world from Boilerplate!"
