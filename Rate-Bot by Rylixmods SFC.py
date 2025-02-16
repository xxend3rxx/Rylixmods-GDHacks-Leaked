from requests import get, post
from itertools import cycle
from base64 import b64encode, b64decode
from random import choice, randint
from uuid import uuid4
from hashlib import sha1
from threading import Thread

print("Welcome to Ratebot [Type 'help' for help] (Released on ...) -Rylixmods")

def xor(data, key):
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
    return b64encode(xored.encode())

def unxor(xored, key):
    data = b64decode(xored.encode()).decode()
    unxored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
    return unxored

head = {
    'Accept-Encoding': "",
    'User-Agent': "",
    'Accept': '*/*',
    'Accept-Language': None,
    'Content-Length': '82',
    'Connection': None,
    'Content-Type': 'application/x-www-form-urlencoded'
}
generallist = []
with open("accountids.txt", "r") as f:
    for i in f:
        generallist.append(i)

print()
print("Number of Accounts: "+str(len(generallist)))
print()
while (True):
    try:
        url_level = "http://www.boomlings.com/database/getGJLevels21.php"
        levelid = input("Type in the Level-ID: ")
        r = "gameVersion=21&binaryVersion=35&gdw=0&type=0&str=" +levelid+ "&diff=-&len=-&page=0&total=0&uncompleted=0&onlyCompleted=0&featured=0&original=0&twoPlayer=0&coins=0&epic=0&demonFilter=5&secret=Wmfd2893gb7"
        data_level = post(url=url_level, data=r, headers=head).content.decode()
        if data_level == "-1":
            print("This Level-ID doesn't exist.")
            continue
        data_level2 = data_level.split(":")
        username = data_level2[3]

    except Exception as e:
        print(e)
        print("Type in a real Level-ID.")
        continue

    is_it = input(f"Level: {username} (Press ENTER): ")
    if is_it != "":
        continue

    rate = int(input("""Which Star-Rate do you want?:

1 = easy
2 = normal
3 = hard
4 = harder
5 = insane

: """))
    try:
        if rate < 10:
            if rate <= 5:
                if rate == 1:
                    rate_x = "2"

                if rate == 2:
                    rate_x = "3"

                if rate == 3:
                    rate_x = "4"

                if rate == 4:
                    rate_x = "7"

                if rate == 5:
                    rate_x = "9"

                print()
                print("Starting...")
                print()

                oldproxies = []
                expired_accids = []
                expired_udids = []
                counter_counter = []
                expired_accids = []
                accountidslist = []
                useridslist = []
                gjpslist = []

                with open("accountids.txt", "r") as f:
                    for i in f:
                        i = i.replace("\n", "")
                        accountidslist.append(i)
                with open("userids.txt", "r") as f:
                    for i in f:
                        i = i.replace("\n", "")
                        useridslist.append(i)
                with open("gjps.txt", "r") as f:
                    for i in f:
                        i = i.replace("\n", "")
                        gjpslist.append(i)

                o = 0
                
                counter = 1

                def ratebot(accountid, userid, gjp):
                    
                    global o
                    global proxylist
                    global counter
                    global expired_accids
                    global levelid
                    global rate_x

                    try:
                        proxy = choice(proxylist)
                    except:
                        pass

                    try:
                        if proxy in oldproxies:
                            pass
                        else:
                            
                            type_ = "2"
                            rs = "".join("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"for i in range(10))
                            while (True):
                                udid = str(uuid4())
                                if udid in expired_udids:
                                    continue
                                else:
                                    break
                            salt = "ysg6pUrtjn0J"
                            url = "http://www.boomlings.com/database/rateGJStars211.php"
                            m = sha1(f"{levelid}{rate_x}{rs}{accountid}{udid}{userid}{salt}".encode()).hexdigest()
                            x = xor(m, "58281").decode()
                            r = "gameVersion=20&binaryVersion=34&gdw=0&accountID=" +accountid+ "&gjp=" +gjp+ "&udid=" +udid+ "&uuid=" +userid+ "&levelID=" +levelid+ "&stars=" +rate_x+ "&secret=Wmfd2893gb7&rs=" +rs+ "&chk=" +x

                            try:
                                if o >= len(generallist)-1:
                                    pass
                                else:
                                    data = post(url=url, data=r, headers=head, proxies={'http': proxy}, timeout=6).content.decode()

                                if proxy in oldproxies:
                                    pass
                                elif accountid in expired_accids:
                                    pass
                                elif data == "1":
                                    print(str(counter)+ " | Successfully sent rate...")
                                    if counter in counter_counter:
                                        counter += 1
                                        pass
                                    else:
                                        counter_counter.append(counter)
                                        expired_accids.append(accountid)
                                        expired_udids.append(udid)
                                        oldproxies.append(proxy)
                                        o += 1
                                        counter += 1
                                elif data == "-1":
                                    expired_udids.append(udid)
                                else:
                                    pass
                            except Exception as e:
                                pass
                    except:
                        pass

                while (True):
                    if o >= len(generallist)-1:
                        o = 0
                        break
                    proxylist = []
                    proxy_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true"
                    r = get(proxy_url)
                    for proxy in r.text.splitlines():
                        proxylist.append(proxy)
                    for i in range(2000):
                        if o >= len(generallist)-1:
                            break
                        else:
                            randnum = randint(0, len(accountidslist)-1)
                            accountid = accountidslist[randnum]
                            if accountid in expired_accids:
                                continue
                            userid = useridslist[randnum]
                            gjp = gjpslist[randnum]
                            t = Thread(target=ratebot, args=(accountid, userid, gjp))
                            t.daemon = True
                            t.start()


    except:
        continue