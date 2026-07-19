def test_create_expense(test_client):

    login = test_client.post(
        "/login",
        data={
            "username":"harsh@gmail.com",
            "password":"harsh@123"
        }
    )

    token = login.json()["access_token"]

    headers = {
        "Authorization":f"Bearer {token}"
    }

    cat = test_client.post(
    "/categories",
    json={
        "name": "Food"
    },
    headers=headers
)

    category_id = cat.json()["id"]
    
    
    response = test_client.post(
        "/expenses",
        headers=headers,
        json={
            "title":"Pizza",
            "description":"Food",
            "amount":350,
            "date":"2026-07-18",
            "category_id":category_id
        }
    )
    assert response.status_code == 201