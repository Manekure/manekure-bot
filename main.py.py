import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix = "s!", description = "Bot by LoAiden™#0001")
bot.remove_command('help')

@bot.event
async def on_ready():
    activity = discord.Game(name="Regarde | s!help !", type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")

@bot.command()
async def coucou(ctx):
	await ctx.send("Coucou !")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def test(ctx):
	await ctx.send("Test en cours...")
	import time
	time.sleep(5)
	await ctx.send("Récupération...")
	import time
	time.sleep(2)
	await ctx.send("Réussi avec succès (34 ticks/s)!")
	print("Teste effectué, réussi !")
	
@bot.command()
async def aide(ctx):
	await ctx.send("Si vous avez besoin d'aide, suivez les instructions suivante: Allez prévenir le STAFF pour qu'ils puissent vous aidez.")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send (f"{user} à été ban pour la raison suivante : {reason}.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send (f"{user} à été unban.")
			return
	await ctx.send("L'utilisateur {user} n'est pas dans la liste des bans.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send (f"{user} à été kick.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
    role_members = discord.utils.get(ctx.guild.roles, name='Followers')
    role_muted = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles('Muted')
    await ctx.send("User Was Muted")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    await member.remove_roles(Muted)

@bot.command()
@commands.has_permissions(manage_channels = True)
async def lockchannel(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send( ctx.channel.mention + "Salon verouiller.")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlockchannel(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + "Salon déverouiller.")

@bot.command()
async def hug(ctx, user : discord.User):
	author_name = ctx.message.author.name
	embedhug =discord.Embed(title="", description= (""), color=749198)
	embedhug.add_field(name="Hug", value=(f"{user} est câliner."))
	import io
	liste = ["https://cdn.discordapp.com/attachments/866056620085870612/872902036469973042/tenor_1.gif", "https://cdn.discordapp.com/attachments/866056620085870612/872902070393516072/tenor.gif"]
	url = random.randint(liste)
	await ctx.send(embed=embedhug)
... (18 lignes restantes)
