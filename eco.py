import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"Hai fatto l'accesso come {bot.user}")

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def plastica(ctx):
    await ctx.send("Riduci la quantità di plastica utilizzata a casa")

@bot.command()
async def Greta_Thunberg(ctx):
    await ctx.send("Greta Thunberg ha iniziato i suoi scioperi dalla scuola per il clima a 15 anni. Greta ha inspirato più di un milione e seicentomila giovani a combattere contro la salvaguardia del clima")

@bot.command()
async def busta_riutilizzabile(ctx):
    await ctx.send("Il consiglio di usare buste per la spesa riutilizzabili è a dir poco scontato. Usare la busta riutilizzabile fa si che tu risparmi soldi, ma allo stesso tempo aiuti il pianeta.")

@bot.command()
async def riduci_il_consumo_di_carta(ctx):
    await ctx.send("In questa nostra epoca digitalizzata è facilissimo ridurre il consumo di carta: scontrini e fatture elettroniche, e-book e servizi digitali consentono di limitare concretamente lo spreco di carta e, di conseguenza, di ridurre anche la produzione di rifiuti.")

bot.run("TOKEN")
