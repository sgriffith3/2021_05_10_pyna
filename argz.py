#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Larnin argparse")
parser.add_argument("name", help="The name of your old neighbor")
parser.add_argument("dog_name", help="The name of name's dog")
parser.add_argument("--at-home", default="not sure", help="Use if name is at home")
parser.add_argument("-w", "--woac", metavar="WORK_ON_CAR", default=True, help="Set False if no car in shop")
parser.add_argument("-f", "--fedora", default=False, action="store_true", help="Use this flag if name is wearing a fedora")

args = parser.parse_args()

print(f"All provided args:\n{args}\n")
print(f"Name: {args.name}")
print(f"Dog Name: {args.dog_name}")
print(f"At Home: {args.at_home}")
print(f"Working on Car: {args.woac}")
print(f"Wearing a Fedora: {args.fedora}")
print(type(args.fedora))
if args.fedora == True:
    print("Awesome Hat!!!")
    
