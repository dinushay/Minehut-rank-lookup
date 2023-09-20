import requests
import nextcord
from nextcord.ext import commands

bot = commands.Bot()

@bot.slash_command(description="Queries the rank of a player on Minehut")
async def rank(interaction: nextcord.Interaction, playername: str):
    mojang_url = f"https://api.mojang.com/users/profiles/minecraft/{playername}"
    mojang_response = requests.get(mojang_url)
    if mojang_response.status_code == 200:
        mojang_data = mojang_response.json()
        uuid = mojang_data["id"]
        mcname = mojang_data["name"]
        uuid_with_dashes = f"{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}"
        minehut_url = f"https://api.minehut.com/cosmetics/profile/{uuid_with_dashes}"
        minehut_response = requests.get(minehut_url)
        if minehut_response.status_code == 200:
            minehut_data = minehut_response.json()
            rank = minehut_data["rank"]
            if rank == "DEFAULT":
                await interaction.response.send_message(f"`{mcname}` has not subscribed to a Minehut rank.", ephemeral=False)
            else:
                await interaction.response.send_message(f"The rank of `{mcname}` is `{rank}`.", ephemeral=False)
        else:
            await interaction.response.send_message(f"`{ncname}` has never joined Minehut.", ephemeral=False)
    else:
        await interaction.response.send_message(f"This player `{playername}` does not exist.", ephemeral=False)

@bot.slash_command(description="Queries the rank of a player on Minehut privately")
async def rank_private(interaction: nextcord.Interaction, playername: str):
    mojang_url = f"https://api.mojang.com/users/profiles/minecraft/{playername}"
    mojang_response = requests.get(mojang_url)
    if mojang_response.status_code == 200:
        mojang_data = mojang_response.json()
        uuid = mojang_data["id"]
        mcname = mojang_data["name"]
        uuid_with_dashes = f"{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}"
        minehut_url = f"https://api.minehut.com/cosmetics/profile/{uuid_with_dashes}"
        minehut_response = requests.get(minehut_url)
        if minehut_response.status_code == 200:
            minehut_data = minehut_response.json()
            rank = minehut_data["rank"]
            if rank == "DEFAULT":
                await interaction.response.send_message(f"`{mcname}` has not subscribed to a Minehut rank.", ephemeral=True)
            else:
                await interaction.response.send_message(f"The rank of `{mcname}` is `{rank}`.", ephemeral=True)
        else:
            await interaction.response.send_message(f"`{mcname}` has never joined Minehut.", ephemeral=True)
    else:
        await interaction.response.send_message(f"This player `{playername}` does not exist.", ephemeral=True)


bot.run("DISCORDTOKEN")
