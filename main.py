from library import *
from plotFunction import *

client = discord.Client()
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.
guild_ids = [745725474465906732]

### Join call
@slash.slash(name="join", description=".", guild_ids=guild_ids)
async def _pog(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
### Join call end

### Documentation
@slash.slash(name="help", description="Documentation", guild_ids=guild_ids)
async def _help(ctx):

  embed=discord.Embed(title="Page 1/2\n\nCoolbot -  Documentation", description="These are the available commands and features for this bot.", color=0xff0000)
  embed.set_author(name="Github", url="https://github.com/owe005", icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
  embed.add_field(name="/chinatime", value="This command will return the current time in mainland China.", inline=False)
  embed.add_field(name="/flipacoin", value="This command will simply flip a coin for you and display it in an embedded message for you to view.", inline=False)
  embed.add_field(name="/lightshot", value="Will generate a random URL from prnt.sc/ for you to view. There is a chance that the image might be deleted, if that is the case, just try again!", inline=False)
  embed.add_field(name="/ssl", value="This is game of Stein Saks Laks! The rules of this game are:\nStein beats Saks and Laks.\nSaks beats Laks but loses to Stein.\nLaks loses to Stein and Laks.\nIf both pick the same, it's a tie.\nWill you risk playing Saks?", inline=False)

  embed2=discord.Embed(title="Page 2/2\n\nCoolbot -  Documentation ", description="These are the available commands and features for this bot.", color=0xff0000)
  embed2.set_author(name="Github", url="https://github.com/owe005", icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
  embed2.add_field(name="/plot {function}", value="Run /plot followed by the function you wish to plot. For example: /plot x^3+sin(2*x)-(5/x)+ln(x) That's it! It is important to separate x variables with a * or else it will not run. E.g 2*x and not 2x.", inline=False)
  embed2.add_field(name="/reddit {subreddit}", value="This command will return a random image from a subreddit of your choosing.", inline=False)
  embed2.add_field(name="/weather {city}", value="You run /weather and give it a city name. For example /weather bergen.", inline=False)

  message = await ctx.send(embed = embed)
  def check(reaction, user):
    return user == ctx.author

  await message.add_reaction('◀')
  await message.add_reaction('▶')

  i = 0
  reaction = None
  pages = [embed,embed2]

  while True:
    if str(reaction) == '◀':
      if i > 0:
        i -= 1
        await message.edit(embed = pages[i])

    elif str(reaction) == '▶':
      if i < 2:
        i += 1
        await message.edit(embed = pages[i])

    try:
      reaction, user = await client.wait_for('reaction_add', timeout = 30.0, check = check)
      await message.remove_reaction(reaction, user)

    except:
      break

  await message.clear_reactions()
### Documentation

### Stein saks laks (alternativ måte å spille stein, saks, papir)
@slash.slash(name="ssl", description="STEIN, SAKS, LAKS!", guild_ids=guild_ids)
async def _rps(ctx, choice: str):
  choices=["stein", "saks", "laks"]
  if choice.lower() not in choices:
    await ctx.send("Error: Stein, saks eller laks?")
  else:
    bot_choice = random.choice(choices)

    if (choice.lower() == bot_choice.lower()):
      embed = discord.Embed(title=f"Vi begge valgte {choice}. Uavgjort!")
      await ctx.send(embed=embed)

    elif (choice.lower() == "stein"):
      if (bot_choice.lower() == "saks"):
        embed = discord.Embed(title="Du valgte stein, jeg valgte saks. You win.")
        await ctx.send(embed=embed)

      else:
        embed = discord.Embed(title="Du valgte stein, jeg valgte laks. I cannot win, therefore you win.")
        await ctx.send(embed=embed)

    elif (choice.lower() == "saks"):
      if (bot_choice.lower() == "stein"):
        embed = discord.Embed(title="Du valgte saks, jeg valgte stein. I win.")
        await ctx.send(embed=embed)

      else:
        embed = discord.Embed(title="Du valgte saks, jeg valgte laks. I cannot win, therefore you win.")
        await ctx.send(embed=embed)

    elif (choice.lower() == "laks"):
      if (bot_choice.lower() == "stein"):
        embed = discord.Embed(title="Du valgte laks, jeg valgte stein. You cannot win, therefore I win.")
        await ctx.send(embed=embed)

      else:
        embed = discord.Embed(title="Du valgte laks, jeg valgte saks. You cannot win, therefore I win.")
        await ctx.send(embed=embed)
### SSL End

### ChatGPT in Discord!
@slash.slash(name="askCoolbot", description="What do you want to know?", guild_ids=guild_ids)
async def _askCoolbot(ctx, prompt: str):
  
  await ctx.defer()
  
  context = dan + "\n" + prompt
  response = openai.Completion.create(
    engine ="text-davinci-003",
    prompt = context,
    max_tokens = 500,
    n=1,
    stop=None,
    temperature=0.5,
  )
  answer = response.choices[0].text.strip()

  if len(prompt) > 256:
    output = f"**The question was**: *{prompt}* \n\n**ANSWER**: *{answer}*"
    await ctx.send(output)
    
  else:
    embed = discord.Embed(title=f"QUESTION: {prompt}", description=answer)
    await ctx.send(embed=embed)
### GPT End

### Generate random lightshot URL
@slash.slash(name="lightshot", description="Generate random Lightshot URL", guild_ids=guild_ids)
async def _lightshot(ctx): 
      randomurlString = string.ascii_lowercase + string.digits
      randomizing = ''.join(random.choice(randomurlString) for i in range(6))
      url = "https://prnt.sc/" + str(randomizing)
      await ctx.send(url)
### Random lightshot URL End

### Flip a coin
@slash.slash(name="flipacoin", description="Flip a coin!", guild_ids=guild_ids)
async def _flipacoin(ctx): 
      deter = [1, 0]
      if random.choice(deter) == 1:
          embedVar2 = discord.Embed(title="Heads!", description="You rolled heads bro", color=0xff0000)
          embedVar2.set_thumbnail(url="https://www.pngkey.com/png/full/146-1464786_400px-circle-quarter-heads-side-of-coin.png")
          await ctx.send(embed=embedVar2)
      else:
          embedVar3 = discord.Embed(title="Tails!", description="You rolled tails bro", color=0xff0000)
          embedVar3.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
          await ctx.send(embed=embedVar3)
### Flip a coin end

### Return time in China!
@slash.slash(name="chinatime", description="Returns current time in China", guild_ids=guild_ids)
async def _chinatime(ctx): 
      asia_time = pytz.timezone('Asia/Shanghai')
      country_time = datetime.now(asia_time)
      time = country_time.strftime("%H:%M:%S")
      china_time = f"Currently it is {time} in China"
      embedMsg = discord.Embed(title=china_time)
      await ctx.send(embed=embedMsg)
### Chinatime end

### Weather api
@slash.slash(name="weather", description="Give a city name and it will return the current weather", guild_ids=guild_ids)
async def _weather(ctx, city: str): 
      city_name = str(city)
      complete_url = base_url + "appid=" + api_key + "&q=" + city_name
      response = requests.get(complete_url)
      x = response.json()

      if x["cod"] != "404": # If it does not return 404.
          y = x["main"]
          current_temperature = y["temp"]
          current_temperature = current_temperature - 273.15
          current_temperature = round(current_temperature, 2)
          z = x["weather"]
          weather_description = z[0]["description"]
          embedWeather = discord.Embed(title=f"Information about {city_name.capitalize()}", description=f"The current temperature is {current_temperature} ℃ with {weather_description}", color=0xff0000)

          if "cloud" in weather_description:
            embedWeather.set_thumbnail(url="https://images.immediate.co.uk/production/volatile/sites/22/2018/09/Storm-clouds-UK-countryside-500b8b1.jpg?quality=90&resize=768,574")

          elif "clear" in weather_description:
            embedWeather.set_thumbnail(url="https://clarksvillenow.sagacom.com/files/2020/11/shutterstock_286242953.jpg")

          elif "thunder" in weather_description:
            embedWeather.set_thumbnail(url="https://imageio.forbes.com/specials-images/imageserve/180132155/Lightning-over-field/960x0.jpg?fit=bounds&format=jpg&width=960")
          
          elif "snow" in weather_description:
            embedWeather.set_thumbnail(url="https://www.thesun.co.uk/wp-content/uploads/2018/10/NINTCHDBPICT000444849657.jpg")

          elif "rain" in weather_description:
            embedWeather.set_thumbnail(url="https://assets.thehansindia.com/h-upload/2021/08/17/1102463-pain.webp")
            
          await ctx.send(embed=embedWeather)

      else:
          await ctx.send("Place not found") # Else, it returned 404
### End weather

### Plot
@slash.slash(name="plot", description="Take adventage of matplotlib in Discord!", guild_ids=guild_ids)
async def _plot(ctx, function: str):
    x = np.linspace(-5,5,100)
    y = string2func(function)
    plt.plot(x,y(x))
    plt.legend([function])
    figure = "figures/figure"+str(random.sample(range(100000), 1)) +".jpg"
    plt.savefig(figure)
    plt.close()
    await ctx.send(file=discord.File(figure))
    os.remove(figure)
### Plot end

### Return random image from specific subreddit with Reddit API
@slash.slash(name="reddit", description="Return image from subreddit", guild_ids=guild_ids)
async def _reddit(ctx, sub: str):
  subreddit = await reddit.subreddit(sub)
  all_subs = []
  top = subreddit.hot(limit=50)
  async for submission in top:
    all_subs.append(submission)

  random_sub = random.choice(all_subs)
  name = random_sub.title
  url = random_sub.url
  em = discord.Embed(title=name)
  em.set_image(url=url)
  em.set_footer(text="If it does not load, try again. It is because of posts linking to imgur,gyazo, etc..")
  await ctx.send(embed=em)
### End random subreddit image

@client.event
# Start events
async def on_ready(): 
  change_status.start()
  cat_of_month.start()
  happy_birthday.start()
  print("Coolbot is online and ready")

### Status Change
@tasks.loop(hours=1)
async def change_status(): 
  status = cycle(["Rock Paper Scissors", "UNO!", "Phasmophobia"])
  await client.change_presence(activity=discord.Game(next(status)))
### End Status Change

### Cat of the Month
@tasks.loop(hours=48)
async def cat_of_month(): 
  channel = client.get_channel(828292849061068831)

  if (str(datetime.today().strftime('%d')) != "01"): # If not 01 of the current month, print status update.
    print("It is not the first of a given month.")

  elif (str(datetime.today().strftime('%d')) == "01"): # If it is, select random cat and send it in embedded message.
    channel = client.get_channel(745726336311623740)
    random_user = random.choice(Users)
    clownMsg = (f"Listen up everyone, {random_user} has been automatically chosen as the Cat of {datetime.today().strftime('%B')}\n\nThis action was done automatically, and may not be reverted.")
    embedMsg = discord.Embed(title=f"NEW Cat of the Month: {random_user}!",description=clownMsg, color=0xff0000)
    embedMsg.set_thumbnail(url="https://st3.depositphotos.com/1177973/13325/i/450/depositphotos_133251802-stock-photo-cute-cat-on-couch.jpg")
    await channel.send(embed=embedMsg)
### End Cat of the Month

### Happy Birthday Impl
@tasks.loop(hours=24) # Check everyday.
async def happy_birthday():
  channel = client.get_channel(745726336311623740)
  timezone = pytz.timezone("Europe/Amsterdam")
  day = str(datetime.now(timezone).day)
  month = str(datetime.now(timezone).month)
  dateNow = str(f"{day}/{month}")
  print(dateNow)

  for i in birthdays:
    targetBday = str(birthdays[i])

    if dateNow == targetBday:
      output = f"@everyone - Happy Birthday to / Gratulerer med dagen til @{i}"
      print(f"It IS {i}'s birthday today")
      await channel.send(output)
### End Happy Birthday Impl

@client.event
async def on_message(message): 
  var = str(message.content) # Save the message as a String.
  varlower = var.lower() # Lowercase it for special conditions.
  channel = str(message.channel) # Save the channel as a String
  
  if message.author.bot == True: # Ignore Bots.
    return
  
### Rare chance!
  with open("chance.txt","r") as perc:
    prob = int(perc.readlines()[0])

    if random.randint(1,prob) == 1: 
      embedVar = discord.Embed(title=(f"Wow!!"), description=f"Congratulations, the odds of you receiving this message was 1 / {prob}! This message was sent because you recently sent a message in the discord server. The odds have now been reset to 8192, but you don't have to tell them! :)", color=0xff0000)
      embedVar.set_image(url="https://cdn.discordapp.com/attachments/745725475157967000/942926568475463690/nooocat.jpg")
      probDec = str(8192)

      with open("chance.txt","w") as percUpd:
        percUpd.writelines(probDec)
        
      await message.author.send(embed = embedVar)

    else:
      prob-=1
      probInc = str(prob)

      with open("chance.txt","w") as percUpd:
        percUpd.writelines(probInc)
### End Rare chance!

### Translations ### O(1)
  if channel == "chinese-translation":
    translator = Translator()
    results = translator.translate(var, dest='zh-cn')
    await message.channel.send(results.text)

  if channel == "japanese-translation":
    translator4 = Translator()
    results4 = translator4.translate(var, dest='ja')
    await message.channel.send(results4.text)
  
  if channel == "english-translation":
    translator2 = Translator()
    results2 = translator2.translate(var, dest='en')
    await message.channel.send(results2.text)

  if channel == "norwegian-translation":
    translator3 = Translator()
    results3 = translator3.translate(var, dest='no')
    await message.channel.send(results3.text)
### End Translations ###

### Run Bot
client.run(TOKEN)