import discord
from discord.ext import commands
from discord.ui import Button, View 
from mcstatus import JavaServer

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)


# Verifica
@bot.event
async def on_ready():
  print('System rebooted.')
  bot.add_view(Verification())

class Verification(discord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
  @discord.ui.button(label="Verifica",custom_id = "1267242135799988265",style = discord.ButtonStyle.success, emoji="<:approvato:1267785498278105099>")
  async def verify(self, interaction, button):
    role = 1258130335162699860
    user = interaction.user
    if role not in [y.id for y in user.roles]:
      await user.add_roles(user.guild.get_role(role))
      await user.send("Ti sei verificato!")

@bot.command()
async def Verifica(ctx):
  embed = discord.Embed(title = "Verifica", description = "Clicca qua giù per verificarti.")
  await ctx.send(embed = embed, view = Verification())

# Comando per visualizzare i giocatori online su Minecraft
@bot.command()
async def Server(ctx):
    server = JavaServer.lookup("server ip")
    status = server.status()
    if status.players.online > 0:
        player_names = ', '.join([player.name for player in status.players.sample])
        await ctx.send(f'Giocatori online: {status.players.online}\nNomi: {player_names}')
    else:
        await ctx.send('Nessun giocatore online al momento.')

# Avvia il bot
bot.run('token')
