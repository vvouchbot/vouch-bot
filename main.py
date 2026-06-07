import discord
from discord.ext import commands
from dsicord import app_commands
import json
import os
from datetime import datetime

TOKEN = os.getenv ("DISCORD_TOKEN")

intents = discord.intents.default()
bot = commands.bot(command_prefix="!",intents=intents)

DATA_FILE = "vouches.json"

if not os.path exists(DATA_FILE) with open(DATA_FILE,"w") as f: 
  "last_id":0},f)

def load_data():
  with open(DATA_FILE,"r") as f:
    return json.load(f)

def save_data(data):
  with open(DATA_FILE, "w") as f:
    json.dump(data, f, indent=4)

@bot.event
async def on_ready():
  await bot.tree_sync()
  print(f"Logged in as {bot.user}")

  @bot.tree command(name="vouch",
                    description="Leave a vouch")
  @app_commands.describe(user="User to vouch", comment="Your review")
  async def vouch(interaction:discord.interaction, user:discord member,comment: str):

    if user.id==interaction.user.id:
      await
      interaction.response.send_message("❌ You cant vouch for yourself.",
                                        ephemeral=True)
      return
      data= load_data()
      uid = str(user.id)
      if uid not in data["vouches"]:
        data["vouches"][uid]= 0

data["vouches"][uid] += 1
data ["last_id"] += 1

save_data(data)

embed= discord.Embed(title="New vouch received",color= 0x3498db)

embed_set_thumbnail(url=interaction.user.display_avatar.url)

embed.add_field(name="From",

                value=f"{interaction.user.mention}
                \n({interaction.user,id})",
                inline=False)

embed add_Field(name="vouched user",
                value=user.mention,
                inline= False)

embed add_field(name="rating",
                value="⭐⭐⭐⭐⭐(5/5)",
                inline= False)

embed.add_field(name="vouched at",
                value=datatime.now().strftime("%B %d,%Y %I: %M %p"),
                                              inline=False)
embed.add_field(name="vouch ID",
                value=str(data["last_id"]),
                inline=False)

embed.set_footer(text="Thanks for purchasing our product!")

await
interaction.response.send_message(embed=embed)
                                              
                                          
