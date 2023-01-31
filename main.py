#---
from discord.ext import commands, tasks
import discord
import string

import sys
import asyncio
import nest_asyncio
import random
import os
import requests
import time
from discord.utils import get
from datetime import datetime
from keep_alive import keep_alive
import json
import re

# UCnRLNqdJspckDnNPRcYLMSA



intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)



@bot.event
async def on_ready():
    print("Scooter is online yay!!")

    


msg_dump_channel = 1006225893758345316


@bot.event
async def on_message(message: discord.Message):
    channel = bot.get_channel(msg_dump_channel)
    if message.guild is None and not message.author.bot:
        # if the channel is public at all, make sure to sanitize this first
        embed = discord.Embed(title=message.content, color=0x1abc9c)
        embed.add_field(name="Sent by: ", value=message.author)
        embed.timestamp = datetime.now()
        embed.set_thumbnail(url=message.author.avatar_url)
        await channel.send(embed=embed)

    await bot.process_commands(message)




bot.remove_command("help")




@bot.command()
@commands.is_owner()
async def DM(ctx, user: discord.Member, *, message=None):
    """Sends a person a dm from a bot. Only people with ban perms, and can manage roles can access this command to prevent overusing."""

    await ctx.send("What is the message you want to send this user?")

    message = await bot.wait_for(
        "message",
        check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=200.0)

    message = message.content

    await user.send(message)

    await ctx.send(f"Message sent to {user}")


@bot.command(administrator=True)
async def dm(ctx, user: discord.Member, *, message=None):
    """Sends a person a dm from a bot. Only people with ban perms, and can manage roles can access this command to prevent overusing."""

    await ctx.send("What is the message you want to send this user?")

    message = await bot.wait_for(
        "message",
        check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=200.0)

    message = message.content

    await user.send(message)

    await ctx.send(f"Message sent to {user}")


@bot.command()
async def yesno(ctx: commands.Context):
    """In Beta"""

    await ctx.send(
        "Ask me a yes, no question, and I'll answer with my wise scooter power yes or no!!"
    )

    try:

        yesno = await bot.wait_for("message",
                                   check=lambda m: m.author == ctx.author and m
                                   .channel == ctx.channel,
                                   timeout=60.0)

    except asyncio.TimeoutError:

        await ctx.send("You took too long to answer try again!")

    else:
        choice = ["no", "yes"]

        e = random.choice(choice)

        message = await ctx.send("Scooter says: ...")
        await asyncio.sleep(0.01)
        await message.edit(content="Scooter says: |..")
        await asyncio.sleep(0.01)
        await message.edit(content="Scooter says: .|.")
        await asyncio.sleep(0.01)
        await message.edit(content="Scooter says: ..|")
        await asyncio.sleep(0.01)
        await message.edit(content="Scooter says: |..")
        await asyncio.sleep(0.01)
        await message.edit(content="Scooter says: .|.")
        await asyncio.sleep(0.01)
        await message.edit(content="Scooter says: ..|")
        await message.edit(content=f"Scooter says: {e}")


@bot.command()
@commands.is_owner()
async def setstatus(ctx: commands.Context):
    """Set the bot's status. Only ducky#8888 can do this!!"""

    await ctx.send("Type the bot's status: ")

    status = await bot.wait_for(
        "message",
        check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)

    await ctx.send("What type of status(Game, Watching, Listening)")

    status_type = await bot.wait_for(
        "message",
        check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)

    if status_type.content.lower() == "game":
        await bot.change_presence(activity=discord.Game(name=status.content))

    if status_type.content.lower() == "watching":
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name=status.content))

    if status_type.content.lower() == "listening":
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, name=status.content))


