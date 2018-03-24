import random
import asyncio
import requests
from discord import Game
from discord.ext.commands import Bot

TOKEN = ''
BOT_PREFIX = ('!')

client = Bot(command_prefix = BOT_PREFIX)

@client.command(name = '8ball',
                description = 'Answers a yes/no question',
                brief = 'Answers from the beyond',
                pass_context = True)

async def eight_ball(context):
    possible_responses = [
        'Very doubtful',
        'My reply is no',
        'Yes definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name = 'hello',
                description = 'Say hello to your waifu',
                brief = 'Say hello to your waifu',
                pass_context = True)

async def hello(context):
    await client.say('Ohayō ' + context.message.author.mention)

@client.command(name = 'love',
                description = 'Your waifu loves you',
                brief = 'Talk to your waifu',
                pass_context = True)

async def love(context):
    await client.say('Watashi wa, anata o aishiteimasu ' + context.message.author.mention)


@client.command(name = 'square',
                description = 'Ask your waifu to calculate square of a number',
                brief = 'Ask your waifu to calculate square of a number')

async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + ' squared is ' + str(squared_value))

@client.event
async def on_ready():
    await client.change_presence(game = Game(name = "with senpai"))
    print('Logged in as ' + client.user.name)

@client.command(name = 'bitcoin',
                description = 'Hurts your feelings',
                brief = 'Ask your waifu for a current bitcoin price')
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say("Bitcoin price is: $" + value)

@client.command(name = 'anime',
                description = '¯\_(ツ)_/¯',
                brief = 'Ask your waifu for her favourite anime')
async def anime():
    await client.say('Boku no Pico')

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print('Current servers: ')
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(700)

client.loop.create_task(list_servers())
client.run(TOKEN)