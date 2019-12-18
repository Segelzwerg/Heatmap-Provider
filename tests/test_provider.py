class TestMainApp:
    def test_create_session(self, client):
        assert client.get("/create-session").status_code == 200