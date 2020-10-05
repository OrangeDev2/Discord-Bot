import discord
import math, random
#from discord.ext.commands import Bot, Cog, command # Comment this out when running this file alone.
from discord.ext import commands # Comment this out when this is a part of Cog file.

bot_prefix = "."

client = commands.Bot(command_prefix=bot_prefix)

class GuessGame(): #(Cog): # Include Cog if it's a part of Cog file in Friendo Bot. Change class name if needed.
    """Commands for Guessing Right Number"""

    #def __init__(self, bot: Bot): # Comment this out when running this file alone.
    #    self.bot = bot

    # Variables in class GuessGame
    lower_bound = 1
    upper_bound = 10

    check_number = round(random.randint(lower_bound, upper_bound))  # Get random number.
    rounds_number = round(math.log(upper_bound - lower_bound + 1,
                                   2))  # Get random number of rounds. Like 3 rounds or 3 attempts left to guess.

    # Look in `guess` command below.
    count = 0

    ##Results in terminal # Comment this out when this is a part of Cog file.
    @client.event
    async def on_ready(): # No `self` if no Cog.
        print('Bot is ready.')

    ### Commands
    @client.command(
        brief="- Use `.bound n1 n2` to set your bound. Use `.bound 0 0` to default bounds.",
        description = " - `.bound n1 n2`\nn1 => lower_bound, n2 => upper_bound\n Example: `.bound 1 10` will set the bound to 1 and 10.\nEnter `.bound 0 0` to get the default."
    )
    # Set up the bounds.  Optional.  (1,10) is the default.
    async def bound(ctx, lower: int,upper: int): # No `self` if no Cog. Will set bound when called.
        # Default bounds unless it's rewritten with .bound command
        lower_bound = 1
        upper_bound = 10

        if lower == 0 or upper == 0: # In case someone want to change it back to default
            GuessGame.lower_bound = lower_bound
            GuessGame.upper_bound = upper_bound
            await ctx.send(f'The bounds are now default. Bounds: {GuessGame.lower_bound} and {GuessGame.upper_bound}.')
        else:
            GuessGame.lower_bound = lower
            GuessGame.upper_bound = upper

        await ctx.send(f'You entered bounds: {GuessGame.lower_bound} and {GuessGame.upper_bound}\nPlease `.start` or `.guess n`')


    # Starting the game...
    @client.command(
        brief=" - Type `.start` to start the game.",
        description = " - Type `.start` to get more details on how play the game."
    )
    async def start(ctx): # No `self` if no Cog.
        await ctx.send(f'Try to guess a random number between {GuessGame.lower_bound}-{GuessGame.upper_bound}.\nType a number after `.guess` command.\nGood Luck!', delete_after=30)


    @client.command(
        brief=" - Enter the number after `.guess` to guess the right number.",
        description = " - Example: `.guess 5` and repeat until you guess it right."
    )
    async def guess(ctx, guess_number: int): # No `self` if no Cog.
        lower_bound = GuessGame.lower_bound
        upper_bound = GuessGame.upper_bound

        check_number = GuessGame.check_number
        rounds_number = GuessGame.rounds_number

        GuessGame.count += 1

        if check_number == guess_number:
            await ctx.send(f'Congratulations you did it! You entered {guess_number}.\nPlease enter `.reset` to restart the bot. Type `.start` to play again or use `.help` to see options.')
            GuessGame.count -= count # So we don't bother passing `4th` if statement.
        elif check_number > guess_number:
            await ctx.send(f'You guessed too small!  Try again {rounds_number - GuessGame.count} round(s) pending.', delete_after=30)
        elif check_number < guess_number:
            await ctx.send(f'You guessed too high!  Try again. {rounds_number - GuessGame.count} round(s) pending.', delete_after=30)
        if GuessGame.count >= rounds_number:
            await ctx.send(f'Sorry! The number is {check_number}. Please enter `.reset` to restart the bot. Type `.start` to play again.')


#def setup(bot: Bot) -> None:
#    """Load the Guess_Game cog."""
#    bot.add_cog(GuessGame(bot))  # # Comment this out when running this file, without Cog, alone.


#client.run('token') for test running as a bot with this file alone.  Make sure to do this without `Cog` and `Bot`
client.run('NzYyMjMwMDc2Nzg3NTIzNjE0.X3mIEw.MnuTTeSrl9T4npLpEaUXQFNywO0')
