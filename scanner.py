#!/usr/bin/env python3
import socket
import time
import threading
from datetime import datetime

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return port, result == 0
    except:
        return port, False

def scan_target(target):
    print(f"[{datetime.now()}] Scanning {target}...")
    open_ports = []
    
    for port in [21,22,23,80,443,3389,8080]:
        port_num, is_open = scan_port(target, port)
        if is_open:
            open_ports.append(port_num)
            print(f"  Port {port_num}: OPEN")
    
    with open("scan_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {target}: {open_ports}\n")
    
    print(f"Open ports: {open_ports}\n")

# Auto-scan every 60 seconds
target_ip = "scanme.nmap.org"  # Change to your target

while True:
    scan_target(target_ip)
    time.sleep(60)
