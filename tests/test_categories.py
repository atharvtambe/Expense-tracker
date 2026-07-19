def test_get_categories(test_client):

    login = test_client.post(
        "/login",
        data={
            "username": "harsh@gmail.com",
            "password": "harsh@123"
        }
    )

    token = login.json()["access_token"]

    response = test_client.get(
        "/categories",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200