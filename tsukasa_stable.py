import discord
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
import aiohttp
import asyncio
from itertools import cycle
import json
import random
from discord import Embed
from datetime import datetime
 
TOKEN = #omitted for safety

client = commands.Bot(command_prefix='!')

WO_channel_id=795496651263442954
WO_role_id='737977617688297512'

channel_id = 797856042888462388

async def on_command_error(self, ctx, exc):
    if isinstance(exc, CommandNotFound):
        pass
    elif hasattr(exc, "original"):
        raise exc.original
    else:
        raise exc



status=cycle(["smug waifu", "O.OOOO34%"])

@tasks.loop(minutes=15.0)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



@client.event
async def on_ready():

    change_status.start()

    print("Logged in as: ")
    print(client.user.name)
    print(client.user.id)
    print("Bot is ready")
    print("-----")

# commands pannel
commands_url='https://media.tenor.com/images/76e7656dddda2237009d67a1fefd8d95/tenor.gif'


@client.command(pass_context=True, aliases=["c", "command"])
async def commands(ctx):
    embed = discord.Embed(title="Commands for Tsukasa!", description="Welcomes to lizwhales's Tsukasa Bot!" +
    "\nWill automatically paste out codes that spawn!\nLook underneath for a full list of commands", color=0xF08080)
    embed.set_thumbnail(url=commands_url)
    embed.add_field(name='!t', value='A truck is on the loose.', inline=False)
    embed.add_field(name='!spam', value='Tsukasa will spam for you to spawn lootcrates', inline=False)
    embed.add_field(name='!stop', value='Tsukasa will stop spamming now!', inline=False)
    
    await ctx.send(embed=embed)


laifu_id = 688202466315206661

dictionary = {}



#cooldown event'title': 'Cooldowns'

work_dictionary = {}



#LOOT CRATE EVENT 'title': 'Lootcrate Spawned!'

relevant_list = []
work_list = []
daily_list = []
vote_list = []

from datetime import datetime

@client.event
async def on_message(message):
    embeds = message.embeds # return list of embeds
    for embed in embeds:
        #print(embed.to_dict())
        dictionary = embed.to_dict()

        print("-------")

        title =(message.embeds[0].title)
        #print(dictionary)
        info = dictionary['fields']
        #print(message.embeds[0].name)

        if (title == 'Lootcrate Spawned!'):
        #print(info)
            for i in info:
                code = i['value']
                codes = code[4:13] 
    
            channel = client.get_channel(channel_id)

            await channel.send(f".claim {codes}")
            
        #print(name)

       
    await client.process_commands(message)




tsukasa_gifs = ["https://media1.tenor.com/images/8c90af00f9d8d2671cdb5ebce7c1bf6e/tenor.gif?itemid=18652929",
"https://i.pinimg.com/originals/fe/5b/79/fe5b7939cd66b3dcef2d65fc1d3a8a92.gif","https://media1.tenor.com/images/516a797b81a22058f57f2f9dc21f2eba/tenor.gif?itemid=19169823"]

test_channel = 797856042888462388

@tasks.loop(seconds=10)
async def spam_loop():
    embed =  discord.Embed(title="Tsukasa helps you spawn :heart:", description="I will spam every 10 seconds~",color=0xEA7DD5)
    embed.set_image(url = random.choice(tsukasa_gifs))
    channel=client.get_channel(channel_id)
    #await channel.send(embed=embed)
    await channel.send(embed=embed)
    
@tasks.loop(seconds=5)
async def spam_msgs():
    channel=client.get_channel(channel_id)
    await channel.send("Testing word spam")

@client.command(pass_context=True, aliases=['spawn', 's'])
async def spam(ctx):        
    spam_loop.start()
    spam_msgs.start()


@client.command(pass_context=True)
async def stop(ctx):
    spam_loop.cancel()
    spam_msgs.cancel()
    embed = discord.Embed(title="Tsukasa stopping now!",color=0xEA7DD5)
    embed.set_image(url='https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/avatars/fc/fc0212284682b38db76a9d2da3cc5d6057dc51a5_full.jpg')
    await ctx.send(embed=embed)







# truck kun gif command!

truck_urls = ['https://i.ytimg.com/vi/hxtRPlBOYug/maxresdefault.jpg', "https://i.ytimg.com/vi/77if5mRTkOE/maxresdefault.jpg"
, "https://cdn.discordapp.com/attachments/617385082562543618/749895549636968528/EJnioT-WkAAU9qI.png", 
"https://cdn.discordapp.com/attachments/735019223763517522/753143052448563210/Flocalgirlhitandkilledonthewayto_dfca0d_7103087.gif",
 "https://cdn.discordapp.com/attachments/617385082562543618/753972714552950874/f92.jpg",
 "https://cdn.discordapp.com/attachments/617385082562543618/753973009856856174/18904.jpg",
 "https://pbs.twimg.com/media/EXfV-SaVcAE0tlL?format=jpg&name=small",
 "https://i.imgur.com/9b16t0a.gif"]

@client.command(pass_context = True, aliases =['truck'] )
async def t(ctx):
    embed = discord.Embed(title="TRUCK KUN UWU (>////<)", color=0xCA97FF)
    embed.set_image(url=random.choice(truck_urls))
    
    await ctx.send(embed=embed)





client.run(TOKEN)

