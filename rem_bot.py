import discord
from discord.ext import commands, tasks
import aiohttp
import asyncio
import json
from itertools import cycle
import random 
import time
# by renaming the datetime as dt you can use both modules without conflicting names!
from datetime import datetime, timedelta
import datetime as dt
from discord.utils import get
from datetime import date


TOKEN = 'NzM0NjQ4NDQ2MzM3OTQxNjA2.XxUwrg.Brb_WL1epHxHVsfJI1d8asd-ybU'
client = commands.Bot(command_prefix = '!')

channel_id = 617385082562543618
role_id = '737977617688297512'



# will cycle through the strings
status = cycle([ 'rem > emilia', 'rem <3 liz'])

from discord.ext.commands import CommandNotFound
async def on_command_error(self, ctx, exc):
    if isinstance(exc, CommandNotFound):
        pass
    elif hasattr(exc, "original"):
        raise exc.original
    else:
        raise exc

@client.event
async def on_ready():

    change_status.start()
    reminder.start()
    sam.start()
    grocery.start()


    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('Bot is ready')
    print('-----')

# commands list of rem's functionality

url = 'https://i.gifer.com/4DT6.gif'

@client.command(pass_context=True, aliases=['c', 'command'])
async def commands(ctx):
    embed = discord.Embed(title="Commands for Rem!", description="Welcome to lizwhale's Rem Bot!\n Rem will automatically tag for roll times and gifts." +
     "\nLook underneath for a full list of commands",color=0x89cff0)
    embed.set_thumbnail(url=url)
    embed.add_field(name='!sp', value='Tags @weebs for a yuge sp.', inline=False)
    embed.add_field(name='!s', value='Rem joins you in Sadge.', inline=False)
    embed.add_field(name='!bdo', value='The next world boss timing appears.', inline=False)
    embed.add_field(name='!rem', value='Reveal a cute Rem.', inline=False)
    embed.add_field(name='!josh', value='Tag Josh easily.', inline=False)
    embed.add_field(name='!t', value='A truck is on the loose.', inline=False)
    embed.add_field(name='!e', value='Enchanting simulator.     ', inline=False)
    embed.add_field(name='!ping', value="Check discord's latency.", inline=False)
    await ctx.send(embed=embed)

# BDO ENCHANTING CALC

def check(ctx):
    return lambda m: m.author == ctx.author and m.channel == ctx.channel

async def get_input_of_type(func, ctx):
    while True:
        try:
            msg = await client.wait_for('message', check=check(ctx))
            return func(msg.content)
        except ValueError:
            continue


@client.command(pass_context=True, aliases = ['enchanting','e'])
async def enchant(ctx):
    #await ctx.send("Please enter your failstack number:")
    #failstack = await get_input_of_type(int, ctx)
    await ctx.send("Please enter your percentage of success: ")
    success_chance = await get_input_of_type(float, ctx)
    if ((random.random()) * 100) <= success_chance:
        await ctx.send("Success")
    else:
        await ctx.send("Fail")


# DICTIONARIES FOR EACH DAY

mon_dict = {
    "Nouver":"0:00:00", 
    "Vell":"7:00:00",
    "Kzarka":"3:00:00", 
    "Garmouth":"10:00:00",
    "Kzarka & Nouver":"13:15:00",
    "Kutum & Karanda":"15:15:00",
    "Karanda":"17:00:00",
    "Kzarka":"20:00:00"
}

tues_dict = {
    "Kzarka":"0:00:00",
    "Offin":"3:00:00",
    "Kutum":"7:00:00",
    "Nouver": "10:00:0",
    "Kzarka":"13:15:00",
    "Karanda":"15:15:00",
    "Kutum":"17:00:00",
    "Kzarka":"20:00:00"
}

weds_dict = {
    "Nouver":"00:00:00",
    "Kutum":"3:00:00",
    "Nouver":"7:00:00",
    "Karanda":"10:00:00",
    "Garmouth":"13:15:00",
    "Kutum & Kzarka":"15:15:00",
    "Karanda":"17:00:00",
}

thurs_dict = {
    "Karanda":"00:00:00",
    "Nouver":"3:00:00",
    "Kutum & Offin":"7:00:00",
    "Vell":"10:00:00",
    "Karanda & Kzarka":"13:15:00",
    "Quint & Muraka":"14:15",
    "Nouver":"15:15:00",
    "Kutum":"17:00:00",
    "Kzarka":"20:00:00"
}

fri_dict = {
    "Kutum":"00:00:00",
    "Nouver":"3:00:00",
    "Kzarka":"7:00:00",
    "Kutum":"10:00:00",
    "Garmouth":"13:15:00",
    "Kzarka & Karanda":"15:15:00",
    "Nouver":"17:00:00",
    "Karanda":"20:00:00"
}

sat_dict = {
    "Kutum":"00:00:00",
    "Karanda":"3:00:00",
    "Nouver":"7:00:00",
    "Kzarka":"10:00:00",
    "Karanda":"15:15:00",
    "Offin":"17:00:00",
    "Nouver":"20:00:00"
}

