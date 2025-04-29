from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    if stored_logins[email] == hash_password(password_to_check):
        return True
    return False

def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "user@domain.com": "d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2",
    }
    
    print(login("example@gmail.com", stored_logins, "password"))
    print(login("example@gmail.com", stored_logins, "wrongpassword"))
    print(login("user@domain.com", stored_logins, "hello"))
    print(login("user@domain.com", stored_logins, "wrong"))

if __name__ == '__main__':
    main()
