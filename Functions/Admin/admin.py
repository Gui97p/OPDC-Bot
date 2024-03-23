from discord.ext import commands
from Database.db import getDB

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.users = getDB('users')

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def addData(self, ctx, data: str):
        doc = {}
        itens = data.split(',')
        for item in itens:
            item = item.split(':')
            if 'int' in item[1]:
                item[1] = item[1].replace('int', '')
                item[1] = int(item[1])
            
            doc[item[0]] = item[1]
        
        
        log, e  = self.users.create(doc)
        if log == True:
            await ctx.send(f'*Data created successfully!*\n> ***__Info:__***\n\n```\n{doc}\n```')
        else:
            await ctx.send(f'*Error on adding Data:*\n\n> **Error Data** -> __***{e}***__')


async def setup(bot):
    await bot.add_cog(Admin(bot))
