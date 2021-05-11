#!/usr/bin/env python3
import smtplib # make the smtplib module avail
import getpass # secret acceptance of password

def send_my_message(subj, txt):
    mypass = getpass.getpass("Enter your Password:")
    myaddress = input("Enter your mail.com address (ex. pythonstudent01@mail.com):")

    content = f"""From:{myaddress}\n
    Subject: {subj}\n\n{txt}"""
    mail = smtplib.SMTP('smtp.mail.com',587) # server info
    mail.ehlo() # vs mail.hello() # for handshaking-- seems like you can skip
    mail.starttls() # start an encrypted connection
    mail.login(myaddress, mypass) # log into your account

    # send from, send to, what to send
    mail.sendmail(myaddress, 'beardedsam@mail.com', content)
    mail.close() # end the connection


send_my_message("Is this really considered a subject?", "Nope, I don't think so")
# this calls your main function

