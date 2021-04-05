import discord
import os
import random
randomcurrent = False
guesses = 0
number = 1
client = discord.Client()
@client.event
async def on_ready():
  print("ready-user:{0.user}".format(client))
@client.event
async def on_message(mes):
  global number
  global guesses
  inte = []
  for j in range(1000):
    inte.append(j+1)
  global randomcurrent
  if mes.author == client.user:
    return
  qas=[]
  qadd=[]
  qu = ""
  an = ""
  beforetilda = True
  questxt = open("qa's.txt", "r")
  for o in range(len(questxt.readlines())):
    questxt.close()
    questxt = open("qa's.txt", "r")
    for p in questxt.readlines()[o]:
      if p == "~":
        beforetilda = False
        continue
        print('tilda')
      if beforetilda == True:
        qu += p
      if beforetilda == False:
        an += p
    qadd.append(qu)
    qadd.append(an)
    qas.append(qadd)
    qadd = []
    an = ""
    qu = ""
    questxt.close()
    questxt = open("qa's.txt", "r")
    beforetilda = True
  if mes.content[0] == "'":
    print("activated")
    message = ""
    for k in range(len(mes.content)):
      if mes.content[k] == "'":
        continue
      else:
        message += str(mes.content[k])
    print(message.lower())
    for a in range(len(qas)):
      if message.lower() == qas[a][0]:
        await mes.channel.send(qas[a][1])
    if message.lower() == "random" and randomcurrent == False:
      guesses = 0
      number = random.randint(1, 1000)
      await mes.channel.send("Number has been created please guess")
      randomcurrent = True
    if message.lower() == "quit" and randomcurrent == True:
      randomcurrent = False
      await mes.channel.send("quit.")
      guesses = 0
    if message.lower() == "dmme":
      await mes.author.send("ok")
    thingy = False
    if randomcurrent == True:
      for u in inte:
        if message == str(u):
          thingy = True
      if thingy == False:
        return
      else:
        if int(message) == number:
          await mes.channel.send("YOU GOT IT!! Guesses: " + str(guesses))
          randomcurrent = False
          guesses = 0
        elif int(message) < number:
          await mes.channel.send("too low")
          guesses +=1
        elif int(message) > number:
          await mes.channel.send("too high")
          guesses += 1
client.run(os.getenv('TOKEN'))
