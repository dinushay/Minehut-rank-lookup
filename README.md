# Minehut rank lookup
A Discord bot that queries the rank of a player on Minehut using the Mojang API and the Minehut API. Supports slash commands. Written in Python using the nextcord library.

## Commands

`/rank` - Check a player's Minehut rank.

`/rank_private` - Check a player's Minehut rank privately. 

## Invite the bot

[Click here to invite the bot to your server.](https://discord.com/oauth2/authorize?client_id=1152580494790246441&scope=bot&permissions=1024)

## Installation (Create your own bot)

1. Clone this repository
```bash
git clone https://github.com/dinunuggets/Minehut-rank-lookup.git
```
2. Install the dependencies
```bash
python3 -m pip install -U nextcord
python3 -m pip install -U requests
```
3. [Create a Discord bot](https://discord.com/developers/) and copy the token.

4. Replace `bot.run("DISCORDTOKEN")` at bot.py on the last line with your real bot token

5. Start the Bot
```bash
python3 bot.py
```
6. Invite your Bot here: https://discordapi.com/permissions.html

## Demo

![image](https://github.com/DinuNuggets/Minehut-rank-lookup/assets/61915816/f85985c6-519c-4237-a222-f2453fa9f29c)
