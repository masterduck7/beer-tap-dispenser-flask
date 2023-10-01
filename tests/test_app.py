class TestApp:
    def test_index(app, client):
        response = client.get("/")
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "Hello world!"
