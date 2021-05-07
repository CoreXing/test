import discord,asyncio,os
from discord.ext import commands

bot = commands.Bot(case_insensitive=True,command_prefix='*')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle,activity=discord.Game(name="耍費中"))
    print('Logged in')
    print(bot.user.name)
    print(bot.user.id)
    print('-------------')

@bot.command()
async def load(ctx, extension):
    await ctx.send(f'load {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'unload {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'reload {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')


if __name__ == "__main__":
    bot.run('NzkxOTIzMTgxNDA5NDAyOTAx.X-WN7w.w0gzS7GXgMwyuFm2rS2wkBVDJLY')