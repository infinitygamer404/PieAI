import discord
from discord.ext import commands

def new(prefix, name, title, description):
    client = commands.Bot(command_prefix=prefix)
    @client.command(name=name)
    async def _ping(ctx):
        await ctx.send(embed=discord.Embed(title=title, description=description))
