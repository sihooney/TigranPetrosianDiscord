import discord
import random

class TigranPetrosian(discord.Client):

    COPYPASTA = """Are you kidding ??? What the **** are you talking about man ? You are a biggest looser i ever seen in my life ! 
    You was doing PIPI in your pampers when i was beating players much more stronger then you! You are not proffesional, 
    because proffesionals knew how to lose and congratulate opponents, you are like a girl crying after i beat you! Be brave, 
    be honest to yourself and stop this trush talkings!!! Everybody know that i am very good blitz player, i can win anyone in 
    the world in single game! And "w"esley "s"o is nobody for me, just a player who are crying every single time when loosing, 
    ( remember what you say about Firouzja ) !!! Stop playing with my name, i deserve to have a good name during whole my chess carrier, 
    I am Officially inviting you to OTB blitz match with the Prize fund! Both of us will invest 5000$ and winner takes it all! 
    I suggest all other people who's intrested in this situation, just take a look at my results in 2016 and 
    2017 Blitz World championships, and that should be enough... No need to listen for every crying babe, 
    Tigran Petrosyan is always play Fair ! And if someone will continue Officially talk about me like that, 
    we will meet in Court! God bless with true! True will never die ! Liers will kicked off..."""

    SHORTENED_PHRASES = [
    "Are you kidding ??? What the **** are you talking about man ?",
    "You was doing PIPI in your pampers when i was beating players much more stronger then you!",
    "Be brave, be honest to yourself and stop this trush talkings!!!",
    "Everybody know that i am very good blitz player, i can win anyone in the world in single game!",
    '"w"esley "s"o is nobody for me',
    "Tigran Petrosyan is always play Fair !",
    "God bless with true! True will never die ! Liers will kicked off...",
    ]

    KEYWORDS = {"pipi", "pampers", "tigran", "petrosian"}
    
    async def on_message(self, msg: discord.Message):
        if msg.author.id == self.user.id:
            return
        
        if "Google en passant" in msg.content:
            await msg.reply("Holy Hell", mention_author=True)
            return
        
        for word in self.KEYWORDS:
            if word in msg.content.lower():
                if random.randint(0, 1) == 0:
                    await msg.channel.send(self.COPYPASTA.replace("\n", ''))
                else:
                    await msg.channel.send(random.choice(self.SHORTENED_PHRASES))
                return

client = TigranPetrosian()
client.run('token')
