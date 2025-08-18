import discord
from contra import gen_pass
from doble_carta import calcular 
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$RESPONDE'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$PASS'):
        await message.channel.send("ESTA ES TU COMTRASEÑA=    "+gen_pass(14))
    elif message.content.startswith('$calc'):
        expresion = message.content[len('$calc '):]  
        respuesta = calcular(expresion)
        await message.channel.send(respuesta)
    else:
        await message.channel.send(message.content)

client.run("token aqui")
