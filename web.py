import time
from datetime import datetime as dt
i=int(input("Intial Website Block time:  "))
j=int(input("Final Website Block time:  "))
sites=["www.youtube.com","www.facebook.com","facebook.com","youtube.com"]
hosts_place="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,i) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,j):
        print("Web Blocker Active")
        with open(hosts_place,"r+") as file:
            content=file.read()
            for site in sites:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
    else:
        print("Play Time")
        with open(hosts_place,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites):
                    file.write(line)
                file.truncate()
    time.sleep(3)
