#coding: utf-8
import subprocess
import random
yazi ='''


███╗░░░███╗░█████╗░░█████╗░░█████╗░██╗░░██╗░█████╗░███╗░░██╗░██████╗░███████╗██████╗░
████╗░████║██╔══██╗██╔══██╗██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝░██╔════╝██╔══██╗
██╔████╔██║███████║██║░░╚═╝██║░░╚═╝███████║███████║██╔██╗██║██║░░██╗░█████╗░░██████╔╝
██║╚██╔╝██║██╔══██║██║░░██╗██║░░██╗██╔══██║██╔══██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗
██║░╚═╝░██║██║░░██║╚█████╔╝╚█████╔╝██║░░██║██║░░██║██║░╚███║╚██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝
'''
print(yazi)

import sys

if ("--help" in sys.argv):
    print("""
    - 1'i secerseniz mac adresini yazin
    - 2'yi secerseniz rastgele mac adresi kullaniriz.
    - Linux'ta ifconfig yazarsiniz, Linux eth0 veya wlan0 mac adresi der.
    Ardindan, macchanger arayuzu ne tercih edersiniz der; Sen yaz.
    uyari!! : Wifi karti olmadan kali linux veya farkli bir linux uzerinde calisiyorsaniz,
    internet baglantiniz kaybolabilir.
    ornegin : eth0 agini kullaniyorsaniz internet baglantiniz kesilecektir. """)
    sys.exit()




while True:
    try:
        print("-------------------")
        print("Random Mac adress")
        print("-------------------")
        mac_address = 1
        
       
        
        
        

    except:
        print("PLEASE CHOOSE")
        continue
    else:
        break



print("-------------------")
print("eth0")
print("-------------------")
interface = 'eth0'
r1 = str(random.randint(0,10))
r2 = str(random.randint(0,10))



if mac_address == 1:
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether","00:"+r1+r2+":"+r1+r2+":"+r1+r2+":"+"aa:"+r1+r2])
    subprocess.call(["ifconfig",interface,"up"])
    print("MAC CHANGED")
    

   

else:
    print("You Didn't Make the Right Choice")

