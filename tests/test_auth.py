def test_home(test_client):
    response = test_client.get("/")

    assert response.status_code == 200
    
import random

def test_register(test_client):

    email = f"user{random.randint(1,100000)}@gmail.com"

    response = test_client.post(
    "/register",
    json={
        "username": "harsh",
        "email": "raju@gmail.com",
        "password": "harsh@123",
        "phone_number": "9876543210"
    }
)

    assert response.status_code == 201
    
def test_login(test_client):

    response = test_client.post(
        "/login",
        data={
            "username":"pytest@gmail.com",
            "password":"12345678"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    
    