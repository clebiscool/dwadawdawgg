from os import name
from typing import Any, Coroutine, Optional
from datetime import datetime
from discord.interactions import Interaction
import requests
import discord 
import json
from discord import utils, app_commands
from discord.ext import commands
from colorama import init, Fore
import asyncio
from configparser import ConfigParser

# -- Setup --
init(autoreset=True) #  -- Colorama color reset --

config = ConfigParser() #  -- Config Parser used to parse whole config --
with open("config.json") as f: 
    config = json.load(f) # Load Config

token = config["discord_token"] #  -- Token --

intents = discord.Intents.all()

client = commands.Bot(command_prefix=".", intents=intents, case_insensitive=True, self_client=True)

# -- Commands --


# -- Commands --
@client.tree.command(name="drop", description="Drops Nitro URL from file to user.")
@commands.has_permissions(administrator=True)
async def drop(interaction: discord.Interaction, user: discord.Member, amount: int, type: int):
    
    if interaction.guild is None:
        return await interaction.response.send_message("You can't use this command in DMs.", ephemeral=True)
    else:
        if type == 1:
            file = "nitro.txt"
        elif type == 2:
            file = "nitrobc.txt"
        else:
            return await interaction.response.send_message("Invalid type.", ephemeral=True)

        try:

            with open(file, "r") as f:
                nitros = f.readlines()

            if amount > len(nitros):
                return await interaction.response.send_message("Not enough Nitro URLs available.", ephemeral=True)

            nitro = ""  
            for i in range(amount):
                nitro += nitros[i]
            nitro = nitro.replace("\n", "\n")

            embd = f"""
<:_:1147506556372516874> **__THANK YOU FOR ORDERING!__** <:_:1147506556372516874>

**Here's your Nitro Boost/Nitro Basic! <a:_:1147287012542533763> <a:_:1147287009568751706> **

{nitro}

<:_:1147506221851611210> Don't forget to vouch for your warranty! <a:_:1147287008289509376>
<:_:1147506221851611210> Always recheck and save your links. <a:_:1147287004485271663>
<:_:1147506221851611210> Strictly No Claim warranty after receiving the nitro. <a:_:1147287002170003516>

**Vouch Here for your warranty:** ⁠https://discord.com/channels/1098326056873767002/1098329820447916083 <:_:1147506557614039060>
            """

            await asyncio.sleep(1.5)
            await user.send(f"{embd}")
            with open(file, "w") as f:
                for i in range(amount, len(nitros)):
                    f.write(nitros[i])

            await interaction.response.send_message(f"""
Sent {amount} Nitro(s) to {user.mention}.
- Thank you for buying from us <a:_:1147592668881371227>
- Leave a vouch in ⁠https://discord.com/channels/1098326056873767002/1098329820447916083 <a:_:1147592668881371227>
- This message may appear as **direct or request** message.
            """)
            return 

        except Exception as e:
            print(e)
            return await interaction.response.send_message(f"Error: {e}", ephemeral=True)

