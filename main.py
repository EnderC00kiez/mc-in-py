import click
import requests
click.echo("Contacting McInPy servers...")
remotescript = requests.get("https://raw.githubusercontent.com/EnderC00kiez/mc-in-py/master/main.py")
with open("main.py", "r") as main:
    if remotescript.text == main.read():
        click.echo("You are on the lastest version.")
    else:
        click.echo("You are on an older version then the servers.")
        if input("Update to lastest version? Type Y to update and any other key to not.") == "Y" or "y":
            click.echo("Updating...")
            print(remotescript.text)
