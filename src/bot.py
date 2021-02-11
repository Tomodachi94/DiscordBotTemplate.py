from discord.ext import commands
# This imports the Discord package for use in the bot.
import os
from python_dotenv import load_dotenv
# You'll need this package to load your token from .env. 
# It is an encouraged practice to keep tokens etc out of source.

bot = commands.Bot(command_prefix="!")

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
    
  else:
    print(f'Unable to load {filename[:-3]}')
    
bot.run(os.getenv("DISCORD_TOKEN"))
