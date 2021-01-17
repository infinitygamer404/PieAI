import discord
from discord.ext import commands


def main():
    '''
        \@client.command(name='')
        async def ping(ctx):
            await ctx.send(embed=discord.Embed(title='', description='', footer=''))
    '''

    help = commands.Bot(command_prefix=f'')
    client = commands.Bot(command_prefix='.p ')

    x = discord.Member.mentioned_in()
    print(x)

    @client.command(name='new')
    async def new(ctx):
        await ctx.send(embed=discord.Embed(title='', description='', footer=''))

    @client.command(name='ping')
    async def ping(ctx):
        await ctx.send(embed=discord.Embed(title='Pong', description=f'{int(client.latency * 1000)}ms', footer='')), print(f'Pinged by {ctx.author.name}#{ctx.author.discriminator}, {ctx.author.id}!')

    client.run(open('token.txt').read())


if __name__ == '__main__':
    main()
    help()
