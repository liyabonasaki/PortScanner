#!/usr/bin/python3

import socket

print('''
 _                _             ____        _       _ _   
| |__   __ _  ___| | _____ _ __/ ___| _ __ | | ___ (_) |_ 
| '_ \ / _` |/ __| |/ / _ \ '__\___ \| '_ \| |/ _ \| | __|
| | | | (_| | (__|   <  __/ |   ___) | |_) | | (_) | | |_ 
|_| |_|\__,_|\___|_|\_\___|_|  |____/| .__/|_|\___/|_|\__|
                                     |_|

						contact me: hackersploit22@gmail.com
						version: 1.0
						Evil Port Scanner 

''')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Please enter the host you want to scann : ")
port = int(input("Please enter the port you want to scann : "))

def portscanner(port):
    if s.connect_ex((host , port)):
        print("The port is closed")
    else:
        print("The port is open")
    
portscanner(port)


            
        
