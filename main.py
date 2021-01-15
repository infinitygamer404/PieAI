import discord
from discord.ext import commands
import new_com

TOKEN = open('token.txt').read()
print(TOKEN)

def main(TOKEN):
    client = commands.Bot(command_prefix='.pie ')

    @client.command(name='NAME')
    async def _NAME(ctx):
        embed = discord.Embed(title=f'{client.user.name} - [DESCRIPTION]', description=f'[INFO]')
        await ctx.send(embed=embed)

    @new_com.new()
    def NewCommand():
        pass

    @client.event
    async def on_ready():
        print(f'Login as {client.user.name}')
        # NOW SET THE ACTIVITY
        await client.change_presence(activity=discord.Game(name=f'{client.command_prefix}ping'))

    client.run(TOKEN)

main(TOKEN)
