import discord
from discord.ext import commands


def New_Command(name, title, description, footer=''):
    client = commands.Bot(command_prefix='.pie ')

    @client.command(name=name)
    async def _ping(ctx):
        await ctx.send(embed=discord.Embed(title=title, description=description, footer=footer))


def main():
    client = commands.Bot(command_prefix='.pie ')

    @client.event
    async def on_ready():
        print(f'Login as {client.user.name}')
        await client.change_presence(activity=discord.Game(name=f'{client.command_prefix}'))

    async def NewCommand():
        New_Command('test2_name', 'test2_title', 'test2_description')

    client.run(open('token.txt').read())


if __name__ == '__main__':
    main()
