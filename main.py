import discord
import datetime
import json
import os
from rich.console import Console
from rich.align import Align
from rich.panel import Panel

# This is a simple Discord Rich Presence client for VR
# I will add more features soon like VR platform support
# because this version only works with Meta RPC without platform

##################################### CONFIG ##############################

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)
    

logo = r"""
 /$$$$$$$  /$$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$$ 
| $$__  $$| $$__  $$ /$$__  $$| $$   | $$| $$__  $$
| $$  \ $$| $$  \ $$| $$  \__/| $$   | $$| $$  \ $$
| $$$$$$$/| $$$$$$$/| $$      |  $$ / $$/| $$$$$$$/
| $$__  $$| $$____/ | $$       \  $$ $$/ | $$__  $$
| $$  \ $$| $$      | $$    $$  \  $$$/  | $$  \ $$
| $$  | $$| $$      |  $$$$$$/   \  $/   | $$  | $$
|__/  |__/|__/       \______/     \_/    |__/  |__/

"""

config = load_config()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

TOKEN = config['token']

APPLICATION_ID = config['application_id']

NAME = config['rpcname']

DETAILS = config['details']

STATE = config['state']

LARGE_IMAGE = config['large_image']

console = Console()

start_time = datetime.datetime( 
            2001, 1, 1, 12, 0, 0,
            tzinfo=datetime.timezone.utc
        )

welcome = Panel(Align.center(logo), title="RPCVR", style="blue")

################################ RPC ##########################
class RPC(discord.Client):
    async def on_ready(self):
        activity = discord.Activity(
            application_id=APPLICATION_ID,
            type=discord.ActivityType.playing,
            name=NAME,
            details=DETAILS,
            timestamps=discord.ActivityTimestamps(start=start_time),
            platform = discord.ActivityPlatform.meta_quest,
            assets=discord.ActivityAssets(
                large_image=LARGE_IMAGE,
            )
        ) 

        await self.change_presence(activity=activity)
        
        clear_console()
        console.print(welcome)
        console.print(Align.center(f"| [bold green]USER: {self.user} , ID: {self.user.id}[/bold green] |"))
        

client = RPC()
client.run(TOKEN)

