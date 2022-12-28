import random
yazi ='''

   _____                  _        _                   
  / ____|                | |      | |                  
 | |     _ __ _   _ _ __ | |_ ___ | | ___   __ _ _   _ 
 | |    | '__| | | | '_ \| __/ _ \| |/ _ \ / _` | | | |
 | |____| |  | |_| | |_) | || (_) | | (_) | (_| | |_| |
  \_____|_|   \__, | .__/ \__\___/|_|\___/ \__, |\__, |
               __/ | |                      __/ | __/ |
              |___/|_|                     |___/ |___/ 
'''
print(yazi)

def safetyLock():

	shuffleKey= input('Enter Key:')
	if (shuffleKey != '00000000000000000'):
		print ("Key Working...")
		callMenu(shuffleKey)
	else :
		print ("")

def	encrypt(shuffleKey):
	keyBase = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+'
	keyBaseArray = list(keyBase)
	codeKeyArray = keyBaseArray
	cumle= input("Which word/text do you want to encrypt : ")
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
	cumle = input("Which word/text do you want to encrypt:  ")
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
		choice = input("\n1.Encrypt \n2.Decrypt \n3.Exit \nEnter Selection : ")
		if choice == "1":
			answer = encrypt(shuffleKey)
			print ('Encrypted Version : ' + '\033[1m\033[31m' + answer + '\033[0m')

		elif choice == "2":
			answer = decrypt(shuffleKey)
			print ('Decryped : ' + '\033[1m\033[31m' + answer + '\033[0m')
		
		elif choice == "3":
			exit()
		
		

		else:
			print("you did not choose Please try again\n")

if __name__ == '__main__':
	try:
		safetyLock()
	except KeyboardInterrupt:
		print('\nExiting...')