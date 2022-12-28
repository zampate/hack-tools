import requests
import sys

name = input('Enter Username:')
if(name == ''):
	print("You entered the wrong value, try again")
	sys.exit(0)
	
yazi ='''

███████╗ ██████╗  ██████╗██╗ █████╗ ██╗         ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║         ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
███████╗██║   ██║██║     ██║███████║██║         ███████╗█████╗  ███████║██████╔╝██║     ███████║
╚════██║██║   ██║██║     ██║██╔══██║██║         ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
███████║╚██████╔╝╚██████╗██║██║  ██║███████╗    ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝                    
                                                                                                
'''
print(yazi)

#--------------------------------------------------
github = requests.get(f'https://github.com/{name}')
st_code = github.status_code

if (st_code == 200):
	print('Github    ✔'  "Found",f'https://github.com/{name}')
else:
	print('Github    ✖' "Not Found")

#--------------------------------------------------
gitlab = requests.get(f'https://gitlab.com/{name}')
st_code = gitlab.status_code

if(st_code == 200):
	print('Gitlab    ✔' "Found", f'https://gitlab.com/{name}')
else:
	print('Gitlab    ✖' "Not Found")

#--------------------------------------------------
dev = requests.get(f'https://dev.to/{name}')
st_code = dev.status_code

if(st_code == 200):
	print('Dev.to    ✔' "Found" f'https://dev.to/{name}')
else:
	print('Dev.to    ✖' "Not Found")

#--------------------------------------------------
attherate = '@'
medium = requests.get(f'https://medium.com/{attherate}{name}')
st_code = medium.status_code

if(st_code == 200):
	print('Medium    ✔' "Found" ,f'https://medium.com/{attherate}{name}')
else:
	print('Medium    ✖' "Not Found" )
 
#--------------------------------------------------
replit = requests.get(f'https://replit.com/@{name}/')
st_code = replit.status_code

if(st_code == 200):
	print('Replit    ✔' "Found", f'https://replit.com/@{name}/')
else:
	print('Replit    ✖' "Not Found")


#--------------------------------------------------
quora = requests.get(f'https://www.quora.com/profile/{name}')
st_code = quora.status_code

if(st_code == 200):
	print('Quora     ✔' "Found" ,f'https://www.quora.com/profile/{name}')
else:
	print('Quora     ✖' "Not Found")

#--------------------------------------------------

reddit = requests.get(f'https://www.reddit.com/user/{name}')
st_code = reddit.status_code

if(st_code == 200):
	print('Reddit    ✔' "Found",f'https://www.reddit.com/user/{name}')
else:
	print('Reddit    ✖' "Not Found")
 
#--------------------------------------------------
flickr = requests.get(f'https://www.flickr.com/people/{name}')
st_code = flickr.status_code

if(st_code == 200):
	print('Flickr    ✔' "Found", f'https://www.flickr.com/people/{name}')
else:
	print('Flickr    ✖' "Not Found" )

#--------------------------------------------------
pinterest = requests.get(f'https://in.pinterest.com/{name}/')
st_code = pinterest.status_code

if(st_code == 200):
	print('Pinterest ✔' "Found", f'https://in.pinterest.com/{name}/')
else:
	print('Pinterest ✖' "Not Found" )


instagram = requests.get(f'https://instagram.com/{name}/')
st_code = instagram.status_code

if(st_code == 200):
	print('Instagram ✔' "Found", f'https://instagram.com/{name}/')
else:
	print('Instagram ✖' "Not Found")


#--------------------------------------------------
facebook = requests.get(f'https://www.facebook.com/{name}/')
st_code = facebook.status_code

if(st_code == 200):
	print('Facebook  ✔' "Found" ,f'https://www.facebook.com/{name}/')
else:
	print('Facebook  ✖' "Not Found")

#--------------------------------------------------
youtube = requests.get(f'https://www.youtube.com/{name}/')
st_code = youtube.status_code

if(st_code == 200):
	print('Youtube  ✔' "Found" ,f'https://www.youtube.com/{name}/')
else:
	print('Youtube  ✖' "Not Found")
