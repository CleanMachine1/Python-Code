#!/usr/bin/python3
import os
import getpass

user = getpass.getuser()
if user == "root":
    print("Hello root")
else:
    print("Hello", user)

