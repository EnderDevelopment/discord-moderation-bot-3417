import discord
from discord.ext import commands

class WelcomeGoodbye(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.Cog.listener()
        async def on_member_join(self, member):
            channel = discord.utils.get(member.guild.text_channels, name='welcome')
            if channel:
                await channel.send(f'Welcome {member.mention} to the server!')

                @commands.Cog.listener()
                async def on_member_remove(self, member):
                    channel = discord.utils.get(member.guild.text_channels, name='goodbye')
                    if channel:
                        await channel.send(f'Goodbye {member.mention}!')

                        async def setup(bot):
                            await bot.add_cog(WelcomeGoodbye(bot))
