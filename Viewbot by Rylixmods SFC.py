from base64 import b64decode, b64encode
from requests import post, get
from random import choice, randint
from itertools import cycle
from hashlib import sha1
from time import sleep
from threading import Thread
from uuid import uuid4

print(
  "Welcome to the View-Bot for Geometry Dash. -Rylixmods SFC"
)


def xor(data, key):
  xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))
  return b64encode(xored.encode())


def unxor(xored, key):
  data = b64decode(xored.encode()).decode()
  unxored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))
  return unxored


head = {
  'Accept-Encoding': None,
  'User-Agent': "",
  'Accept': '*/*',
  'Accept-Language': None,
  'Content-Length': '82',
  'Content-Type': 'application/x-www-form-urlencoded'
}

gjpslist = [
"Y1pWRGFxTUZ5YWFCVnc="
]

accountidslist = [
"24470056"
  ]

useridslist = [
"218268726"
  ]

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