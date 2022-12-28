import requests
import sys

name = input('Kullanıcı Adı Giriniz :')
if(name == ''):
	print("Yanlış değer girdiniz, Tekrar deneyin")
	sys.exit(0)
	
yazi ='''

░██████╗░█████╗░░██████╗██╗░░░██╗░█████╗░██╗░░░░░  ░█████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░
██╔════╝██╔══██╗██╔════╝╚██╗░██╔╝██╔══██╗██║░░░░░  ██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗
╚█████╗░██║░░██║╚█████╗░░╚████╔╝░███████║██║░░░░░  ███████║██████╔╝███████║██╔████╔██║███████║
░╚═══██╗██║░░██║░╚═══██╗░░╚██╔╝░░██╔══██║██║░░░░░  ██╔══██║██╔══██╗██╔══██║██║╚██╔╝██║██╔══██║
██████╔╝╚█████╔╝██████╔╝░░░██║░░░██║░░██║███████╗  ██║░░██║██║░░██║██║░░██║██║░╚═╝░██║██║░░██║
╚═════╝░░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
'''
print(yazi)

#--------------------------------------------------
github = requests.get(f'https://github.com/{name}')
st_code = github.status_code

if (st_code == 200):
	print('Github    ✔'  "Bulundu",f'https://github.com/{name}')
else:
	print('Github    ✖' "Bulunamadı")

#--------------------------------------------------
gitlab = requests.get(f'https://gitlab.com/{name}')
st_code = gitlab.status_code

if(st_code == 200):
	print('Gitlab    ✔' "Bulundu", f'https://gitlab.com/{name}')
else:
	print('Gitlab    ✖' "Bulunmadı")

#--------------------------------------------------
dev = requests.get(f'https://dev.to/{name}')
st_code = dev.status_code

if(st_code == 200):
	print('Dev.to    ✔' "Bulundu" f'https://dev.to/{name}')
else:
	print('Dev.to    ✖' "Bulunmadı")

#--------------------------------------------------
attherate = '@'
medium = requests.get(f'https://medium.com/{attherate}{name}')
st_code = medium.status_code

if(st_code == 200):
	print('Medium    ✔' "Bulundu" ,f'https://medium.com/{attherate}{name}')
else:
	print('Medium    ✖' "Bulunamadı" )
 
#--------------------------------------------------
replit = requests.get(f'https://replit.com/@{name}/')
st_code = replit.status_code

if(st_code == 200):
	print('Replit    ✔' "Bulundu", f'https://replit.com/@{name}/')
else:
	print('Replit    ✖' "Bulunamadı")


#--------------------------------------------------
quora = requests.get(f'https://www.quora.com/profile/{name}')
st_code = quora.status_code

if(st_code == 200):
	print('Quora     ✔' "Bulundu" ,f'https://www.quora.com/profile/{name}')
else:
	print('Quora     ✖' "Bulunamadı")

#--------------------------------------------------

reddit = requests.get(f'https://www.reddit.com/user/{name}')
st_code = reddit.status_code

if(st_code == 200):
	print('Reddit    ✔' "Bulundu",f'https://www.reddit.com/user/{name}')
else:
	print('Reddit    ✖' "Bulunamadı")
 
#--------------------------------------------------
flickr = requests.get(f'https://www.flickr.com/people/{name}')
st_code = flickr.status_code

if(st_code == 200):
	print('Flickr    ✔' "Bulundu", f'https://www.flickr.com/people/{name}')
else:
	print('Flickr    ✖' "Bulunamadı" )

#--------------------------------------------------
pinterest = requests.get(f'https://in.pinterest.com/{name}/')
st_code = pinterest.status_code

if(st_code == 200):
	print('Pinterest ✔' "Bulundu", f'https://in.pinterest.com/{name}/')
else:
	print('Pinterest ✖' "Bulunamadı" )


instagram = requests.get(f'https://instagram.com/{name}/')
st_code = instagram.status_code

if(st_code == 200):
	print('Instagram ✔' "Bulundu", f'https://instagram.com/{name}/')
else:
	print('Instagram ✖' "Bulunamadı")


#--------------------------------------------------
facebook = requests.get(f'https://www.facebook.com/{name}/')
st_code = facebook.status_code

if(st_code == 200):
	print('Facebook  ✔' "Bulundu" ,f'https://www.facebook.com/{name}/')
else:
	print('Facebook  ✖' "Bulunamadı")

#--------------------------------------------------
youtube = requests.get(f'https://www.youtube.com/{name}/')
st_code = youtube.status_code

if(st_code == 200):
	print('Youtube  ✔' "Bulundu" ,f'https://www.youtube.com/{name}/')
else:
	print('Youtube  ✖' "Bulunamadı")
	
