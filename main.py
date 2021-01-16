import discord
from discord.ext import commands


def main():
    client = commands.Bot(command_prefix='.pie ')

    @client.event
    async def on_ready():
        print(f'Login as {client.user.name}')
        await client.change_presence(activity=discord.Game(name=f'{client.command_prefix}'))

    @client.command(name='test2_name')
    async def _ping(ctx):
        await ctx.send(embed=discord.Embed(title='title', description='description', footer=''))

    client.run(open('token.txt').read())


if __name__ == '__main__':
    main()
