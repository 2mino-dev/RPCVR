import discord
from discord.gateway import DiscordWebSocket
import asyncio
import datetime
import random
import json
import os
from rich.console import Console
from rich.align import Align
from rich.panel import Panel

##################################### CONFIG ##############################

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)
    
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

config = load_config()

TOKEN = config['config']['token']

APPLICATION_ID = config['config']['application_id']

NAME = config['rpc']['name']

DETAILS = config['rpc']['details']

LARGE_IMAGE = config['rpc']['large_image']

CURRENT_SIZE = config['party']['current_size']

MAX_SIZE = config['party']['max_size']

STATE = config['party']['state']

console = Console()

start_time = datetime.datetime.now(datetime.timezone.utc)

if config["party"]["enable"]:
    party = discord.ActivityParty(
        current_size=CURRENT_SIZE,
        max_size=MAX_SIZE
    )
else:
    party = None
    
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

welcome = Panel(Align.center(logo), title="RPCVR", style="blue")

##############################################################

original_identify = DiscordWebSocket.identify

async def vr(self):
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

DiscordWebSocket.identify = vr

################################ RPC ##########################
class RPC(discord.Client):

    async def on_ready(self):
        initial_activity = discord.Activity(
            type=discord.ActivityType.playing,
            application_id=APPLICATION_ID,
            name=NAME,
            details=DETAILS,
            state=STATE,
            party=party,
            timestamps=discord.ActivityTimestamps(start=start_time),
            platform = discord.ActivityPlatform.meta_quest,
            assets=discord.ActivityAssets(
                large_image=LARGE_IMAGE,
            )
        )   

        await self.change_presence(activity=initial_activity, status=discord.Status.online)

        clear_console()
        userinfo = Panel(Align.center(f"User : {self.user.display_name} | ID : {self.user.id}"),title=f"Welcome : {self.user}", style="blue")
        console.print(welcome, userinfo)

        self.loop.create_task(rpc_loop(self, initial_activity))

################################ loop ################################

NAME1 = config['loop1']['name']
DETAILS1 =  config['loop1']['details']
LARGE_IMAGE1 = config['loop1']['large_image']

NAME2 = config['loop2']['name']
DETAILS2 =  config['loop2']['details']
LARGE_IMAGE2 = config['loop2']['large_image']

async def rpc_loop(client, initial_activity):
    while True:
        if config["config"].get("loop", False):
            activities = [
                discord.Activity(
                    application_id=APPLICATION_ID,
                    type=discord.ActivityType.playing,
                    name=NAME1,
                    details=DETAILS1,
                    state=STATE,
                    party=party,
                    timestamps=discord.ActivityTimestamps(start=start_time),
                    platform=discord.ActivityPlatform.meta_quest,
                    assets=discord.ActivityAssets(large_image=LARGE_IMAGE1)
                ),
                discord.Activity(
                    application_id=APPLICATION_ID,
                    type=discord.ActivityType.playing,
                    name=NAME2,
                    details=DETAILS2,
                    state=STATE,
                    party=party,
                    timestamps=discord.ActivityTimestamps(start=start_time),
                    platform=discord.ActivityPlatform.meta_quest,
                    assets=discord.ActivityAssets(large_image=LARGE_IMAGE2)
                )
            ]
            activity = random.choice(activities)
        else:
            activity = initial_activity
        
        await client.change_presence(activity=activity, status=discord.Status.online)
        await asyncio.sleep(10)

               

client = RPC()
client.run(TOKEN)

