import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())

@bot.slash_command()
async def kotik(interaction: disnake.AppCmdInter):
  await interaction.send("Котик крутой")

bot.run()
