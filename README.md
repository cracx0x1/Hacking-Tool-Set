# Hacking Tool Set 

### Overview :
The Hacking Tool Set is a folder that contains multiple repositories, which are a collection of cybersecurity tools designed for ethical penetration testing and educational purposes. These tools are built using pwntools and various Python libraries. One of the key tools in this set is an advanced SSH brute-forcing script that automates password discovery through a password list, leveraging the power of pwntools and paramiko for SSH interaction.

### How to Use :
#### <ins>  Prerequisites : </ins>
1. Ensure that Python 3.x is installed on your machine.
2. Install required dependencies:

     - pip3 install paramiko pwntools
  
#### <ins>   For Cloning : </ins>
Clone the repository to your local system:

       git clone https://github.com/yourusername/hacking-tool-set.git
       cd hacking-tool-set

#### <ins>   Usage : </ins>
1. For ssh-bruteforcing script
   Edit the script and modify the following parameters:
   > - host = "TARGET_IP_OR_HOSTNAME"  # Replace with the target IP or hostname
   > - username = "USERNAME"  # Replace with the target username
   > - password_file = "ssh-common-passwords.txt"  # Path to your password list
2. Run the script:
    -         python3 script_name.py
  
      # Work In progress

