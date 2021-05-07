import discord
import json
from discord.ext import commands
from random import randint
from core.classes import cog_Extention
jdata = {}
with open("data.json", "r") as file:
    jdata = json.load(file)

on=[]

class 音樂(cog_Extention):
    @commands.command(name='say')
    async def play_(self, ctx, *, search: str):
        await ctx.message.delete()
        await ctx.send(search)

    @commands.command(name='hurt', aliases=['h', '嘴砲'])
    async def hurt_(self, ctx):
        global on
        await ctx.message.delete()
        if ctx.message.channel in on:
            await ctx.send(f"---------------------\n乖啦~停戰囉OwO")
            on.remove(ctx.message.channel)
        else:
            await ctx.send(f"---------------------\n來啊 來嘴砲啊")
            on.append(ctx.message.channel)

    @commands.Cog.listener()
    async def on_reaction_add(self, react, our):
        chan = self.bot.get_channel(react.message.channel.id)
        if (react.message.author.bot):
            await chan.send(f"<@{our.id}>按三小")

    @commands.Cog.listener()
    async def on_message_delete(self, mess):
        chan = self.bot.get_channel(mess.channel.id)
        a=('*','-')
        if (not (mess.content.startswith(a))):
            if (not (mess.author.bot)):
                await chan.send(f"ㄍ 偷刪仔")

    @commands.Cog.listener()
    async def on_message(self, mess):
        global on
        chan = self.bot.get_channel(mess.channel.id)
        if not (mess.author.bot):
            if ('早安' in mess.content):
                await chan.send(f"<@{mess.author.id}>早ㄤ~")
            if (mess.channel in on) and (not (mess.content.startswith('*'))):
                if ('ㄏㄚˋ' in mess.content):
                    await chan.send(f"<@{mess.author.id}> {jdata['haha'][randint(0,len(jdata['haha'])-1)]}")
                else:
                    await chan.send(f"<@{mess.author.id}> {jdata['sosad'][randint(0,len(jdata['sosad'])-1)]}")


def setup(bot):
    bot.add_cog(音樂(bot))
