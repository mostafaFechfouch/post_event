# -*- coding: utf-8 -*-

import unicodecsv as csv
from string import Template
import smtplib
from dotenv import load_dotenv
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

env_path="ENV/authentication.env"
load_dotenv(dotenv_path=env_path)

certifications_path = 'certifications/'
MY_ADDRESS = os.getenv('EMAIL') 
PASSWORD = os.getenv('PASSWORD') 
print(PASSWORD,MY_ADDRESS)

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def get_contacts(filename):
    with open(u'testing.csv','rb') as csvfile:
        reader = csv.reader(csvfile, encoding="utf-8") 
        seen = set()
        names=[]
        emails=[]
        for line in reader:
            if line[0] in seen: continue
            names.append(line[1].strip())
            emails.append(line[0].strip())
            seen.add(line[0])
        return names, emails

def main():
    message_template =read_template("message.txt")
    names,emails = get_contacts("testing.csv")
    print(names,emails)
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.ehlo()
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    for name, email in zip(names, emails):
        msg = MIMEMultipart()
        message = message_template.substitute(PERSON_NAME=name)
        print(name,email)
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']= name + " DEVFEST 2K21 EL BAYADH! Attendance Certificate"
        msg.attach(MIMEText(message, 'plain'))
        with open(certifications_path+"certificate_"+email.split("@")[0]+".pdf", "rb") as file:
            attach = MIMEApplication(file.read(),_subtype="pdf")
        attach.add_header('Content-Disposition','attachment',filename=str("certificate_"+email.split("@")[0]+".pdf"))
        msg.attach(attach)
        s.send_message(msg)
        print(name," email sent")
        del msg
    s.quit()

if __name__ == '__main__':
    main()