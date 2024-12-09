# Hacking Tool Set

## Overview
The Hacking Tool Set is a folder containing multiple repositories of cybersecurity tools designed for ethical penetration testing and educational purposes. These tools leverage Python libraries like pwntools and paramiko to perform various tasks such as SSH brute-forcing and password hash cracking.

## Key Tools in the Set:
1. SHA-256 Password Cracker: A script to crack SHA-256 password hashes using a wordlist.
2. SSH Brute-Forcing Script: Automates the discovery of SSH passwords using a dictionary attack.
3. Brute Force Login Tester: A script to brute-force web login forms. It attempts multiple username-password combinations against a target URL and identifies valid credentials based on a predefined success message.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `pwntools`
  - `paramiko`
  - `requests`

Install the required libraries by running:

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

