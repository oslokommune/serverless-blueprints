import blueprint.handler as blueprint_handler


class TestBlueprint:
    def test_get_blueprint(self):
        response = blueprint_handler.get_blueprint({}, {})
        assert response == "Hello, world from Blueprint!"
