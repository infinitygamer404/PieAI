import discord
from discord.ext import commands
import new_com


def main():
    client = commands.Bot(command_prefix='.pie ')

    @client.event
    async def on_ready():
        print(f'Login as {client.user.name}')
        await client.change_presence(activity=discord.Game(name=f'{client.command_prefix}'))

    @new_com.new(description='test_description', name='test_name', prefix='.pie ', title='test_title')
    async def NewCommand():
        pass

    client.run(open('token.txt').read())


main(open('token.txt').read())
