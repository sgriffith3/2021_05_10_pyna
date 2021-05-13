#!/usr/bin/env python3
import os
import sqlite3

conn = sqlite3.connect("devices.db")

data = conn.execute("SELECT * from switches")
for row in data:
    print(row)
    ping = os.system(f"ping -c 1 {row[0]}")
    print(ping)

