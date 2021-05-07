import discord
from discord.ext import commands

class cog_Extention(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.players = {}