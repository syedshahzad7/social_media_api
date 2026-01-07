from app import schemas    
import pytest
from jose import jwt
from app.config import settings




def test_create_user(client):
    res = client.post(
        "/users/",
        json={"email": "test@example.com", "password": "strongpassword"}
    )
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "test@example.com"
    assert res.status_code == 201

def test_login_user(test_user, client):
    res = client.post(
        "/login",
        data={"username": test_user['email'], "password": test_user['password']}
    )
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('test@example.com', 'wrongpassword', 403),
    ('nonexistent@example.com', 'wrongpassword', 403), 
    ('wrongemail@gmail.com', 'strongpassword', 403),
    (None, 'strongpassword', 422),
    ('test@example.com', None, 422),
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post(
        "/login",
        data={"username": email, "password": password}
    )
    assert res.status_code == status_code
   