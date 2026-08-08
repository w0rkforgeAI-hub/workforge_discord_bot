import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ.get("DiscordBotKey")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="#", intents= intents)

@bot.event 
async def on_ready():
    print("I'm up")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Ping : {round(bot.latency* 1000)}ms")

@bot.command()
async def hello(ctx):
    await ctx.send(f"{ctx.author.mention}Hello {ctx.author.name}")

bot.run(bot_token)