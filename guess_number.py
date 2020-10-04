import discord
import math, random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

### Results in terminal
@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

async def on_member_remove(member):
    print(f'{member} has left a server.')

### Commands
@client.command()
async def help(ctx):
    pass

@client.command()
async def ping(ctx): # write '.ping' to invoke the command.  .ping => ping(ctx)
    # invoke the command
    await ctx.send(f'Pong! \nType `.start` to start a game.')

# Give details.
@client.command()
async def start(ctx):
    # Dm user
    await ctx.send(f'Try to guess a random number between 1-100.\nType a number after `.n` command.\nExample: `.n 3`\nHave fun!')
    # await ctx.send(f'Hello!\n`Let me explain how this game works.`\nYou can enter 2 numbers for lower bound and upper bound. Try to guess a random number between bounds within rounds or you lose. You will be given chances to guess the number.\nUse `.bound n1 n2` to set lower_bound and upper_bound.\nYou will be given number of rounds and use `.n` to guess number!\nGood luck!')

    global check_number
    check_number = round(random.randint(1, 100)) # Random number between 1 and 100
    #await ctx.send(check_number)

@client.command()
async def n(ctx, guess_number: int):
    count = 0

    while count <
    if check_number == guess_number:
        await ctx.send(f'Congratulations you did it! You entered {guess_number}.\nType `.start` to play again.')
    elif check_number > guess_number:
        await ctx.send(f'You guessed too small!  Try again') #{roundn - count} round(s) pending.'
    elif check_number < guess_number:
        await ctx.send(f'You guessed too high!  Try again.') #{roundn - count} round(s) pending.'




client.run('token') # Put your token in string there.
