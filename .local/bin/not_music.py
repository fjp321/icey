import discord
import time
import glob
import asyncio
from discord.ext import commands
import os
import random
from urllib import parse, request
import re

music_dir='elmo'
bot = commands.Bot(command_prefix='>', description="Making Music")
song_array = []
current_song=''
banned_phrases=['tianmen square', 'china bad']

#social credit
#@bot.event()
#async def on_message(message):
#    for phrase in banned_phrases:
#        if phrase in message.content:
#            await message.channel.send("ALERT USER {0}, -10000000 SOCIAL CREDIT POINTS!!11!!1!1!!!!!!".format(message.author.mention))
#            return

# ping test
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def next(ctx):
    # grab the user who sent the command
    user = ctx.message.author
    # get user guild
    guild = ctx.message.guild
    channel = None
    for vc in guild.voice_channels:
        if vc.name == "Concert":
            channel = vc
            break
    if channel is None:
        channel = user.voice.voice_channel
    # try to connect
    try:
        vc = await channel.connect()
    except:
        vc = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    vc.stop()

@bot.command()
async def stop(ctx):
    # grab the user who sent the command
    user = ctx.message.author
    # get user guild
    guild = ctx.message.guild
    channel = None
    for vc in guild.voice_channels:
        if vc.name == "Concert":
            channel = vc
            break
    if channel is None:
        channel = user.voice.voice_channel
    # try to connect
    try:
        vc = await channel.connect()
    except:
        vc = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    await vc.disconnect()

@bot.command()
async def queue(ctx):
    global song_array
    for song in song_array:
        await ctx.send(song)

@bot.command()
async def current(ctx):
    global current_song
    await ctx.send(current_song)

# connect to "Concert" channel and play arg tracks
@bot.command()
async def play(ctx):
    #set globals
    global song_array
    global current_song
    # grab the user who sent the command
    user = ctx.message.author
    # get user guild
    guild = ctx.message.guild
    channel = None
    for vc in guild.voice_channels:
        if vc.name == "Concert":
            channel = vc
            break
    if channel is None:
        channel = user.voice.voice_channel
    # try to connect
    try:
        vc = await channel.connect()
    except:
        vc = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    # play audio
    song_array = [
        random.choice(glob.glob(music_dir + "/*.mp3")),
        random.choice(glob.glob(music_dir + "/*.mp3")),
        random.choice(glob.glob(music_dir + "/*.mp3")),
        random.choice(glob.glob(music_dir + "/*.mp3")),
        random.choice(glob.glob(music_dir + "/*.mp3"))
    ]
    while vc.is_connected():
        # update songs
        current_song = song_array.pop(0)
        song_array.append(random.choice(glob.glob(music_dir + "/*.mp3")))
        # convert sound to audio data
        audio_source = discord.FFmpegPCMAudio(current_song)
        vc.play(audio_source, after=lambda e: print('done', e))
        while vc.is_playing():
            await asyncio.sleep(1)
        vc.stop()
    await vc.disconnect()

@bot.command()
async def reshuffle(ctx):
    global song_array
    song_array = [
        random.choice(glob.glob(music_dir + "/*.mp3")),
        random.choice(glob.glob(music_dir + "/*.mp3")),
        random.choice(glob.glob(music_dir + "/*.mp3")),
        random.choice(glob.glob(music_dir + "/*.mp3")),
        random.choice(glob.glob(music_dir + "/*.mp3"))
    ]

bot.run(os.getenv("DISCORD_BOT_TOKEN"))

