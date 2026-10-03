import discord
from discord.ext import commands

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def ticket(self, ctx):
            guild = ctx.guild
            category = discord.utils.get(guild.categories, name='Tickets')
            if not category:
                category = await guild.create_category('Tickets')

                channel = await guild.create_text_channel(f'ticket-{ctx.author.name}', category=category)
                await channel.set_permissions(ctx.guild.default_role, read_messages=False)
                await channel.set_permissions(ctx.author, read_messages=True)
                await ctx.send(f'Ticket created: {channel.mention}')

                async def setup(bot):
                    await bot.add_cog(Tickets(bot))
