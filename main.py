import random
import discord
import random
from discord import channel
from discord.enums import MessageType
import praw
from random import choice
from discord.ext import commands
import urllib.parse, urllib.request, re
import redditstuff

bot = commands.Bot(command_prefix='$')
reddit = praw.Reddit(client_id=redditstuff.client_id,
                     client_secret=redditstuff.client_secret,
                     username=redditstuff.username,
                     password=redditstuff.password,
                     user_agent=redditstuff.user_agent)


class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('with my nervs'))
    print('We have logged in as {0.user}'.format(bot))
    print('bot is now working lol')


@bot.command()
async def ping(ctx):
    await ctx.send(f"deez nutz {round(bot.latency * 1000)}ms")


@bot.command()
async def test(ctx):
    await ctx.send('yes i work UwU')


@bot.command(aliases=['imsad'])
async def hug(ctx):
    await ctx.send('i will hug you back bec i love you and i am at gun point')


@bot.command(aliases=['son', 'are you wining son'])
async def areyouwinningson(ctx):
    await ctx.send('no dad im depressed and nothing makes me happy anymore')


@bot.command()
async def kill(ctx):
    await ctx.send('bang bang :gun: , now ur dead')


@bot.command(aliases=['friend'])
async def friendzone(ctx):
    await ctx.send('https://www.youtube.com/watch?v=p37_Ux1G_BI%27')


@bot.command(aliases=['aids'])
async def std(ctx):
    await ctx.send('https://www.youtube.com/watch?v=uukvEcd25oQ&feature=youtu.be')


@bot.command(aliases=['kys', 'kill yourself'])
async def killyourself(ctx):
    await ctx.send('https://www.youtube.com/watch?v=2dbR2JZmlWo')


@bot.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    top = subreddit.top(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)



@bot.command()
async def dank(ctx):
    subreddit = reddit.subreddit("dankmemes")
    all_subs = []
    top = subreddit.top(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)


@bot.command()
async def animeme(ctx):
    subreddit = reddit.subreddit("goodanimemes")
    all_subs = []
    top = subreddit.top(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)


@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))


@bot. command(aliases=['command', 'bot command'])
async def commands(ctx):
    await ctx.send ('slap\nkys\nmeme\ndank\nanimeme\naids\nfriendzone\nping\ntest\nhug\nareyouwiningson\nkill\nimsad\nbtw when running a command be sure to write $ before')
@bot.command()
async def repeat(ctx, arg):
    if arg == ("i'm retarded"):
       await ctx.send("yes we know")
    else:
        await ctx.send(arg)


nword = ('mrs obama get down' , 'they is going to say the n-word' , 'you rasic scum i will cancel you on twitter','thats a hard R now you are getting out of hand buddy')

@bot.event
async def on_message(message):
    if message.content.startswith('nigger'):
        await message.channel.send(random.choice(nword))
        await bot.process_commands(message)

    if message.author.bot:
        return
    await bot.process_commands(message)


@bot.command(aliases=['u gay', 'why are you named fembot' ,'femboi'])
async def fembot(ctx):
    await ctx.send ('yes iam a femboi and iam tried of being oppresed FEMBOIS RISE UP')

@bot.command(aliases=['makers' , 'creators' , 'devs' ])
async def developers(ctx):
    await ctx.send ('im developed by diana and maazaki')

@bot.command(aliases=['lemon' , 'lime'])
async def lemonade(ctx):
    await ctx.send ('https://www.youtube.com/watch?v=yK1JRtoBY3Y')

Ballchoice = ('As I see it, yes.' , 'Ask again later.' , 'Better not tell you now.' ,'Cannot predict now.' , 'Concentrate and ask again.' , 'Don???t count on it.' , 'It is certain.' , 'It is decidedly so.' , 'My reply is no.' , 'My sources say no.' , 'Outlook not so good.' , 'Outlook good.' , 'Reply hazy, try again.' , 'Signs point to yes.' , 'Very doubtful.' , 'Without a doubt.' , 'Yes.' , 'Yes ??? definitely.')