sun_dict = {
    "Kutum":"00:00:00",
    "Nouver":"3:00:00",
    "Quint & Muraka":"7:00:00",
    "Kzarka & Karanda":"10:00:00",
    "Nouver & Kutum":"15:15:00",
    "Kzarka":"17:00:00",
    "Kutum":"20:00:00"
}
def get_key(val):
    for key, value in mon_dict.items():
        if val == value:
            return key
def get_key1(val):
    for key, value in tues_dict.items():
        if val == value:
            return key
def get_key2(val):
    for key, value in weds_dict.items():
        if val == value:
            return key
def get_key3(val):
    for key, value in thurs_dict.items():
        if val == value:
            return key
def get_key4(val):
    for key, value in fri_dict.items():
        if val == value:
            return key
def get_key5(val):
    for key, value in fri_dict.items():
        if val == value:
            return key
def get_key6(val):
    for key, value in fri_dict.items():
        if val == value:
            return key

mon_list = []
tues_list = []
weds_list = []
thurs_list = []
fri_list = []
sat_list = []
sun_list = []

print(dt.datetime.now())

# THERE IS A 10 HOUR DIFFERENCE IN INDIA 
'''
time = datetime.now() + timedelta(hours=10)
print(time)
z = '{:%H:%M:%S}'.format(time)
print(z)

'''

@client.command()
async def bdo(ctx):
    if date.today().weekday() == 0:
        time = datetime.now() + timedelta(hours=10)
        time = '{:%H:%M:%S}'.format(time)
        for values in mon_dict:
            if mon_dict[values] > time:
                vals = mon_dict[values]
                mon_list.append(vals)
        closest_boss = min(mon_list)
        start = str(closest_boss)
        end = str(time)
        start_dt = dt.datetime.strptime(start, '%H:%M:%S')
        end_dt = dt.datetime.strptime(end, '%H:%M:%S')
        diff = (start_dt - end_dt)
        boss = (get_key(start))
        await ctx.send(f"The boss {boss} will spawn in {diff} (H:M:S).")
    elif date.today().weekday() == 1:
        time = datetime.now() + timedelta(hours=10)
        time = '{:%H:%M:%S}'.format(time)
        for values in tues_dict:
            if tues_dict[values] > time:
                vals = tues_dict[values]
                tues_list.append(vals)
        closest_boss = min(tues_list)
        start = str(closest_boss)
        end = str(time)
        start_dt = dt.datetime.strptime(start, '%H:%M:%S')
        end_dt = dt.datetime.strptime(end, '%H:%M:%S')
        diff = (start_dt - end_dt)
        boss = (get_key1(start))
        await ctx.send(f"The boss {boss} will spawn in {diff} (H:M:S).")
    elif date.today().weekday() == 2:
        time = datetime.now() + timedelta(hours=10)
        time = '{:%H:%M:%S}'.format(time)
        for values in weds_dict:
            if weds_dict[values] > time:
                vals = weds_dict[values]
                weds_list.append(vals)
        closest_boss = min(weds_list)
        start = str(closest_boss)
        end = str(time)
        start_dt = dt.datetime.strptime(start, '%H:%M:%S')
        end_dt = dt.datetime.strptime(end, '%H:%M:%S')
        diff = (start_dt - end_dt)
        boss = (get_key2(start))
        await ctx.send(f"The boss {boss} will spawn in {diff} (H:M:S).")
    elif date.today().weekday() == 3:
        time = datetime.now() + timedelta(hours=10)
        time = '{:%H:%M:%S}'.format(time)
        for values in thurs_dict:
            if thurs_dict[values] > time:
                vals = thurs_dict[values]
                thurs_list.append(vals)
        closest_boss = min(thurs_list)
        start = str(closest_boss)
        end = str(time)
        start_dt = dt.datetime.strptime(start, '%H:%M:%S')
        end_dt = dt.datetime.strptime(end, '%H:%M:%S')
        diff = (start_dt - end_dt)
        boss = (get_key3(start))
        await ctx.send(f"The boss {boss} will spawn in {diff} (H:M:S).")
    elif date.today().weekday() == 4:
        time = datetime.now() + timedelta(hours=10)
        time = '{:%H:%M:%S}'.format(time)
        for values in fri_dict:
            if fri_dict[values] > time:
                vals = fri_dict[values]
                fri_list.append(vals)
        closest_boss = min(fri_list)
        start = str(closest_boss)
        end = str(time)
        start_dt = dt.datetime.strptime(start, '%H:%M:%S')
        end_dt = dt.datetime.strptime(end, '%H:%M:%S')
        diff = (start_dt - end_dt)
        boss = (get_key4(start))
        await ctx.send(f"The boss {boss} will spawn in {diff} (H:M:S).")
    elif date.today().weekday() == 5:
        time = datetime.now() + timedelta(hours=10)
        time = '{:%H:%M:%S}'.format(time)
        for values in sat_dict:
            if sat_dict[values] > time:
                vals = sat_dict[values]
                sat_list.append(vals)
        closest_boss = min(sat_list)
        start = str(closest_boss)
        end = str(time)
        start_dt = dt.datetime.strptime(start, '%H:%M:%S')
        end_dt = dt.datetime.strptime(end, '%H:%M:%S')
        diff = (start_dt - end_dt)
        boss = (get_key5(start))
        await ctx.send(f"The boss {boss} will spawn in {diff} (H:M:S).")
    elif date.today().weekday() == 6:
        time = datetime.now() + timedelta(hours=10)
        time = '{:%H:%M:%S}'.format(time)
        for values in sun_dict:
            if sun_dict[values] > time:
                vals = sun_dict[values]
                sun_list.append(vals)
        closest_boss = min(sun_list)
        start = str(closest_boss)
        end = str(time)
        start_dt = dt.datetime.strptime(start, '%H:%M:%S')
        end_dt = dt.datetime.strptime(end, '%H:%M:%S')
        diff = (start_dt - end_dt)
        boss = (get_key6(start))
        await ctx.send(f"The boss {boss} will spawn in {diff} (H:M:S).")
        
