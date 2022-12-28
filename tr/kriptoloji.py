import random
yazi ='''



██╗░░██╗██████╗░██╗██████╗░████████╗░█████╗░██╗░░░░░░█████╗░░░░░░██╗██╗
██║░██╔╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░██╔══██╗░░░░░██║██║
█████═╝░██████╔╝██║██████╔╝░░░██║░░░██║░░██║██║░░░░░██║░░██║░░░░░██║██║
██╔═██╗░██╔══██╗██║██╔═══╝░░░░██║░░░██║░░██║██║░░░░░██║░░██║██╗░░██║██║
██║░╚██╗██║░░██║██║██║░░░░░░░░██║░░░╚█████╔╝███████╗╚█████╔╝╚█████╔╝██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚══════╝░╚════╝░░╚════╝░╚═╝
'''
print(yazi)

def safetyLock():

	shuffleKey= input('Anahtar giriniz:')
	if (shuffleKey != '00000000000000000'):
		print ("Anahtar Çalışıyor...")
		callMenu(shuffleKey)
	else :
		print ("")

def	encrypt(shuffleKey):
	keyBase = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+'
	keyBaseArray = list(keyBase)
	codeKeyArray = keyBaseArray
	cumle= input("Hangi kelimeyi/metni şifrelemek istiyorsun : ")
	karakterdizisi = list(cumle)
	print (shuffleKey)
	for count1,elem in enumerate(karakterdizisi):
		shuffleKey = int(shuffleKey)
		shuffleKey += count1
		random.seed(shuffleKey)
		random.shuffle(codeKeyArray)
		for count2,elem2 in enumerate(keyBase):
			if elem == elem2:
				karakterdizisi[count1]=codeKeyArray[count2]
	string1 = ''.join(karakterdizisi)
	return string1

def decrypt(shuffleKey):
	keyBase = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+'
	keyBaseArray = list(keyBase)
	codeKeyArray = keyBaseArray
	cumle = input("Hangi kelimeyi/metnin şifresini çözmek istiyorsun  : ")
	karakterdizisi = list(cumle)
	for count1,elem in enumerate(karakterdizisi):
		shuffleKey = int(shuffleKey)
		shuffleKey += count1
		random.seed(shuffleKey)
		random.shuffle(codeKeyArray)
		for count2,elem2 in enumerate(codeKeyArray):
			if elem == elem2:
				keyBaseArray = list(keyBase)
				karakterdizisi[count1]=keyBaseArray[count2]
	string1 = ''.join(karakterdizisi)
	return string1

def callMenu(shuffleKey):
	choice = 0
	while (choice != '4'):
		choice = input("\n1.Sifreleme \n2.Cozumleme \n3.Cık \nSecimi gir : ")
		if choice == "1":
			answer = encrypt(shuffleKey)
			print ('Şifrelenmis hali : ' + '\033[1m\033[31m' + answer + '\033[0m')

		elif choice == "2":
			answer = decrypt(shuffleKey)
			print ('Çözümlenmis hali : ' + '\033[1m\033[31m' + answer + '\033[0m')
		
		elif choice == "3":
			exit()
		

		else:
			print("Seçim yapmadın, lütfen tekrar deneyin\n")

if __name__ == '__main__':
	try:
		safetyLock()
	except KeyboardInterrupt:
		print('\nÇıkılıyor...')