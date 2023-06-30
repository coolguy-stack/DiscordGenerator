import os
import discord
from keepAlive import keep_alive
from discord.ext import commands
import random

file = open("words","r")
words = file.read().split("\n")


client = commands.Bot(command_prefix = '#!')

@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}')

def get_word():
  valid_word = False
  while(not valid_word):
    index = random.randint(0, 235887)
    word = words[index]
    if (len(word)>=3):
      valid_word = True
      return word.capitalize()


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("!"):
    await message.channel.send(get_word() + get_word() + str(random.randint(1, 100)))


keep_alive()

token = os.environ['TOKEN']
client.run(token)