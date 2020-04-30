#!/usr/bin/python3
from sys import platform as plt
import service

if plt == 'linux2' or plt == 'linux':
    status = service.status()
    if status:
        print("Ok")
    else:
        print("Error")
