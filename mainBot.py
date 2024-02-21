import discord, random, requests, os
from discord.ext import commands
from bot_logic import coins, gen_pass
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def flipkoin(ctx, detik=1):
    await ctx.send(coins(detik))

@bot.command()
async def createpass(ctx):
    await ctx.send(gen_pass(8))

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def ide_sampah(ctx):
    img_name = random.choice(os.listdir('kerajinan'))
    with open(f'kerajinan/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            await file.save(f'./{file.filename}')
            await ctx.send(f'FILE BERHASIL DISIMPAN DENGAN NAMA {file.filename}')
            hasil = get_class('keras_model.h5', 'labels.txt', file.filename)

            if hasil[0] == "Merpati\n" and hasil [1] >= 0.7:
                await ctx.send('INI ADALAH BURUNG MERPATI')
                await ctx.send('Burung ini memakan beras')
                await ctx.send('Persentase kemiripan {:,.1f}%'.format(hasil[1]*100))
            elif hasil[0] == "Pipit\n" and hasil [1] >= 0.7:
                await ctx.send('INI ADALAH BURUNG PIPIT')
                await ctx.send('Burung ini memakan kacang')
                await ctx.send('Persentase kemiripan {:,.1f}%'.format(hasil[1]*100))
            elif hasil[0] == "Perkutut\n" and hasil [1] >= 0.7:
                await ctx.send('INI ADALAH BURUNG PERKUTUT')
                await ctx.send('Burung ini memakan padi-padian')
                await ctx.send('Persentase kemiripan {:,.1f}%'.format(hasil[1]*100))
            else:
                await ctx.send('GAMBAR TIDAK TERDETEKSI')
    else:
        await ctx.send('ANDA LUPA MENGIRIM GAMBAR!')


bot.run("TOKEN")

