from pwn import *
import sys
import hashlib

if len(sys.argv) != 2:
    print("Invalid arguments!")
    print(">> {} <sha256sum>".format(sys.argv[0]))
    sys.exit(1)

wanted_hash = sys.argv[1]
password_file = "rockyou.txt"
attempts = 0

try:
    with log.progress("Attempting to crack: {}!\n".format(wanted_hash)) as p:
        with open(password_file, "r", encoding='latin-1') as password_list:
            for password in password_list:
                password = password.strip("\n").encode('latin-1')  
                password_hash = hashlib.sha256(password).hexdigest()  
                p.status("[Attempt: {}] Trying: '{}' -> {}".format(attempts, password.decode('latin-1'), password_hash))
                if password_hash == wanted_hash:
                    p.success("Password found after {} attempts! '{}' hashes to '{}'.".format(
                        attempts, password.decode('latin-1'), password_hash))
                    sys.exit(0)
                attempts += 1
        p.failure("Password was not found in the provided wordlist.")
except FileNotFoundError:
    log.error("Password file '{}' not found. Please make sure it exists.".format(password_file))
    sys.exit(1)
except Exception as e:
    log.error("An error occurred: {}".format(str(e)))
    sys.exit(1)
