import discord
from discord.gateway import DiscordWebSocket
import datetime
import json
import os
from rich.console import Console
from rich.align import Align
from rich.panel import Panel

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

start_time = datetime.datetime.now(datetime.timezone.utc)


welcome = Panel(Align.center(logo), title="RPCVR", style="blue")

##############################################################

original_identify = DiscordWebSocket.identify

async def identify_vr(self):
    payload = {
        "op": 2,
        "d": {
            "token": self.token,
            "capabilities": 16381,
            "properties": {
                "os": "VR",
                "browser": "Discord VR",
                "device": "Discord VR"
            },
            "compress": True,
            "large_threshold": 250
        }
    }

    await self.send_as_json(payload)

DiscordWebSocket.identify = identify_vr

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

        await self.change_presence(activity=activity, status=discord.Status.online)

##################################################################
        clear_console()
        user = Panel(Align.center(f"User : {self.user.display_name} | ID : {self.user.id}"),title=f"Welcome : {self.user}", style="blue")
        console.print(welcome, user)
               

client = RPC()
client.run(TOKEN)

