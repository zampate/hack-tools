import socket as s
yazi ='''

░██████╗██╗████████╗███████╗  ██╗██████╗░  ██████╗░██╗░░░██╗██╗░░░░░███╗░░░███╗░█████╗░
██╔════╝██║╚══██╔══╝██╔════╝  ██║██╔══██╗  ██╔══██╗██║░░░██║██║░░░░░████╗░████║██╔══██╗
╚█████╗░██║░░░██║░░░█████╗░░  ██║██████╔╝  ██████╦╝██║░░░██║██║░░░░░██╔████╔██║███████║
░╚═══██╗██║░░░██║░░░██╔══╝░░  ██║██╔═══╝░  ██╔══██╗██║░░░██║██║░░░░░██║╚██╔╝██║██╔══██║
██████╔╝██║░░░██║░░░███████╗  ██║██║░░░░░  ██████╦╝╚██████╔╝███████╗██║░╚═╝░██║██║░░██║
╚═════╝░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝╚═╝░░░░░  ╚═════╝░░╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
'''
print(yazi)
website = input("Site Linki giriniz =")
ip = s.gethostbyname(website)
print("  Girdiginiz Sitenin ip Adresi : "+ip)