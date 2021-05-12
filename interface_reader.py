#!/usr/bin/env python3

import netifaces

def get_ip(interface):
    return (netifaces.ifaddresses(interface)[netifaces.AF_INET])[0]['addr']


def get_mac(interface):
    return (netifaces.ifaddresses(interface)[netifaces.AF_LINK])[0]['addr']


def main():
    print(netifaces.interfaces())
    for i in netifaces.interfaces():
        print(f'\n****** details of interface - {i} {get_ip(i)} {get_mac(i)}******')
        try:
            #my_mac = get_mac(i)
            #print("MAC: " + my_mac)
            print(f'MAC: {get_mac(i)}') 
            print(f'IP: {get_ip(i)}') 
        except:         
            print('Could not collect adapter information') 


if __name__ == "__main__":
    main()
    #print(get_mac("docker0"))