@bot.command(aliases=['help 8 ball','8ball'])
async def ballcommands(ctx):
    await ctx.send (' As I see it, yes.\nAsk again later.\nBetter not tell you now.\nCannot predict now.\nConcentrate and ask again.\nDon???t count on it.\nIt is certain.\nIt is decidedly so.\nMost likely.\nMy reply is no.\nMy sources say no.\nOutlook not so good.\nOutlook good.\nReply hazy, try again.\nSigns point to yes.\nVery doubtful.\nWithout a doubt.\nYes.\nYes ??? definitely.\nYou may rely on it.')
@bot.command(aliases=['choice'])
async def ballc(ctx):
    await ctx.send(random.choice(Ballchoice))

throw = (1 , 2 , 3 , 4 , 5 , 6)

@bot.command(aliases=['throw a die','dice' ])
async def die(ctx):
    await ctx.send(random.choice(throw))

#you can change the file directory nased one the place of the text files
#i have mine at my D directory and I named the folder "discord_bot storage"
#the ranndom choice works beacuse i have the quotes like these '' or "" if they aren't there it wouldn't be considered a value each and would just print the whole text file
#example "songslink"
#         "another song link"
#so it is considered an another value
#an easy way to get the file location is just to copy the file explorer path then \yourtxtfile 

randomaritsts = ('fairouz' , 'eminem' , 'Mac miller' , 'mac demarco' , 'Adele' , 'Childish gambino' ,'Freddie dredd' ,'ghostmane' ,'Alec Benjamin' ,'hozier','Joji','Juice wrld','sub urban','um kulthoum')

@bot.command(aliases=['artist' 'random singer'])
async def randomartist(ctx):
    await ctx.send(random.choice(randomaritsts))



@bot.command(aliases=['Mac demarco','Mac Demarco'])
async def macdemarco(ctx):
    await ctx.send((random.choice(list(open('D:\discord_bot storage\Mac_demarco.txt')))))



@bot.command(aliases=['filthyfrank'])
async def joji(ctx):
    await ctx.send((random.choice(list(open('D:\discord_bot storage\Joji.txt')))))

@bot.command()
async def adele(ctx):
    await ctx.send((random.choice(list(open('D:\discord_bot storage\Adele.txt')))))


@bot.command(aliases=['childish gambino'])
async def childishgambino(ctx):
    await ctx.send((random.choice(list(open('D:\discord_bot storage\childish_gambino.txt')))))

@bot.command()
async def eminem(ctx):
    await ctx.send((random.choice(list(open(r'eminem.txt')))))

@bot.command(aliases=['Freddie dredd'])
async def Freddiedredd(ctx):
    await ctx.send((random.choice(list(open('D:\discord_bot storage\Freddie_dredd.txt')))))

@bot.command()
async def fyrooz(ctx):
    await ctx.send((random.choice(list(open('D:\discord_bot storage\Fyrooz.txt')))))

@bot.command(aliases=['ghoste mane'])
async def ghostmane(ctx):
    await ctx.send((random.choice(list(open('D:\discord_bot storage\ghostmane.txt')))))

@bot.command()
async def hozier(ctx):
    await ctx.send((random.choice(list(open('D:\discord_bot storage\hozier.txt')))))

@bot.command(aliases=['Juice wrld'])
async def Juicewrld(ctx):
    await ctx.send((random.choice(list(open('D:\discord_bot storage\Juice_wrld.txt')))))


@bot.command()
async def Random(ctx):
    await ctx.send((random.choice(list(open('D:\discord_bot storage\Random.txt')))))

@bot.command(aliases=['sub urban'])
async def suburban(ctx):
    await ctx.send((random.choice(list(open('D:\discord_bot storage\sub_urban.txt')))))


@bot.command(aliases=['um kulthoum'])
async def umkulthoum(ctx):
    await ctx.send((random.choice(list(open(r'D:\discord_bot storage\Um_kulthoum.txt')))))


bot.run("your token")