@client.tree.command(name="spdrop", description="Drops Spotify from file to user.")
@commands.has_permissions(administrator=True)
async def drop(interaction: discord.Interaction, user: discord.Member, amount: int, type: int):
    
    if interaction.guild is None:
        return await interaction.response.send_message("You can't use this command in DMs.", ephemeral=True)
    else:
        if type == 1:
            file = "spot.txt"
        else:
            return await interaction.response.send_message("Invalid type.", ephemeral=True)

        try:

            with open(file, "r") as f:
                nitros = f.readlines()

            if amount > len(nitros):
                return await interaction.response.send_message("Not enough Spotifys available.", ephemeral=True)

            nitro = ""  
            for i in range(amount):
                nitro += nitros[i]
            nitro = nitro.replace("\n", "\n")

            embd = f"""
<:_:1147506556372516874> **__THANK YOU FOR ORDERING!__** <:_:1147506556372516874>

**Here's your Spotifys! <a:_:1147287012542533763> <a:_:1147287009568751706> **

{nitro}

<:_:1147506221851611210> Don't forget to vouch for your warranty! <a:_:1147287008289509376>
<:_:1147506221851611210> Always recheck and save your links. <a:_:1147287004485271663>
<:_:1147506221851611210> Strictly No Claim warranty after receiving the nitro. <a:_:1147287002170003516>

**Vouch Here for your warranty:** ⁠https://discord.com/channels/1098326056873767002/1098329820447916083 <:_:1147506557614039060>
            """

            await asyncio.sleep(1.5)
            await user.send(f"{embd}")
            with open(file, "w") as f:
                for i in range(amount, len(nitros)):
                    f.write(nitros[i])


            await interaction.response.send_message(f"""
Sent {amount} Spotifys(s) to {user.mention}.
- Thank you for buying from us <a:_:1147592668881371227>
- Leave a vouch in ⁠https://discord.com/channels/1098326056873767002/1098329820447916083 <a:_:1147592668881371227>
- This message may appear as **direct or request** message.
            """)
            return 

        except Exception as e:
            print(e)
            return await interaction.response.send_message(f"Error: {e}", ephemeral=True)

@client.tree.command(name="restock", description="Restocks the nitro codes.")
@commands.has_permissions(administrator=True)
async def restock(interaction: discord.Interaction, code: str, type: int):
    # if in dm
    if interaction.guild is None:
        return await interaction.response.send_message("You can't use this command in DMs.", ephemeral=True)
    else:
        if interaction.user.id != 1218311311411118161:#
            return await interaction.response.send_message("You can't use this command.", ephemeral=True)
        if type == 1:
            file = "nitro.txt"
        elif type == 2:
            file = "nitrobc.txt"
        else:
            return await interaction.response.send_message("Invalid type.", ephemeral=True)
        try:
            code = code.replace("https://paste.ee/p/", "")
            temp_stock = requests.get(f"https://paste.ee/d/{code}", headers={ "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"}).text;
    
            f = open(file, "a", encoding="utf-8")
            f.write(f"{temp_stock}\n")
            f.close()
            lst = temp_stock.split("\n")
            return await interaction.response.send_message(f"Restocked {len(lst)} nitro codes in {file}.", ephemeral=True)
        except Exception as e:
            print(e)
            return await interaction.response.send_message(f"Error: {e}", ephemeral=True)

@client.tree.command(name="stock", description="Shows the current stock of Nitro URLs.")
@commands.has_permissions(administrator=True)
async def stock1(interaction: discord.Interaction):
    try:
        class stock(discord.ui.View):
            def __init__(self) -> None:
                super().__init__(timeout=None)
        with open("nitro.txt", "r") as f:
            nitro_codes = f.readlines()
        with open("nitrobc.txt", "r") as f:
            nitro_codes2 = f.readlines()
        with open("spot.txt", "r") as f:
            spot = f.readlines()
        banana = stock()
        banana.add_item(discord.ui.Button(label=f"Nitro Boost ({len(nitro_codes)})", style=discord.ButtonStyle.grey,emoji="<a:_:1147287012542533763>" ,custom_id="stock1"))
        banana.add_item(discord.ui.Button(label=f"Nitro Basic ({len(nitro_codes2)})", style=discord.ButtonStyle.grey, emoji="<a:_:1147287009568751706>",custom_id="stock2"))
        banana.add_item(discord.ui.Button(label=f"Spotify ({len(spot)})", style=discord.ButtonStyle.grey, emoji="<a:_:1185975428515647638>",custom_id="stock3"))
        await interaction.response.send_message(view=banana)
    except Exception as e:
        await interaction.response.send_message(f"Error {e}")
        print(e)

@client.event
async def on_ready():
    activity = discord.Game(name=".gg/bestboosts", type="2")
    await client.change_presence(activity=discord.Game(name=".gg/bestboosts"))
    print(Fore.CYAN + "Bot is currently running.")
    await client.tree.sync()

client.run(token)