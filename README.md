*Author: owe005*

# Coolbot
A super cool Discord bot

**Coolbot -  Documentation**

**Check library.py for what libraries is needed to run the bot. This is not meant for someone to just pick up and use for their server. This is merely a way for me to keep track of what updates I roll out for the bot.**

Features:
- Happy Birthday wisher,
- Weather information around the world,
- Lightshot URL generation,
- SSL (Stein, saks, laks - a new way to play rock paper scissors),
- Flip a coin,
- Plot a function on a graph (it returns a picture of the graph),
- Pull random image from a specified subreddit,
- Translations,
- Access ChatGPT with the bot,

Dependencies (pip install ..)
asyncpraw
discord 1.7.3
discord-py-slash-command 3.0.3
pytz
requests, json
time
pandas
googletrans **3.1.0a0** <-- very important version
discord.ext
itertools
datetime
random
os
string
tabulate
re
numpy
matplotlib.pyplot
openai

_/chinatime_
The reason why this bot was created in the first place. This command will return the current time in mainland China.

_/flipacoin_
This command will simply flip a coin for you and display it in an embedded message for you to view.

_/lightshot_
Will generate a random URL from prnt.sc/ for you to view. There is a chance that the image might be deleted, if that is the case, just try again!

_/ssl_
This is game of Stein Saks Laks! The rules of this game are: Stein beats Saks and Laks. Saks beats Laks but loses to Stein. Laks loses to Stein and Laks. If both pick the same, it's a tie. Will you risk playing Saks?

_/plot {function}_
The plot command is probably the most useful command added to this god forsaken bot. To put it simply, run /plot followed by the function you wish to plot. For example: /plot x^3 That's it! It is important to separate x variables with a * or else it will not run. E.g 2*x and not 2x.

_/reddit {subreddit}_ 
This command will return a random image from a subreddit of your choosing.

_/weather {city}_
As obvious as this is, I'll still explain it. You run /weather and give it a city name. For example /weather bergen.
