import discord
from discord.ext import commands


def main():
    '''
        \@client.command(name='')
        async def ping(ctx):
            await ctx.send(embed=discord.Embed(title='', description='', footer=''))
    '''

    client = commands.Bot(command_prefix='.p ')

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')
        game = discord.Game(name=f'{client.command_prefix}')
        await client.change_presence(activity=game)


    @client.command(name='new')
    async def new(ctx):
        await ctx.send(embed=discord.Embed(title='', description='', footer=''))


    @client.command(name='ping')
    async def ping(ctx):
        e = discord.Embed(title='Pong',
        description=f'{int(client.latency * 1000)}ms',
        footer='')

        await ctx.send(embed=e)
        print(f'Pinged by {ctx.author}!')


    @client.event
    async def on_message(message):
        if client.user.mentioned_in(message):
            e = discord.Embed(title='Help',
            description='Use .p to signal you want to use a command',
            footer='Use .p help for help')

            await message.channel.send(embed=e)
        else:
            pass

        await client.process_commands(message)


    client.run(open('token.txt').read())


if __name__ == '__main__':
    main()

