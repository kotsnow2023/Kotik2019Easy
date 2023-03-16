import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())

@bot.slash_command()
async def kotik(interaction: disnake.AppCmdInter):
  await interaction.send("Котик крутой")

bot.run("MTA4NTY4NjE2Njk5NDU2NzI4OQ.GcTNhE.ZbmEsCobmwmp_b0pA9ReL8O-VqNSNimwS3IDx0")