@bot.command()
async def qpoll(ctx: commands.Context, channel: discord.TextChannel):

    await ctx.send("Is the question QOTD or POLL. Please put it exactly.")

    typeqp = await bot.wait_for(
        "message",
        check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=60.0)

    typeqp = typeqp.content

    await ctx.send(
        "What is the question of the day? Note: The question will react :one: and :two:, etc"
    )

    question = await bot.wait_for(
        "message",
        check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=60.0)

    question = question.content

    await ctx.send(
        "How many options do you want your question to have? Min: 2 | Max: 5 Please put a number, not the word."
    )

    amount = await bot.wait_for(
        "message",
        check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
        timeout=30.0)

    amount = amount.content
    #await ctx.send("What is the channel ID you want to send it too. Note: You have to turn on developer mode, you can find how to turn it on here: https://www.howtogeek.com/714348/how-to-enable-or-disable-developer-mode-on-discord/")

    #id = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

    #channel = bot.get_channel(id)

    embed = discord.Embed(title=f"{typeqp}: {question} ", color=0x1abc9c)
    embed.add_field(name=f"{typeqp} made by: ", value=ctx.author)

    embed.timestamp = datetime.now()

    message = await channel.send(embed=embed)
    if amount == "1":
        await channel.send(
            "You can't do that! The minimum amount is 2! Try again!")
    if amount == "2":
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
    if amount == "3":
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")
    if amount == "4":
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")
        await message.add_reaction("4️⃣")
    if amount == "5":
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")
        await message.add_reaction("4️⃣")
        await message.add_reaction("5️⃣")

#channel = bot.get_channel()


@bot.command()
async def war_results(ctx: commands.Context):
    """Creates a war result embed with your specfic requirments."""

    team1_players = {}
    team2_players = {}

    try:

        await ctx.send("What is the first team?")

        team1 = await bot.wait_for("message",
                                   check=lambda m: m.author == ctx.author and m
                                   .channel == ctx.channel,
                                   timeout=30.0)

        await ctx.send("What's the second team?")

        team2 = await bot.wait_for("message",
                                   check=lambda m: m.author == ctx.author and m
                                   .channel == ctx.channel,
                                   timeout=30.0)

        await ctx.send(
            "What's the score. First team - Second team(Example: 4-0, 4-1)")

        score = await bot.wait_for("message",
                                   check=lambda m: m.author == ctx.author and m
                                   .channel == ctx.channel,
                                   timeout=30.0)

        team1 = team1.content

        team2 = team2.content

        #loop
        x = 0
        while x == 0:

            await ctx.send(
                f"Who played for {team1}. Note: Once you finished with all the players, say 'done' "
            )
            players = await bot.wait_for("message",
                                         check=lambda m: m.author == ctx.author
                                         and m.channel == ctx.channel,
                                         timeout=30.0)

            players = players.content

            if players == 'done':
                await ctx.send(
                    "Are you sure you're done? Say 'done' again to comfirm")
                round = await bot.wait_for("message",
                                           check=lambda m: m.author == ctx.
                                           author and m.channel == ctx.channel,
                                           timeout=30.0)

            else:
                await ctx.send(f"How many rounds did {players} play?")

                round = await bot.wait_for("message",
                                           check=lambda m: m.author == ctx.
                                           author and m.channel == ctx.channel,
                                           timeout=30.0)
            round = round.content

            if round == 'done':
                x = 1

            else:
                team1_players[players] = round

        op = 0
        while op == 0:

            await ctx.send(
                f"Who played for {team2}. Note: Once you finished with all the players, say 'done' "
            )
            player = await bot.wait_for("message",
                                        check=lambda m: m.author == ctx.author
                                        and m.channel == ctx.channel,
                                        timeout=30.0)

            player = player.content

            if player == 'done':
                await ctx.send(
                    "Are you sure you're done? Say 'done' again to comfirm")
                rounds = await bot.wait_for(
                    "message",
                    check=lambda m: m.author == ctx.author and m.channel == ctx
                    .channel,
                    timeout=30.0)

            else:
                await ctx.send(f"How many rounds did {player} play?")

                rounds = await bot.wait_for(
                    "message",
                    check=lambda m: m.author == ctx.author and m.channel == ctx
                    .channel,
                    timeout=30.0)
            rounds = rounds.content

            if rounds == 'done':
                op = 1

            else:
                team2_players[player] = rounds

                await ctx.send("Who got MVP?")

                mvp = await bot.wait_for("message",
                                         check=lambda m: m.author == ctx.author
                                         and m.channel == ctx.channel,
                                         timeout=30.0)

                mvp = mvp.content

                await ctx.send("Who got runner up?")

                ru = await bot.wait_for("message",
                                        check=lambda m: m.author == ctx.author
                                        and m.channel == ctx.channel,
                                        timeout=30.0)

                ru = ru.content

    except asyncio.TimeoutError:
        await ctx.send("You took too long to answer, try again!")

    else:

        score = score.content

        elements = len(team1_players)
        element = len(team2_players)

        n = 0
        p = 0

        embed = discord.Embed(title=f"War Results: {team1} {score} {team2} ",
                              color=0xf47fff)

        embed.add_field(name=f"{team1}: ", value="**Rounds: **")

        while n < elements:
            keys = list(team1_players.keys())[n]
            value = list(team1_players.values())[n]

            embed.add_field(name=f"{keys}", value=f"{value} rounds")

            n += 1

        embed.add_field(name=f"{team2}: ", value="**Rounds: **")

        while p < element:
            key = list(team2_players.keys())[p]
            values = list(team2_players.values())[p]

            embed.add_field(name=f"{key}", value=f"{values} rounds")

            p += 1

        embed.add_field(name="--------------------",
                        value="-------------------")

        await ctx.send(embed=embed)


