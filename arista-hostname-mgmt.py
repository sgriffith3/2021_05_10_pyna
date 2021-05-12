import sys
import telnetlib

def read_and_print(host, tn, string):
   print(str(host) + "> Reading until: \"" + string + "\"")
   o = tn.read_until(bytes(string, 'ascii'))
   print(o.decode("ascii"))

def run_and_print(host, tn, cmd, string):
   print(str(host) + "> Sending: \"" + cmd + "\\r\\n\"")
   tn.write(bytes(cmd, 'ascii') + b"\r\n")
   read_and_print(host, tn, string)
   

host = #inf_host
course = #coursecode
start = #num
end   = #num2

for i in range(start, end+1):
  # switch sw1 and sw2
  for j in range (1,3):
    port = int("2"+str(j)+str(i))
    hostname = course + "-" + str(i) + "-sw" + str(j)
    tn = telnetlib.Telnet(host, port)
    
    run_and_print(port, tn, "",                    "localhost login:")
    run_and_print(port, tn, "admin",               "localhost>")
    run_and_print(port, tn, "enable",              "localhost#")
    run_and_print(port, tn, "config t",            "localhost(config)#")
    run_and_print(port, tn, "hostname "+ hostname, hostname+"(config)#")
    run_and_print(port, tn, "username admin secret alta3", hostname+"(config)#")

    run_and_print(port, tn, "int M1",   hostname+"(config-if-Ma1)#")
    run_and_print(port, tn, "ip address dhcp", "ip address dhcp")
    run_and_print(port, tn, "dhcp client accept default-route", "dhcp client accept default-route")
    run_and_print(port, tn, "exit",     hostname+"(config)#")

    run_and_print(port, tn, "management ssh",   hostname+"(config-mgmt-ssh)#")
    run_and_print(port, tn, "idle-timeout 0",   "idle-timeout 0")
    run_and_print(port, tn, "no-shutdown",      "no-shutdown")
    run_and_print(port, tn, "authentication mode keybaord-interactice", "authentication mode keybaord-interactice")
    run_and_print(port, tn, "exit",             hostname+"(config)#")

    run_and_print(port, tn, "exit",             hostname+"#")
    run_and_print(port, tn, "write memory",     "write memory")
    run_and_print(port, tn, "exit",             hostname+" login:")
