# MakoKujo Discord bot

MakoKujo basically is something that I've created to test somethings
in python like the discord.py module and asynchronous tasks.


## ***@Cloning repository.*** ##

```bash
#1. clone repository
git clone https://github.com/catsploit/MakoKujo

#2. Open the project folder & install requirements
pip install -r requirements.txt 
#or pip3 install -r requirements.txt
```

## ***@Installing.***

1. To get the bot working you have to set-up your token. For that you can just create a `token.txt`
file and rewrite the function `read_token()` in `mako.py`, then link it to your token file path.

2. Or you can rewrite `bot.run(TOKEN)` in `mako.py` with your token string.



## ***@IMPORTANT***

If you're using python 3.6 or lower, you must install dataclass module due that
dataclass is a feature included in python 3.7

```bash
#JUST IF YOU'RE USING PYTHON 3.6 OR LOWER
pip3 install dataclasses
```


## ***@3rd party codes***

[NHentai-API](https://github.com/AlexandreSenpai/NHentai-API)