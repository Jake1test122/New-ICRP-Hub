import os,json,discord
from discord.ext import commands
TOKEN=os.getenv("MTU1Mzk5NTk1MzUwNDI1NjA0MA.G9ReUC.QrLw-IVSPoI9FladahTcpYBWKSulnGGR7GeBU4")
intents=discord.Intents.default(); intents.guilds=True
bot=commands.Bot(command_prefix="!",intents=intents)
with open("hub_structure.json",encoding="utf-8") as f: CFG=json.load(f)

@bot.event
async def on_ready(): print(f"ICRP Hub ready as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_hub(ctx):
    g=ctx.guild
    msg=await ctx.send("Building ICRP Hub...")
    have={r.name for r in g.roles}
    for name in CFG["roles"]:
        if name not in have: await g.create_role(name=name[:100],reason="ICRP Hub setup")
    cm={c.name:c for c in g.categories}
    for cn,items in CFG["categories"].items():
        cat=cm.get(cn) or await g.create_category(cn[:100],reason="ICRP Hub setup")
        existing={c.name for c in cat.channels}
        for x in items:
            if x["name"] in existing: continue
            if x["type"]=="voice": await g.create_voice_channel(x["name"][:100],category=cat)
            else: await g.create_text_channel(x["name"][:100],category=cat)
    await msg.edit(content="✅ ICRP Hub created. Review permissions before use.")

if not TOKEN: raise RuntimeError("Put DISCORD_TOKEN in Replit Secrets.")
bot.run(TOKEN)
