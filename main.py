import discord
from discord.ext import commands


def main():
    '''
        \@client.command(name='')
        async def ping(ctx):
            await ctx.send(embed=discord.Embed(title='', description='', footer=''))
    '''

    client = commands.Bot(command_prefix='.p ')

    @client.command(name='new')
    async def new(ctx):
        await ctx.send(embed=discord.Embed(title='', description='', footer=''))

    @client.command(name='ping')
    async def ping(ctx):
        await ctx.send(embed=discord.Embed(title='Pong', description=f'{int(client.latency * 1000)}ms', footer='')), print(f'Pinged by {discord.User.id}!')

    @client.event
    async def on_ready():print(f'Login as {client.user.name}');await client.change_presence(activity=discord.Game(name=f'{client.command_prefix}'));

    client.run(open('token.txt').read())


def help():
    client = commands.Bot(command_prefix='.p ')


if __name__ == '__main__':
    main()
    help()
