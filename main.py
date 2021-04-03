import time
Tstart = time.time()
import datetime
StartHour = datetime.datetime.now()
import discord
from discord.ext import commands
import os
Timp = time.time()

def log(text):
	file = open("logs/latest.txt", "a")
	T = datetime.datetime.now().isoformat().replace("T", " ")
	text = "[{0}]   {1} \n".format(T, str(text))
	file.write(text)
	file.close()

def SaveLatestlog():
	latest = open("logs/latest.txt", "r")
	content = latest.read()
	name = "logs/{0}.txt".format(content[0:26])
	log = open(name, "w")
	log.write(content)
	log.close()
	latest.close()


pre = "?"
token = os.environ.get("DISCORD_BOT_SECRET")
bot = commands.Bot(command_prefix = pre)
game = discord.Game(status=discord.Status.dnd, name=pre+"a")
SaveLatestlog()
StartHour = StartHour.isoformat().replace("T", " ") + "\n"
startlog = open("logs/latest.txt", "w")
startlog.write(StartHour)
startlog.close()


Tpy = time.time()

@bot.event
async def on_ready():
	await bot.change_presence(activity = game)
	print("logged in as : {0} \nid : {1}".format(bot.user.name, bot.user.id))
	tolog = "logged in as : {0} \nid : {1}".format(bot.user.name, bot.user.id)
	log(tolog)
	Tdone = time.time()
	print("Bot ready for combat")
	print("Done in {0} seconds \nTime to import : {1} seconds \nTime to setup python : {2} seconds\nTime to start bot : {3} seconds".format(Tdone - Tstart, Timp - Tstart, Tpy - Timp, Tdone - Tpy))

@bot.command()
async def a(ctx):
	msg = await ctx.channel.history(limit=1).flatten()
	await msg[0].delete()
	await ctx.send("https://tenor.com/view/gawr-gura-gura-gawr-holomyth-hololiveen-wink-gif-18669368")

@bot.command()  
async def nice(ctx):
	msg = await ctx.channel.history(limit=1).flatten()
	await msg[0].delete()
	await ctx.send("https://cdn.discordapp.com/attachments/721692590566670398/826863447865426000/NiCe.gif")

@bot.command()
async def repeatn(ctx, nb, *msg):
	test = False
	try:
		nb = int(nb)
		test = True
	except:
		await ctx.send("Fais __**!help**__ pour apprendre à utiliser les commandes".format(pre))
	if test:
		for i in range(nb):
			await ctx.send(" ".join(msg))

@bot.command()
async def repeat(ctx, *msg):
	await ctx.send(" ".join(msg))

@bot.command()
async def obfuscate(ctx, *msg : str):
	obChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
	obText = ""
	for word in msg:
		for char in word:
			if char.isalpha():
				if ord(char) < 91:
					obText += obChar[ord(char)-65]
				else:
					obText += obChar[ord(char)-97]
			else:
				obText += char
		obText += "   "
	await ctx.send(obText)

@bot.command()
async def clear(ctx, nb : int=1):
	messages = await ctx.channel.history(limit = nb + 1).flatten()
	for msg in messages:
		await msg.delete()

@bot.command()
async def spam(ctx):
	await ctx.send("Qui voulez vous spammer ?")

	def check(message):
		msg = message.content
		if msg[0] == "<" and msg[1] == "@" and msg[-1] == ">" :
			test = True
		return message.author == ctx.message.author and ctx.message.channel == message.channel and test
	
	answer = await bot.wait_for("message", check = check)
	tospam = answer.content
	msg = await ctx.send(f"Voulez vous vraiment spammer {tospam} ?")
	await msg.add_reaction("✅")
	await msg.add_reaction("❌")

	def check(reaction, user):
		return ctx.message.author == user and msg.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")
	
	reaction, user = await bot.wait_for("reaction_add", check = check)
	if reaction.emoji == "❌":
		await ctx.send("C'est bien, bon retout du côté de la lumière.")
	else:
		await ctx.send("Okay Master !")
		for i in range (10):
			await ctx.send(f"{tospam}, {answer.author} te spamme !")

@bot.command()
async def help(ctx):
	await ctx.send("Désolé, cette commande ne fait pour l'instant rien")



bot.run(token)