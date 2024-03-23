from discord.ext import commands
from Database.db import getDB
from discord import User

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.users = getDB('users')

    @commands.Cog.listener()
    async def on_member_join(self, member: User):
        channel = member.guild.system_channel
        if channel is not None and not member.bot:
            self.users.create({
                'id': member.id,
                'cash': 200,
                'bank': 0
            })


async def setup(bot):
    await bot.add_cog(Welcome(bot))
