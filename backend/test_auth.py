import requests

BASE_URL = "http://localhost:5000/api"

def test_auth():
    # 1. Test Signup
    signup_data = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "password123"
    }
    print(f"Testing signup for {signup_data['email']}...")
    res = requests.post(f"{BASE_URL}/signup", json=signup_data)
    if res.status_code == 201:
        print("Signup successful!")
    elif res.status_code == 400 and "already exists" in res.text:
        print("User already exists (expected if re-running).")
    else:
        print(f"Signup failed: {res.status_code} - {res.text}")

    # 2. Test Login
    login_data = {
        "email": "test@example.com",
        "password": "password123"
    }
    print(f"Testing login for {login_data['email']}...")
    res = requests.post(f"{BASE_URL}/login", json=login_data)
    if res.status_code == 200:
        print("Login successful!")
        print(f"User data: {res.json()}")
    else:
        print(f"Login failed: {res.status_code} - {res.text}")

    # 3. Test Invalid Login
    print("Testing invalid login...")
    res = requests.post(f"{BASE_URL}/login", json={"email": "test@example.com", "password": "wrongpassword"})
    if res.status_code == 401:
        print("Invalid login correctly rejected.")
    else:
        print(f"Invalid login test failed: {res.status_code}")

if __name__ == "__main__":
    try:
        test_auth()
    except Exception as e:
        print(f"Error during testing: {e}")
