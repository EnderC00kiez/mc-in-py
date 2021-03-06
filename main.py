import os
from time import sleep
try:
    import click
except:
    os.system("pip3 install click")
    import click
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests
click.echo("Contacting McInPy servers...")
servers = requests.get("https://raw.githubusercontent.com/EnderC00kiez/mc-in-py/master/main.py")
if str(servers) != "<Response [200]>":
    print("Server Error (Status Code " + str(servers) + ")")
elif str(servers) == "<Response [200]>":
    print("Servers contacted.")
def kill():
    exit()
def schedule(secs, run):
    sleep(secs)
    eval(run)

while True:
    eval(input(">>> "))
