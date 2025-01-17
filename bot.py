import discord
import os
from discord.ext import commands
import random
from animales import *

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Junta dos numeros."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Lanzar un dado."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('El formato necesita ser NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='Elegir una de tus opciones de otra manera.')
async def choose(ctx, *choices: str):
    """Elige entre multiples opciones."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repitiendo...'):
    """Repite un mensajes multiples veces."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Dice cuando un miembro se unio."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command('animal')
async def duck(ctx):
    '''Una vez que llamamos al comando animal, 
    el programa llama a una funcion para que genere una imagen de un animal'''
    x = random.randint(1,2)
    if x == 1:
        image_url = get_duck_image_url()
    elif x == 2:
        image_url = get_dog_image_url()
    await ctx.send(image_url)
@bot.group()
async def cool(ctx):
    """Dice si un usuario es genial.

    En realidad solo revisa si un subcomando esta siendo invocado.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} no es genial')


@cool.command(name='bot')
async def _bot(ctx):
    """El bot es genial?"""
    await ctx.send('Si, el bot es genial.')

bot.run("TOKEN")
