import discord
from discord.ext import commands

class InviteTracking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.invites = {}

        @commands.Cog.listener()
        async def on_ready(self):
            for guild in self.bot.guilds:
                self.invites[guild.id] = await guild.invites()

                @commands.Cog.listener()
                async def on_member_join(self, member):
                    invites_before = self.invites[member.guild.id]
                    invites_after = await member.guild.invites()

                    for invite in invites_before:
                        if invite.uses < [i for i in invites_after if i.code == invite.code][0].uses:
                            await member.send(f'You joined using the invite: {invite.code}')
                            break

                            self.invites[member.guild.id] = invites_after

                            async def setup(bot):
                                await bot.add_cog(InviteTracking(bot))
