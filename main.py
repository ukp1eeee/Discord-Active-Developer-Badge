import discord
from discord.ext import commands


with open("token.txt", "r", encoding="utf-8") as f:
    token = f.read().strip()


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.hybrid_command()
async def ping(ctx):
    await ctx.send(f"Pong! You succesfully activated Discord Active Developer Badge") #You succesfully activated Discord Developer Badge!

@bot.event
async def on_ready():
    print("I am running!")
    await bot.tree.sync()

bot.run(token)
