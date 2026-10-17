
def test_valid_login():
    username = "Meet"
    password = "Rajani08"
    
    if username and password:
        print("Login test: PASS - Credentials provided")
    else:
        print("Login test: FAIL")

def test_empty_login():
    username = ""
    password = ""
    
    if not username and not password:
        print("Empty login test: PASS - Empty fields detected")
    else:
        print("Empty login test: FAIL")

test_valid_login()
test_empty_login()
