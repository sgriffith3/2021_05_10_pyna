#!/usr/bin/python3
import paramiko 
import os 
import getpass 


def move_it(ip, port, uname, myfile, yourfile):
    t = paramiko.Transport(ip, port) 

    t.connect(username=uname, password=getpass.getpass()) 

    sftp = paramiko.SFTPClient.from_transport(t)

    sftp.put(myfile, yourfile) 

    sftp.close()


if __name__ == "__main__":
    move_it("10.10.2.3", 22, "bender", "camel.yaml", "cameliscious")
    move_it("10.10.2.4", 22, "fry", "camel.yaml", "cameliscious")

