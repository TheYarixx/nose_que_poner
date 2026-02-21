import discord, random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(m):
    if m.author == client.user: return

    if m.content == "$hello":
        await m.channel.send("Hi!")

    elif m.content == "$bye":
        await m.channel.send("🙂")

    elif m.content == "$coin":
        await m.channel.send(random.choice(["Cara 🪙", "Cruz 🪙"]))

    elif m.content == "$emoji":
        await m.channel.send(random.choice(["🔥","😎","🚀","🤖"]))

    elif m.content == "$help":
        await m.channel.send(
            "📌 Comandos disponibles:\n"
            "$hello - Saludo\n"
            "$bye - Despedida\n"
            "$coin - Lanza una moneda\n"
            "$emoji - Emoji aleatorio\n"
            "$help - Muestra esta lista"
        )

client.run("X")