from discord.ext import commands
from Database.db import getDB
from discord import Embed

class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.users = getDB('users')

    @commands.command(aliases=['bal'])
    async def balance(self, ctx, user=None):
        if not user:
            user = ctx.author
        else:
            user = self.bot.get_user(int(user.replace('<@', '').replace('>', '')))
        
        userInfo = self.users.get({'_id': user.id})
        if not userInfo:
            await ctx.send('User not found')
            return

        embed = Embed(title=None, description=None, color=0x800080)
        embed.set_author(name=f"{user.name}'s Balance", icon_url=user.avatar.url)
        embed.add_field(name="Cash", value=f"${userInfo['cash']}", inline=False)
        embed.add_field(name="Bank", value=f"${userInfo['bank']}", inline=False)
        embed.add_field(name="Total", value=f"${userInfo['cash']+userInfo['bank']}", inline=False)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Economy(bot))
