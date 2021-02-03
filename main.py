import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions, has_role
import random


bot = commands.Bot(command_prefix='! ')
#set command_prefix to your prefix
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def ping(ctx):
  await ctx.send("pong")

@bot.command()
async def eightball(ctx, question: str = None):

        responses = [
            "As I see it, yes.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don’t count on it.",
            "It is certain.",
            "It is decidedly so.",
            "Most likely.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Outlook good.",
            "Reply hazy, try again.",
            "Signs point to yes.",
            "Very doubtful.",
            "Without a doubt.",
            "Yes.",
            "Yes – definitely.",
            "You may rely on it."
        ]
        if question is None:
            await ctx.send("Please ask me a question.")
            return
        result = random.choice(responses)
        await ctx.send('Let me see...')
        await ctx.trigger_typing()
        await asyncio.sleep(2)
        await ctx.send(result)
        
@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	channel = await member.create_dm()
	embed=discord.Embed(title=f"Banned", description=f"You have been banned from {guild.name}.")
	embed.add_field(name=f"Reason:", value=f"{reason}", inline=False)
	embed.add_field(name=f"Banned By:", value=f"{ctx.message.author}", inline=False)
	await channel.send(embed=embed)
	await member.ban(reason=reason)
	embed = discord.Embed(title="Ban", description="Member Successfully Banned.")
	await ctx.send(embed=embed)

#mass delete messages
@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def purge(ctx, limit: int):
	await ctx.channel.purge(limit=1)
	await ctx.channel.purge(limit=limit)
	await ctx.send('Cleared by {}'.format(ctx.author.mention))
	await asyncio.sleep(2)
	await ctx.channel.purge(limit=1)

#mute (adds mute role)
@bot.command()
@has_permissions(manage_messages=True)
async def mute(ctx, user:discord.Member, reason = None):
	role = discord.utils.get(ctx.guild.roles, name="Muted")

   await user.add_roles(role)
	embed = discord.Embed(title="Muted", description=f"{user.mention} was muted.")
	await ctx.send(embed=embed)

#unmute (rmeoves mute role
@bot.command()
@has_permissions(manage_messages=True)
async def unmute(ctx, user:discord.Member, reason = None):
	role = discord.utils.get(ctx.guild.roles, name="Muted")

    await user.remove_roles(role)
	embed = discord.Embed(title="Unmuted", description=f"{user.mention} was unmuted.")

	await ctx.send(embed=embed)

#sets slowmode time using channel edit
@bot.command()
async def slowmode(ctx, seconds :int):
	if seconds >= 21600:
		return await ctx.send(f"{ctx.author.mention} '21600' is the max slowmode you can have.")
	await ctx.channel.edit(slowmode_delay=seconds)
	embed=discord.Embed(title=f"Slowmode set to {seconds}", description=f"Slowmode has changed to {seconds}.", color=0xbfbfbf)

    await ctx.send(embed=embed)


bot.run('TOKEN')
#set token to the token you stored in Step 1.
