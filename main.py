import nextcord
from nextcord.ext import commands


with open("token.txt") as token:
    token.read()


intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=nextcord.intents.all)

@bot.hybrid_command()
async def ping(ctx):
    await ctx.send(f"Pong! You succesfully activated Discord Active Developer Badge")

@bot.event
async def on_ready():
    print("I am running!")
    await bot.tree.sync()

bot.run(token)