'''

# grocery reminder!

x = dt.datetime.now()
@tasks.loop(seconds = 60)
async def grocery():
    if datetime.now().minute == 0 and x.day == 5:
        channel = client.get_channel(bdo_channel)
        embed = discord.Embed(title = "Please remember to cancel your Woolworth's delivery subscription today", 
        description="go to https://www.woolworths.com.au/ and cancel the fee", color=0x00351B)
        await channel.send(embed=embed)


'''

# such an easy solution: loops every hour when the current datetime minute is at :01

@tasks.loop(seconds = 60)
async def reminder():
    if datetime.now().minute == 0:
        channel = client.get_channel(channel_id)
        #embed = discord.Embed(title=f"Time to roll! <@&{role_id}>",color=0x89cff0)
        #await channel.send(embed=embed)
        await channel.send(f"Time to roll! <@&{role_id}>")

bdo_channel = 735019223763517522

@tasks.loop(minutes = 60)
async def sam():
    if datetime.now().hour == 1:
        channel = client.get_channel(bdo_channel)
        await channel.send(f"Collect your guild monies! <@200934486110765056>")

# THIS IS FOR GIFTS

test = '<:Sadge:734406359893803098>'

purple_gift =  '<:PurpleGift:689718974023335936>'
blue_gift = '<:BlueGift:689718987503829122>'
red_gift = '<:RedGift:689718959708307498>'
green_gift = '<:GreenGift:689718996018266127>'
orange_gift = '<:OrangeGift:689719005941858411>'

# make list of reacts, do a nest loop comp to check if is in one of them then execute if statement

gift_list = ['<:PurpleGift:689718974023335936>',
'<:BlueGift:689718987503829122>',
'<:RedGift:689718959708307498>',
'<:GreenGift:689718996018266127>',
'<:OrangeGift:689719005941858411>']


@client.event
async def on_raw_reaction_add(reaction):
    if reaction.channel_id == channel_id:
        if str(reaction.emoji) in gift_list:
            channel = client.get_channel(channel_id)
            msg = await channel.fetch_message(reaction.message_id)
            r = get(msg.reactions, emoji=reaction.emoji)
            if r.count == 2:
                await channel.send(f"Gifto! <@&{role_id}>")
           


rem_urls = [
"https://media.tenor.com/images/b1a33856f369b7635effdadcc7ccacca/tenor.gif",
"https://i.imgur.com/kfGENf2.gif",
"https://cdn.discordapp.com/attachments/617385082562543618/752403169253785620/image0.jpg",
"https://i.imgur.com/2xi2FkV.gif",
"https://i.pinimg.com/originals/22/0b/ab/220babfd5f8b629cc16399497ed9dd96.gif",
"https://cdn.discordapp.com/attachments/617385082562543618/752404036782784522/remmss6.png",
"https://cdn.discordapp.com/attachments/617385082562543618/752406422158835732/image0.jpg"
]
@client.command()
async def rem(ctx):
    embed = discord.Embed(color=0x89cff0)
    embed.set_image(url=random.choice(rem_urls))
    await ctx.send(embed=embed)

    

# creates a loop which updates status of bot every 10 seconds

@tasks.loop(seconds=60.0)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command(pass_context=True, aliases=['j'])
async def josh(ctx):
    await ctx.channel.send(f"What does the cake taste like? <@214708221737172992>")
    
from discord import Embed
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

# testing command

@client.command(pass_context = True,  aliases=['bc', 'b'])
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.channel.send("The bittycoin price is: $" + response['bpi']['USD']['rate'])


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(pass_context = True, aliases=['question']) 
async def ask(ctx, * , question):

    responses = ['dont do it ', 
    'smoking is bad ', 
    'dart takes away 7 minutes of your life',
    'this makes Rem sadge'
    'stfu cunt']
    
    await ctx.send(f'Question: {question}\n Answer: {random.choice(responses)}')


@client.command(pass_context = True, aliases = ['Sadge', 's'])
async def sadge(ctx):
    await ctx.send('<:Sadge:734406359893803098>')


@client.command()
async def sp(ctx):
    channel = client.get_channel(channel_id)
    await channel.send(f"YUGE SP! <@&{role_id}>")




client.run(TOKEN)

