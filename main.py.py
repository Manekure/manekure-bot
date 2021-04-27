import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix = "!", description = "Bot by 𝑨𝒊𝒅𝒆𝒏#0336")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def coucou(ctx):
	await ctx.send("Coucou !")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def test(ctx):
	await ctx.send("Test réussi !")
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
async def clear(ctx, nombre : int):
	messages = await ctx.channel.history(limit = nombre + 1).flatten()
	for message in messages:
		await message.delete()

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx,member : discord.Member):
	muted_role = ctx.guild.get_role(771681601473871883)

	await member.add_roles(muted_role)

	await ctx.send("{member.mention} a bien été mute.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
	mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

	await member.remove_roles(mutedRole)
	await ctx.send("L'utilisateur {member.mention} a bien été unmute.")
	await member.send(f"Tu est unmute du serveur {server.name}.")

bot.run("NzcwNzQ4NDI2MTgxOTM1MTM1.X5iFaA.btdjF2XfPeo6Gnk9rvZ54Vr-r6o")