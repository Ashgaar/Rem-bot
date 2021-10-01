import discord
import coinflip
import os
from dotenv import load_dotenv
import rollDie


load_dotenv()

TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')
current_status = discord.Game('¤help for commands')


intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=current_status)
    
    print(f'{client.user} has connected to discord. \n')
    
    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break
        
    # print(
    #     f'{client.user} is connected to the following server: \n'
    #     f'{guild.name} (id: {guild.id})\n'
    # )
    
    # print('Server members:')    
    # for i in guild.members:
    #     print (i)
        
    print('\nReady to execute commands \n')


    
@client.event
async def on_message(message):
    channel = message.channel
    
    if message.content.startswith('¤sayhello'):
        await channel.send('Say hello!')
        def check(m):
            return m.content == 'hello' and m.channel == channel
        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}'.format(msg))
    elif message.content.startswith('¤help'):
        print('Executing help command')
        await message.author.send('Use the prefix: ¤. Example: ¤sayhello \n - sayhello: respond with hello to get a greeting. \n - coinflip: flips a coin and returns the value. \n - ayaya: AYAYA. \n - corruptedvor: corrupted vor monologue. \n - ')
    elif message.content.startswith('¤coinflip'):
        print('Executing coinflip command')
        coinflip_result = coinflip.main()
        await channel.send(f'Result is {coinflip_result}')
    elif message.content.startswith('¤ayaya'):
        print('Executing ayaya command')
        await channel.send('<:ayaya:848476133849694259>')
    elif message.content.startswith('¤corruptedvor'):
        print('Executing corruptedvor command')
        await channel.send(f"Look at them, they come to this place when they know they are not pure. Tenno use the keys, but they are mere trespassers. Only I, Vor, know the true power of the Void. I was cut in half, destroyed, but through it's Janus Key, the Void called to me. It brought me here and here I was reborn. We cannot blame these creatures, they are being led by a false prophet, an impostor who knows not the secrets of the Void. Behold the Tenno, come to scavenge and desecrate this sacred realm. My brothers, did I not tell of this day? Did I not prophesize this moment? Now, I will stop them. Now I am changed, reborn through the energy of the Janus Key. Forever bound to the Void. Let it be known, if the Tenno want true salvation, they will lay down their arms, and wait for the baptism of my Janus key. It is time. I will teach these trespassers the redemptive power of my Janus key. They will learn it's simple truth. The Tenno are lost, and they will resist. But I, Vor, will cleanse this place of their impurity.")
    elif message.content.startswith('¤rolladie'):
        diceRoll_result = rollDie.main()
        await channel.send(f'Result of dice roll is {diceRoll_result}')
            

client.run(TOKEN)