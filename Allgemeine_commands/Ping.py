import discord
from discord.ext import commands
import asyncio


class PingCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.message.delete()
        p = discord.Embed(title='**PING**', description=f'**{round(self.client.latency * 1000)}** ms!', color=0x060baa)
        p.set_thumbnail(
            url='https://i.ibb.co/5Bt2bM9/Neon-Photo-Editor-20200706-144711323.jpg')
        p.set_footer(text=ctx.author.name)
        await ctx.send(embed=p)


def setup(client):
    client.add_cog(PingCommand(client))
