from requests import post, get
from random import randint, choice
from threading import Thread
from time import sleep
from uuid import uuid4

head = {
    'Accept-Encoding': None,
    'User-Agent': "",
    'Accept': '*/*',
    'Accept-Language': None,
    'Content-Length': '82',
    'Content-Type': 'application/x-www-form-urlencoded'
}
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
email = input()
email = email+"@outlook.de"
o = 0

proxylist = []
proxy_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true"
r = get(proxy_url)
for proxy in r.text.splitlines():
    proxylist.append(proxy)

def register(username, password, proxy):
    global o

    r = "userName="+username+"&password="+password+"&email="+email+"&secret=Wmfv3899gc9"
    try:
        data = post(url="http://www.boomlings.com/database/accounts/registerGJAccount.php", data=r, headers=head, proxies={"http": proxy}, timeout=3).content.decode()
        if data.startswith("-"):
            print(data)
            print(username)
            print(password)
            o += 1
        elif data == "1":
            print(data)
            print(username)
            print(password)
            o += 1
    except Exception as e:
        pass

username = "".join(choice(chars)for i in range(randint(10, 15)))
password = "".join(choice(chars)for i in range(randint(10, 15)))

while (True):
    proxy = choice(proxylist)
    t = Thread(target=register, args=(username, password, proxy))
    t.daemon = True
    t.start()
    if o >= 5:
        break

sleep(5)

o = 0

def login(proxy):
    global o
    uuid = str(uuid4())
    r = "udid="+uuid+"&userName="+username+"&password="+password+"&sID=76561199109727097&secret=Wmfv3899gc9"
    try:
        data = post(url="http://www.boomlings.com/database/accounts/loginGJAccount.php", data=r, headers=head, proxies= {"http": proxy}, timeout=3).content.decode()
        if data.startswith("2"):
            print(data)
            o += 1
            with open("gjps.txt", "a") as f:
                f.write("\n"+password)
            accountid = data.split(",")[0]
            with open("accountids.txt", "a") as f:
                f.write("\n"+accountid)
    except Exception as e:
        pass

while (True):
    proxy = choice(proxylist)
    t = Thread(target=login, args=(proxy,))
    t.daemon = True
    t.start()
    if o >= 1:
        break