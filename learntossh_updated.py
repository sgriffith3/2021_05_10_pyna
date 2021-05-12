#!/usr/bin/env python3

## std library imports on top
import os

## 3rd party imports below
import paramiko

## work assigned to a junior programming asset on our team
from jrprogrammer import cmdissue


def get_creds():
    ip = input("IP: ")
    user = input("Username: ")
    # return [ip, user]
    # return {"ip": ip, "user": user}
    return (ip, user)


def get_cmds() -> list:
    cmds = ["ls", "ps", "ls -a", "date"]
    my_cmds = []
    while True:
        print(f"Commands to Run: {my_cmds}")
        cmd = int(input("Which command would you like to run?\n1: {}\n2: {}\n3: {}\n4: {}\nPress 5 to exit\n".format(*cmds)))
        if cmd == 5:
            break
        my_cmds.append(cmds[cmd-1])
    return my_cmds

#    while True:
#        try:
#            cmd = input("What command would you like to run? Press Ctrl C to quit\n")
#            if cmd == "":
#                break
#            cmds.append(cmd)
#        except KeyboardInterrupt as err:
#            print(err)
#            break
#    return cmds

def main():
  ## create session object
  sshsession = paramiko.SSHClient()
  sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

  ## create SSH connection
  while True:
      try:
          creds = get_creds()
          host = creds[0]
          user = creds[1]
          sshsession.connect(hostname=host, username=user, pkey=mykey)
        
          #our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]
        
          our_commands = get_cmds()
          for x in our_commands:
            ## call our imported function and save the value returned
            resp = cmdissue(x, sshsession)
            ## if returned response is not null, print it out
            if resp != "":
              print(resp)
        
          ## end the SSH connection
          sshsession.close()
      except KeyboardInterrupt as err:
          print("Lunch time!!!")
          break


if __name__ == '__main__':
  main()

