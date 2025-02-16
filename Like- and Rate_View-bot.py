from base64 import b64decode, b64encode
from requests import post, get
from random import choice, randint
from itertools import cycle
from hashlib import sha1
from time import sleep
from threading import Thread
from uuid import uuid4

print("Welcome to Like- and Rate/View-bot [Type 'help' for help] (Released on ...) -Rylixmods")

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

print("Number of Accounts: "+str(len(generallist)))   
while (True):    
    command = input(">> ")
    command = command.lower()
    if command == "help":
        print("Type in 'start' to start the programm! That's pretty much it!")   
    if command == "start":
        likebot = input("""
                       
Type '1' for: Level Likebot
Type'2' for: Comment Likebot
Type '3' for: Account-Comment Likebot
Type '4' for: Star-Rate Bot
Type '5' for: View-Bot

Which one do you want: """)                              
        if likebot == "1":      
            try:
                levelid = int(input("Type in the Level-ID: "))
                r = "gameVersion=21&binaryVersion=35&gdw=0&type=0&str=" +str(levelid)+ "&diff=-&len=-&page=0&total=0&uncompleted=0&onlyCompleted=0&featured=0&original=0&twoPlayer=0&coins=0&epic=0&demonFilter=5&secret=Wmfd2893gb7"
                data_level = post(url="http://www.boomlings.com/database/getGJLevels21.php", data=r, headers=head).content.decode()
                if data_level == "-1":
                    print("This Level-ID doesn't exist.")
                    continue                
                data_level2 = data_level.split(":")
                username_level = data_level2[3]            
            
            except:
                print("Type in a real Level-ID.")
                continue   
            
            is_it = input(f"Level: {username_level} (PRESS ENTER): ")
            if is_it != "":
                continue
            
            else:               
                like = input("Which Like-Bot do you want? (Likebot = 1, Dislikebot = 0): ")
                if like == "1" or "0":

                    print()
                    print("Starting...")
                    print()                    
                    oldproxies = []
                    counter_counter = []
                    expired_udids = []
                    expired_accids = []
                    accountidslist = []
                    useridslist = []
                    gjpslist = []                
                    
                    with open("accountids.txt", "r") as f:
                        for i in f:
                            accountidslist.append(i)
                    with open("userids.txt", "r") as f:
                        for i in f:
                            useridslist.append(i)
                    with open("gjps.txt", "r") as f:
                        for i in f:
                            gjpslist.append(i)                                                                  
                    o = 0
                    
                    counter = 1
                    
                    def likebot(accountid, userid, gjp):
                        
                        global username_level
                        global oldproxies
                        global o
                        global counter
                        global like                    
                        
                        try:
                            proxy = choice(proxylist)
                        except:
                            pass                      
                        
                        try:
                            if proxy in oldproxies:
                                pass
                            else:
                                
                                type_ = "1"
                                rs = "".join(choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")for i in range(10))
                                salt = "ysg6pUrtjn0J"
                                special = "0"
                                itemid = str(levelid)                                
                                while (True):
                                    udid = str(uuid4())
                                    if udid in expired_udids:
                                        continue
                                    else:
                                        break                             
                                m = sha1(f"{special}{itemid}{like}{type_}{rs}{accountid}{udid}{userid}{salt}".encode()).hexdigest()
                                x = xor(m, "58281").decode()
                                r = "gameVersion=20&binaryVersion=34&gdw=0&accountID=" +accountid+ "&gjp=" +gjp+ "&udid=" +udid+ "&uuid=" +userid+ "&itemID=" +itemid+ "&like=" +like+ "&type=" +type_+ "&secret=Wmfd2893gb7&special=" +special+ "&rs=" +rs+ "&chk=" +x
                                
                                try:
                                    if o >= len(generallist)-1:
                                        pass
                                    else:
                                        data = post(url="http://www.boomlings.com/database/likeGJItem211.php", data=r, headers=head, proxies={'http': proxy}, timeout=6).content.decode()
                                    
                                    if proxy in oldproxies:
                                        pass
                                    elif accountid in expired_accids:
                                        pass
                                    elif data == "1":
                                        print(str(counter)+ " | Successfully sent like...")
                                        if counter in counter_counter:
                                            counter += 1
                                            pass
                                        else:
                                            counter_counter.append(counter)
                                            expired_accids.append(accountid)
                                            accountidslist.remove(accountid)
                                            expired_udids.append(udid)
                                            useridslist.remove(userid)
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
                        print("New Proxies gained.")
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
                                t = Thread(target=likebot, args=(accountid, userid, gjp))
                                t.daemon = True
                                t.start()                        
        
        
        
        if likebot == "2":           
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
            
            try:
                page = int(input("Which page is the comment: "))
            except:
                continue
            if page >= 0:
                try:
                    comment = int(input("Which comment should it be (newest comment by 0): "))
                except:
                    continue
                if comment < 20:
                    like = input("What Like-Bot do you want? (Likebot = 1, Dislikebot = 0): ")
                    if like == "0" or "1":
                        url2 = "http://www.boomlings.com/database/getGJComments21.php"
                        r2 = {'gameVersion': '21', 'binaryVersion': '35', 'gdw': '0', 'page': str(page), 'total': '0', 'secret': 'Wmfd2893gb7', 'mode': '0', 'levelID': levelid, 'count': '20'}
                        data2 = post(url=url2, data=r2, headers=head).content.decode()
                        try:
                            data2 = post(url=url2, data=r2, headers=head).content.decode()
                            data3 = data2.split("|")
                            like_comment = int(data3[comment].split("~")[5])
                            data3 = data3[comment].split("~")[-1]
                            try:
                                data3 = data3.split("#")[0]
                            except:
                                pass
                            
                            special = levelid
                            
                            data2 = post(url=url2, data=r2, headers=head).content.decode()
                            data3 = data2.split("|")
                            data3 = data3[comment].split(":")[0].split("~")[-1]
                            itemid = data3
                        
                        except Exception as e:
                            print("Type in a valid page or comment.")
                            continue
                        
                        print()
                        print("Starting...")
                        print()                       
                        oldproxies = []
                        expired_udids = []
                        counter_counter = []
                        accountidslist = []
                        expired_accids = []
                        gjpslist = []
                        useridslist = []
                        
                        with open("accountids.txt", "r") as f:
                            for i in f:
                                accountidslist.append(i)
                        with open("userids.txt", "r") as f:
                            for i in f:
                                useridslist.append(i)
                        with open("gjps.txt", "r") as f:
                            for i in f:
                                gjpslist.append(i)                       
                        o = 0
                        
                        counter = 1
                        
                        def likebot(accountid, userid, gjp):
                            
                            global o
                            global oldproxies
                            global page
                            global levelid
                            global like
                            global counter
                            global expired_accids
                            global special
                            global itemid
                            
                            try:
                                proxy = choice(proxylist)
                            except:
                                pass
                            
                            try:
                                if proxy in oldproxies:
                                    pass
                                else:
                                    
                                    type_ = "2"
                                    rs = "".join(choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")for i in range(10))
                                    while (True):
                                        udid = str(uuid4())
                                        if udid in expired_udids:
                                            continue
                                        else:
                                            break
                                    salt = "ysg6pUrtjn0J"
                                    url = "http://www.boomlings.com/database/likeGJItem211.php"
                                    m = sha1(f"{special}{itemid}{like}{type_}{rs}{accountid}{udid}{userid}{salt}".encode()).hexdigest()
                                    x = xor(m, "58281").decode()
                                    r = "gameVersion=20&binaryVersion=35&gdw=0&accountID=" +accountid+ "&gjp=" +gjp+ "&udid=" +udid+ "&uuid=" +userid+ "&itemID=" +itemid+ "&like=" +like+ "&type=" +type_+ "&secret=Wmfd2893gb7&special=" +special+ "&rs=" +rs+ "&chk=" +x
                                    
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
                                            print(str(counter)+ " | Successfully sent like...")
                                            if counter in counter_counter:
                                                counter += 1
                                                pass
                                            else:
                                                counter_counter.append(counter)
                                                expired_accids.append(accountid)
                                                accountidslist.remove(accountid)
                                                useridslist.remove(userid)
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
                                    t = Thread(target=likebot, args=(accountid, userid, gjp))
                                    t.daemon = True
                                    t.start()       
        
        if likebot == "3":
            username = input("Type in the Username: ")
            url = "http://www.boomlings.com/database/getGJUsers20.php"
            r = {'gameVersion': '21', 'binaryVersion': '35', 'gdw': '0', 'str': username, 'total': '0', 'page': '0', 'secret': 'Wmfd2893gb7'}
            try:
                data = post(url=url, data=r, headers=head).content.decode()
                if data == "-1":
                    print("Username doesn't exist.")
                    continue
                data = data.split(":")
                print()
                print("Account-ID: " +data[21])
                print("User-ID: " +data[3])
                print()
            except Exception as e:
                print(e)
                print("Something went wrong...")
                continue
            
            page = int(input("Which Page is your comment (newest comment is on page 0): "))
            if page >= 0:
                comment = int(input("Which comment should it be (newest comment by 0): "))
                if comment < 10:
                    like = input("What Like-Bot do you want? (Likebot = 1, Dislikebot = 0): ")
                    if like == "1" or "0":
                        url2 = "http://www.boomlings.com/database/getGJAccountComments20.php"
                        r2 = {'gameVersion': '21', 'binaryVersion': '35', 'gdw': '0', 'accountID': str(data[21]), 'page': str(page), 'total': '0', 'secret': 'Wmfd2893gb7'}
                        #gameVersion=21&binaryVersion=35&gdw=0&accountID=" +str(data[21])+ "&page=" +str(page)+ "&total=0&secret=Wmfd2893gb7
                        try:
                            data2 = post(url=url2, data=r2, headers=head).content.decode()
                            data2 = data2.split("|")
                            data2 = data2[comment].split("~")[-1]
                            try:
                                data2 = data2.split("#")
                            except:
                                pass
                            
                            special = data[21]
                            itemid = data2[0]
                        
                        except:
                            print("Type in a valid page or comment.")
                            continue
                        
                        print()
                        print("Starting...")
                        print()                       
                        
                        oldproxies = []
                        expired_udids = []
                        counter_counter = []
                        expired_accids = []
                        accountidslist = []
                        useridslist = []
                        gjpslist = []
                        
                        with open("accountids.txt", "r") as f:
                            for i in f:
                                accountidslist.append(i)
                        with open("userids.txt", "r") as f:
                            for i in f:
                                useridslist.append(i)
                        with open("gjps.txt", "r") as f:
                            for i in f:
                                gjpslist.append(i)                        
                        o = 0
                        
                        counter = 1
                        
                        def likebot(accountid, userid, gjp):
                            
                            global o
                            global proxylist
                            global counter
                            global proxylist
                            global expired_accids
                            global special
                            global itemid
                            global like                      
                            
                            try:
                                proxy = choice(proxylist)
                            except:
                                pass
                            
                            try:
                                if proxy in oldproxies:
                                    pass                              
                                else:
                                    
                                    type_ = "3"
                                    rs = "".join(choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")for i in range(10))
                                    while (True):
                                        udid = str(uuid4())
                                        if udid in expired_udids:
                                            continue
                                        else:
                                            break
                                    salt = "ysg6pUrtjn0J"
                                    url = "http://www.boomlings.com/database/likeGJItem211.php"
                                    m = sha1(f"{special}{itemid}{like}{type_}{rs}{accountid}{udid}{userid}{salt}".encode()).hexdigest()
                                    x = xor(m, "58281").decode()
                                    r = "gameVersion=20&binaryVersion=35&gdw=0&accountID=" +accountid+ "&gjp=" +gjp+ "&udid=" +udid+ "&uuid=" +userid+ "&itemID=" +itemid+ "&like=" +like+ "&type=" +type_+ "&secret=Wmfd2893gb7&special=" +special+ "&rs=" +rs+ "&chk=" +x
                                    
                                    try:
                                        if o >= len(generallist)-1:
                                            pass
                                        else:
                                            data = post(url=url, data=r, headers=head, proxies={'http': proxy}, timeout=10).content.decode()                                                                                
                                        if proxy in oldproxies:
                                            pass
                                        elif accountid in expired_accids:
                                            pass
                                        elif data == "1":
                                            print(str(counter)+ " | Successfully sent like...")
                                            if counter in counter_counter:
                                                counter += 1
                                                pass
                                            else:
                                                counter_counter.append(counter)
                                                expired_accids.append(accountid)
                                                accountidslist.remove(accountid)
                                                useridslist.remove(userid)
                                                expired_udids.append(udid)
                                                oldproxies.append(proxy)
                                                o += 1
                                                counter += 1
                                        elif data == "-1":
                                            expired_udids.append(udid)
                                            expired_accids.append(accountid)
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
                                    t = Thread(target=likebot, args=(accountid, userid, gjp))
                                    t.daemon = True
                                    t.start()
        


        if likebot == "4":
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
                                accountidslist.append(i)
                        with open("userids.txt", "r") as f:
                            for i in f:
                                useridslist.append(i)
                        with open("gjps.txt", "r") as f:
                            for i in f:
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
                                    while True:
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
                                            print(str(counter) + " | Successfully sent rate...")
                                            if counter in counter_counter:
                                                counter += 1
                                                pass
                                            else:
                                                counter_counter.append(counter)
                                                expired_accids.append(accountid)
                                                accountidslist.remove(accountid)
                                                useridslist.remove(userid)
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

        
        
        if likebot == "5":            
            gjpslist = ["Y1pWRGFxTUZ5YWFCVnc="]
            accountidslist = ["24470056"]
            useridslist = ["218268726"]

            while (True):
                version = 2
                print()
                levelid = input('Type in the Level-ID: ')
                views_counter = int(input('How many views: '))
                print()
                print("Starting...")
                print()
                proxylist = []
                oldproxies = []
                counter_counter = []
                expired_accids = []
                expired_udids = []
                    
                o = 0

                counter = 1

                def viewbot(accountid, userid, gjp):

                    global oldproxies
                    global o
                    global counter
                    global proxylist
                    global expired_accids
                    global expired_udids
                    global levelid

                    try:
                        proxy = choice(proxylist)


                        if proxy in oldproxies:
                            pass
                        else:

                            type_ = "1"
                            rs = "".join(
                            choice(
                                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
                            ) for i in range(10))
                            salt = "xI25fpAapCQg"
                            while (True):
                                udid = str(uuid4())
                                if udid in expired_udids:
                                    continue
                                else:
                                    break
                            url = "http://www.boomlings.com/database/downloadGJLevel22.php"
                            m = sha1(f"{levelid}1{rs}{accountid}{udid}{userid}{salt}".encode()
                                    ).hexdigest()
                            x = xor(m, "41274").decode()
                            r = "gameVersion=20&binaryVersion=35&gdw=0&accountID=" +accountid+ "&gjp=" +gjp+ "&udid=" +udid+ "&uuid=" +userid+ "&levelID=" +levelid+ "&inc=1&extras=0&secret=Wmfd2893gb7&rs=" + rs + "&chk=" + x

                            try:
                                data = post(url=url,
                                            data=r,
                                            headers=head, proxies={'http': proxy}, timeout=6).content.decode()     

                                if proxy in oldproxies:
                                    pass
                                else: 

                                    if data.startswith("1"):
                                        print(str(counter) + " | Successfully sent view...")
                                        if counter in counter_counter:
                                            counter += 1
                                            pass
                                        else:
                                            counter_counter.append(counter)
                                            counter += 1
                                    elif data == "-1":
                                        expired_udids.append(udid)
                                    else:
                                        pass
                            except TimeoutError:
                                oldproxies.append(proxy)
                            except Exception as e:
                                pass

                    except:
                        pass

                while (True):
                    print(version)
                    if views_counter+(views_counter/2) < counter:
                        break
                    proxylist = []
                    proxy_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true"
                    try:  
                        r = get(proxy_url)
                    except:
                        continue

                    for proxy in r.text.splitlines():
                        proxylist.append(proxy)
                        for i in range(2500):
                            randnum = randint(0, len(accountidslist)-1)
                            accountid = accountidslist[randnum]
                            userid = useridslist[randnum]
                            gjp = gjpslist[randnum]
                            t = Thread(target=viewbot, args=(accountid, userid, gjp))
                            t.daemon = True
                            t.start()