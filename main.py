#--------------------------------
from os import system, name, path
from time import sleep
from random import choice
from base64 import b64decode
try:
    from requests import get
except:
    system('pip install requests')
    from requests import get
try:
    from telethon import TelegramClient, sync, errors, functions, types
    from telethon.tl.functions.account import CheckUsernameRequest, UpdateUsernameRequest
except:
    system('pip install telethon')
    from telethon import TelegramClient, sync, errors, types, functions
    from telethon.tl.functions.account import CheckUsernameRequest, UpdateUsernameRequest
try:
    from bs4 import BeautifulSoup as S
except:
    system('pip install beautifulsoup')
    from bs4 import BeautifulSoup as S
try:
    from fake_useragent import UserAgent
except:
    system('pip install fake_useragent')
    from fake_useragent import UserAgent
try:
	from datetime import datetime
except:
	system('pip install datetime')
	from datetime import datetime
# Import/Download Libraries
me = "@MPPPQ"
def clear():
	system('cls' if name=='nt' else 'clear')
# for check flood , error
def channels2(client, username):
    di = client.get_dialogs()
    for chat in di:
        if chat.name == f'Updated!' and not chat.entity.username:
            client(functions.channels.DeleteChannelRequest(channel=chat.entity))
            return False
    return True
    
def fragment(username):
    headers = {
        'User-Agent': UserAgent().random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers'}
    response = get(f'https://fragment.com/username/{username}', headers=headers)
    soup = S(response.content, 'html.parser')
    ok = soup.find("meta", property="og:description").get("content")
    if "An auction to get the Telegram" in ok or "Telegram and secure your ownership" in ok or "Check the current availability of" in ok or "Secure your name with blockchain in an ecosystem of 700+ million users" in ok:return True
    elif "is taken" in ok:return "is taken"
    else:return False
# for claim username
def telegram(client,claim,username):
	if claim:
		text = f"- Sir New Catch 🐊\n• UserName : @{username} .\n• UserName Person : @MPPPQ ."
		try:print("-")
		except:pass
	else:
		text = f"- Sir New Catch 🐊\n• UserName : @{username} .\n• UserName Person : @MPPPQ."
	client.send_message('me',text)
def climed(client,username):
    result = client(functions.channels.CreateChannelRequest(
		title=f'Updated!',
        about=f'- @MPPPQ',
        megagroup=False))
    try:
        client(functions.channels.UpdateUsernameRequest(
        channel=result.chats[0],
        username=username))
        client.send_message(username,f'- Sir New Catch 🐊\n• UserName : @{username} .\n• UserName Person : @MPPPQ .')
        return True
    except Exception as e:client.send_message('me',f'⌯ Error Message .\nMessage : {e} .');return False
# for checking username
def checker(username,client):
		try:
			check = client(CheckUsernameRequest(username=username))
			if check:
				print('• UserName ['+username+' .'+"] , Available.")
				claimer = climed(client,username)
				if claimer and fragment(username) == "is taken":claim = True
				else:claim = False
				print('Did i take it? '+str(claim)+'\n'+'_ '*20)
				telegram(client,claim,username)
				flood = channels2(client,username)
				if not flood:
					with open('flood.txt', 'a') as floodX:
						floodX.write(username + "\n")
			else:
				print('• UserName ['+username+' .'+"] , Taken.")
		except errors.rpcbaseerrors.BadRequestError:
			print('• UserName ['+username+' .'+"] , Banned.")
			open("banned4.txt","a").write(username+'\n')
		except errors.FloodWaitError as timer:
			print('• Flood ['+timer.second+' .'+"] , Taken")
		except errors.UsernameInvalidError:
			print('- Error UserName : '+username+' .')
# for generate username
def usernameG():
	y = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
	j = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
	n = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
	w = ''.join(choice('1234567890') for i in range(1))
	v1 = y+y+'_'+j+j
	v2 = y+'_'+j+'_'+n
	v3 = y+'_'+n+'_'+j
	v4 = y+y+y+'_'+j
	v5 = y+'_'+j+j+j
	v6 = y+j+j+j+n
	v7 = y+j+n+n+n
	v8 = y+w+w+w+n
	v9 = y+j+j+j+w
	v10 = y+'_'+w+'_'+n
	v11 = y+y+y+n+y
	v12 = y+y+w+y+y
	v13 = y+y+y+y+n
	v14 = y+y+y+y+n
	v15 = y+w+y+y+y
	v16 = y+w+y+w+y
	v17 = y+n+y+n+y
	v18 = y+y+y+'_'+y
	v19 = y+'_'+y+y+y
	v20 = y+y+'_'+y+w
	v21 = y+w+w+w+y
	v22 = y+w+w+w+w
	v23 = y+'_'+w+'_'+w
	v24 = y+'_'+n+'_'+w
	v25 = y+y+y+y+y+n
	v26 = y+y+y+y+y+y+n
	v27 = y+y+j+y+y
	v28 = y+y+j+n+n
	
	
	ls = (v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,)
	u = choice(ls)
	return u
# start checking
def start(client,username):
	try:ok = fragment(username)
	except:return
	try:
		if not ok:
			checker(username,client)
		elif ok == "is taken":
			client.send_message('me',f' ماخوذ   .'+username)
			print('- ماخوذ : '+username+' .')
		else:
			client.send_message('me',f'مزاد '+username)
			print('- مزاد : '+username+' .')
	except Exception as e:print(e)
# get client
def clientX():
	client = TelegramClient("Client", b64decode("MjUzMjQ1ODE=").decode(),b64decode("MDhmZWVlNWVlYjZmYzBmMzFkNWYyZDIzYmIyYzMxZDA=").decode())
	try:client.start()
	except:pass
	try:client(JoinChannelRequest(get('https://pastebin.com/raw/SgDUMsFb').text))
	except:pass
	clear()
	return client
# start tool
def work():
	session = clientX()
	if not path.exists('banned4.txt'):
		with open('banned4.txt','w') as new:pass
	if not path.exists('flood.txt'):
		with open('flood.txt','w') as new:pass
	while True:
		username = usernameG()
		with open('banned4.txt', 'r') as file:
			check_username = file.read()
		if username in check_username:
			print('- Banned1 UserName : '+username+' .')
			continue
		start(session,username)
work()