@bot.command()
async def helpme(ctx: commands.Context):
    """Scooter gives advice. Just tell it what's wrong! Do !helpme"""

    advice = [
        "Get help", "Adopt a duck", "Move to another country", "Rob a bank!",
        "Eat a spider", "Go see a witch", "Do yoga on a volcano",
        "Watch a chessy romantic show", "Get a girlfriend", "Play surviv.io",
        "Watch Mrbeast", "Look up Hom Tolland", "Lock yourself in a cabinent",
        "Give $1 to a random stranger!", "Hook up with a stranger.",
        "Cry you little baby", "Give 20$ to ducky#8888",
        "Delete your discord account", "idk you figure it out",
        "stop asking me stuff ", "go fasting.", "milk me baby", "Love you too",
        "no", "noob", "get better already",
        "1. Not my problem. 2. touch some grass",
        "that's so aids sorry can't help you", "?"
    ]

    try:
        embed = discord.Embed(title="What seems to be the problem? ",
                              color=0xf47fff)

        await ctx.send(embed=embed)

        problem = await bot.wait_for("message",
                                     check=lambda m: m.author == ctx.author and
                                     m.channel == ctx.channel,
                                     timeout=30.0)

    except asyncio.TimeoutError:
        await ctx.send(
            "You took too long to answer, looks like you don't want my advice :(("
        )

    else:
        problem = problem.content

        advice_rando = random.choice(advice)
        embed = discord.Embed(title=f"**Response to: `{problem}`  **",
                              color=0xf47fff)
        embed.add_field(name="**Scooter's Advice**", value=f"{advice_rando}")

        await ctx.send(embed=embed)


@bot.command()
async def rate(ctx: commands.Context, user: discord.Member):
    """Scooter rates a user!! Do !rate @user"""
    yeet = [
        "Dumb", 'gay', 'noob', 'smart', 'chicken', 'witch', 'bot', 'human',
        'duck', 'coward', "dog", "simp", "addict", "gangster", "woman", "pro",
        "horse", "old", "grandpa", "grandma", "toxic", "braindead", "retard"
    ]

    username = user.name

    things = random.choice(yeet)
    val = random.randint(1, 100)
    embed = discord.Embed(title=f"Rating {user}",
                          description="Rate",
                          colour=0x87CEEB)

    embed.add_field(name="Scooter's rating:",
                    value=f"{username} is %{val} {things}",
                    inline=False)

    await ctx.send(embed=embed)




with open("token.txt") as f:
    TOKEN = f.read().strip()

keep_alive()
my_secret = os.environ['TOKEN']
bot.run(my_secret)