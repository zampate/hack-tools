#coding: utf-8
from time import sleep
print('''

_/﹋\_
(҂`_´)
<,︻╦╤─ ҉ - - - - - - -           
_/﹋\_

▄▀█ █▀█ ▄▀█ █▀▀ █░░ ▄▀█ █▀█ █ █▄░█   █▄▀ █░█ █░░ █░░ ▄▀█ █▄░█ █ █▀▄▀█ █
█▀█ █▀▄ █▀█ █▄▄ █▄▄ █▀█ █▀▄ █ █░▀█   █░█ █▄█ █▄▄ █▄▄ █▀█ █░▀█ █ █░▀░█ █
                                  	
  
  ''')
import os
print("0-Anamenü'ye dön")
print("1-TC Kimlik Bulma Kullanımı")
print("2-Macchanger Kullanımı")
print("3-Kriptoloji Şifreleme Kullanımı")
print("4-Admin Panel Bulucu Kullanımı")
print("5-Şifre Oluşturucu Kullanımı")
print("6-Site Ip Bulma Kullanımı")
print("7-Kullanıcı Adını Sosyal Medyada Arama")
print("8-İletişim Adresim")
islem=input("Kullanımı Öğrenemek istediğiniz aracın numarasını yazınız=")

if islem == 1:
    print("------------------------------------------------------------------")
    print("Karşınıza gelen ekranda TC Kimlik numarasınının 9 Hanesini yazınız")
    print("------------------------------------------------------------------")
    sleep(4)
    os.system("clear")
    os.system("python tr/kullanım.py")
    
elif islem == 2:
    print("--------------------------------------")
    print("Karşınıza gelen ekranda işlemi seçiniz. \nAdaptörün mac adresini değişmek istiyorsanız wlan0 yazmanız yeterli olacaktır.Direkt kullandığınız cihazın mac adresinin değişmesini istiyorsanız eth0 yazıp değişimi sağlayabilirsiniz.")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sleep(4)
    os.system("clear")
    os.system("python tr/kullanım.py")
elif islem == 3:
    print("----------------------------------------------------------------------------------------------------------")
    print("Karşınıza gelen ekrada anahtar giriniz. Şifreleme yapmak için '1', çözümleme yapmak için'2' tuşuna basınız.")
    print("----------------------------------------------------------------------------------------------------------")
    sleep(4)
    os.system("clear")
    os.system("python tr/kullanım.py")
elif islem == 4:
    print("-----------------------------------------------------------------------------------")
    print("Karşınıza gelen ekranda admin panelini bulmak istediğiniz sitenin adresini yazınız.")
    print("-----------------------------------------------------------------------------------")
    sleep(4)
    os.system("clear")
    os.system("python tr/kullanım.py")
elif islem == 5:
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Karşınıza gelen ekranda oluşturacağınız şifrenin kaç karakterden oluşacağını belirtiniz.Karakter sayısı belli olduktan sonra kaç adet şifre oluşturulacağı belirtilir." )
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    sleep(4)
    os.system("clear")
    os.system("python tr/kullanım.py")
elif islem == 6:
    print("-------------------------------------------------------------------------------------------------")
    print("Karşınıza gelen ekranda hangi sitenin ip adresini bulmak istiyorsanız o sitenin adresini yazınız.")
    print("-------------------------------------------------------------------------------------------------")
    sleep(4)
    os.system("clear")
    os.system("python tr/kullanım.py")
elif islem==7:
    print("-----------------------------------------------------------------------")
    print("Aratmak istediğiniz kullanıcı adı yazınız ve aratma işlemini başlatınız")
    print("-----------------------------------------------------------------------")
    sleep(4)
    os.system("clear")
    os.system("python tr/kullanım.py")    

elif islem == 8:
    print("--------------------------------------------------------------------------------------------------------------------")
    print("01011001 01101111 01101011 01110011 01100001 00100000 01110110 01100001 01110010 00100000 01101101 11000100 10110001")
    print("--------------------------------------------------------------------------------------------------------------------")
    sleep(4)
    os.system("clear")
    os.system("python tr/kullanım.py")
elif islem == 0:
    os.system("clear")
    print('''
                                                                                                                                                                           
 _____                   _              _      _           _            _                   _                           
|___ /   ___  __ _ _ __ (_)_   _  ___  (_) ___(_)_ __   __| | ___    __| | ___  _ __  _   _| |_   _ _   _  ___  _ __    
  |_ \  / __|/ _` | '_ \| | | | |/ _ \ | |/ __| | '_ \ / _` |/ _ \  / _` |/ _ \| '_ \| | | | | | | | | | |/ _ \| '__|   
 ___) | \__ \ (_| | | | | | |_| |  __/ | | (__| | | | | (_| |  __/ | (_| | (_) | | | | |_| | | |_| | |_| | (_) | |_ _ _ 
|____/  |___/\__,_|_| |_|_|\__, |\___| |_|\___|_|_| |_|\__,_|\___|  \__,_|\___/|_| |_|\__,_|_|\__,_|\__, |\___/|_(_|_|_)
                           |___/                                                                    |___/            
                                                                                                                                                              
    ''')
    sleep(3)
    os.system("clear")
    os.system("python hacktools.py")
else:
    print("Hatalı Tuşlama yaptınız")
    sleep(3)
    os.system("clear")
    os.system("python tr/kullanım.py")
    