from requests import get, post
from itertools import cycle
from base64 import b64encode, b64decode
from random import choice, randint
from uuid import uuid4
from hashlib import sha1
from threading import Thread

print("Welcome to the Demon Changer Hack [Type 'help' for help] (Released on ...) -Rylixmods")

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

# print("Number of Accounts: "+str(len(generallist)))
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

1 = Easy Demon
2 = Normal Demon
3 = Hard Demon
4 = Insane Demon
5 = Extreme Demon

: """))
    try:
        if rate < 10:
            if rate <= 5:

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

                    try:
                        proxy = choice(proxylist)
                    except:
                        pass

                    try:
                        if proxy in oldproxies:
                            pass
                        else:
                            url = "http://www.boomlings.com/database/rateGJDemon21.php"
                            r = "gameVersion=20&binaryVersion=34&gdw=0&accountID=" +accountid+ "&gjp=" +gjp+ "&udid=69&uuid=" +userid+ "&levelID=" +levelid+ "&rating=" +str(rate)+ "&secret=Wmfp3879gc3&rs=JKBHd789od&chk=" +str(xor(sha1(f"{levelid}{rate}JKBHd789od{accountid}69{userid}ysg6pUrtjn0J".encode()).hexdigest(), "58281").decode())

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
                                    if counter in counter_counter:
                                        counter += 1
                                        pass
                                    else:
                                        counter_counter.append(counter)
                                        expired_accids.append(accountid)
                                        oldproxies.append(proxy)
                                        o += 1
                                        counter += 1
                                elif data == "-1":
                                    pass
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

                print("Demon-Rate got changed. Pleae consider waiting, until the Geometry Dash servers have refreshed.")
  
    
    except:
        continue