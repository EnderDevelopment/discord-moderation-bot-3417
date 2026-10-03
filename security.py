import discord
from discord.ext import commands

class Security(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.Cog.listener()
        async def on_message(self, message):
            if message.author.bot:
                return

                if 'badword' in message.content:
                    await message.delete()
                    await message.channel.send(f'{message.author.mention}, please watch your language.')

                    async def setup(bot):
                        await bot.add_cog(Security(bot))
