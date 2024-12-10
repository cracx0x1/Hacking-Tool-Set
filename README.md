# Hacking Tool Set

## Overview
The Hacking Tool Set is a collection of cybersecurity tools designed for ethical penetration testing and educational purposes. These tools leverage Python libraries like requests, pwntools, and paramiko to perform a variety of tasks, including password hash cracking, SSH brute-forcing, and web login brute-forcing. This repository also includes an SQL injection-based password hash extraction tool.

## Key Tools in the Set
1. SHA-256 Password Cracker: A script to crack SHA-256 password hashes using a wordlist.
2. SSH Brute-Forcing Script: Automates the discovery of SSH passwords using a dictionary attack.
3. Brute Force Login Tester: A script to brute-force web login forms. It attempts multiple username-password combinations against a target URL and identifies valid credentials based on a predefined success message.
4. SQL Injection Password Hash Extractor: This tool performs SQL injection to extract password hashes from a vulnerable web application.

## Tool Usage
1. SHA-256 Password Cracker
   
   Usage:
   - Prepare a file containing hashed passwords (one hash per line).
   - Provide a wordlist for cracking attempts.

2. SSH Brute-Forcing Script
   
   Usage:
    - Update the script with the target SSH server address, port, and usernames.
    - Provide a dictionary file with potential passwords.

3. Brute Force Login Tester
   
   Usage:
    - Update the script with the target login URL.
    - Provide a list of usernames and a password dictionary.
   
4. SQL Injection Password Hash Extractor
   
   Usage:
   - Set up the target URL and needle (success message).
   - Charset: Customize the character set used for brute-forcing the password hash.
   - User ID: Input the user ID whose password hash you want to extract.
   
## Prerequisites

- Python 3.x
- Required Python libraries:
  - `pwntools`
  - `paramiko`
  - `requests`

Install the required libraries by running

```bash
pip3 install paramiko pwntools requests

````

## How to Clone
```bash
git clone https://github.com/carcx0x1/hacking-tool-set.git

````
```bash
cd hacking-tool-set
````
## Note
- Use these tools responsibly and only on systems you own or have explicit permission to test.
- The success of brute-forcing or cracking scripts depends heavily on the quality of your wordlist.
- The success of brute-forcing and cracking depends heavily on the quality and size of your wordlist.

## License

This project is provided under the MIT License. Use it ethically and at your own risk. Unauthorized use of these tools is illegal and unethical.

## Contributions

Feel free to contribute, report bugs, or suggest enhancements via GitHub Issues.

## Acknowledgements
- This project was developed for educational purposes. It demonstrates key techniques used in penetration testing and cybersecurity research.
- Ensure that you use these tools ethically and with permission from the relevant parties.
