import discord
import random
from riotwatcher import LolWatcher
from pathlib import Path

from discord.ui import Button, View
from discord.ext import commands

#import os

#     py -3 main.py

"""


PUUID : 6CusSU6ICOQfsOO5tmyocyvJKf89X_OG3IzKtluNWwzmnWFjFcJmSkRch8zOHkJROh3nhHm1yh3xoQ

ACCOUNT ID : 7GkedLZUuqduU1L-3G0CrmkJXoAlS7aCfEGgbY8yv4-5tK4ww2S7KHja

ID : 7XDvEqQlzo1ffnt7XNJ6rl59Uz6ZqAwvSG0s5Djs3aGG7Ob2




"""
prefix = "."
intents=discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

lol_watcher = LolWatcher('RGAPI-d765c4a0-41e0-4a27-ad97-0211606c9b6e')
version = lol_watcher.data_dragon.versions_for_region('na1')
#profile_icon_version = version['n']['profile_icon']
bot = commands.Bot(command_prefix=prefix, intents=intents)

champList = {'266': 'Aatrox', '103': 'Ahri', '84': 'Akali', '166': 'Akshan', '12': 'Alistar', '32': 'Amumu', '34': 'Anivia', '1': 'Annie', '523': 'Aphelios', '22': 'Ashe', '136': 'AurelionSol', '268': 'Azir', '432': 'Bard', '200': 'Belveth', '53': 'Blitzcrank', '63': 'Brand', '201': 'Braum', '51': 'Caitlyn', '164': 'Camille', '69': 'Cassiopeia', '31': 'Chogath', '42': 'Corki', '122': 'Darius', '131': 'Diana', '119': 'Draven', '36': 'DrMundo', '245': 'Ekko', '60': 'Elise', '28': 'Evelynn', '81': 'Ezreal', '9': 'Fiddlesticks', '114': 'Fiora', '105': 'Fizz', '3': 'Galio', '41': 'Gangplank', '86': 'Garen', '150': 'Gnar', '79': 'Gragas', '104': 'Graves', '887': 'Gwen', '120': 'Hecarim', '74': 'Heimerdinger', '420': 'Illaoi', '39': 'Irelia', '427': 'Ivern', '40': 'Janna', '59': 'JarvanIV', '24': 'Jax', '126': 'Jayce', '202': 'Jhin', '222': 'Jinx', '145': 'Kaisa', '429': 'Kalista', '43': 'Karma', '30': 'Karthus', '38': 'Kassadin', '55': 'Katarina', '10': 'Kayle', '141': 'Kayn', '85': 'Kennen', '121': 'Khazix', '203': 'Kindred', '240': 'Kled', '96': 'KogMaw', '897': 'KSante', '7': 'Leblanc', '64': 'LeeSin', '89': 'Leona', '876': 'Lillia', '127': 'Lissandra', '236': 'Lucian', '117': 'Lulu', '99': 'Lux', '54': 'Malphite', '90': 'Malzahar', '57': 'Maokai', '11': 'MasterYi', '902': 'Milio', '21': 'MissFortune', '62': 'MonkeyKing', '82': 'Mordekaiser', '25': 'Morgana', '267': 'Nami', '75': 'Nasus', '111': 'Nautilus', '518': 'Neeko', '76': 'Nidalee', '895': 'Nilah', '56': 'Nocturne', '20': 'Nunu', '2': 'Olaf', '61': 'Orianna', '516': 'Ornn', '80': 'Pantheon', '78': 'Poppy', '555': 'Pyke', '246': 'Qiyana', '133': 'Quinn', '497': 'Rakan', '33': 'Rammus', '421': 'RekSai', '526': 'Rell', '888': 'Renata', '58': 'Renekton', '107': 'Rengar', '92': 'Riven', '68': 'Rumble', '13': 'Ryze', '360': 'Samira', '113': 'Sejuani', '235': 'Senna', '147': 'Seraphine', '875': 'Sett', '35': 'Shaco', '98': 'Shen', '102': 'Shyvana', '27': 'Singed', '14': 'Sion', '15': 'Sivir', '72': 'Skarner', '37': 'Sona', '16': 'Soraka', '50': 'Swain', '517': 'Sylas', '134': 'Syndra', '223': 'TahmKench', '163': 'Taliyah', '91': 'Talon', '44': 'Taric', '17': 'Teemo', '412': 'Thresh', '18': 'Tristana', '48': 'Trundle', '23': 'Tryndamere', '4': 'TwistedFate', '29': 'Twitch', '77': 'Udyr', '6': 'Urgot', '110': 'Varus', '67': 'Vayne', '45': 'Veigar', '161': 'Velkoz', '711': 'Vex', '254': 'Vi', '234': 'Viego', '112': 'Viktor', '8': 'Vladimir', '106': 'Volibear', '19': 'Warwick', '498': 'Xayah', '101': 'Xerath', '5': 'XinZhao', '157': 'Yasuo', '777': 'Yone', '83': 'Yorick', '350': 'Yuumi', '154': 'Zac', '238': 'Zed', '221': 'Zeri', '115': 'Ziggs', '26': 'Zilean', '142': 'Zoe', '143': 'Zyra'}

@bot.event
async def on_ready():
    print("Ready")

"""@bot.command()
async def setprefix(ctx, newPrefix):
    global prefix
    prefix = newPrefix"""

@bot.command()
async def t(ctx):

    #profileIconVersion = (version["n"])["profileicon"]

    #lol_watcher.data_dragon.champions(champions_version)
    """print(lol_watcher.summoner.by_name("na1", "mystixninja726"))
    print(type(profileIconVersion))
    print(lol_watcher.data_dragon.profile_icons(profileIconVersion))"""

    #embed = discord.Embed()

    #profileIcons = lol_watcher.data_dragon.profile_icons(profileIconVersion)

    #testIcon = (((profileIcons["data"])["0"])["image"])["sprite"]
    #print(testIcon)

    #file = discord.File("path/to/my/image.png", filename="image.png")
    #embed = discord.Embed(description="test", url="https://ddragon.leagueoflegends.com/cdn/13.13.1/img/profileicon/5320.png")
    
    """embed.set_image(url="https://ddragon.leagueoflegends.com/cdn/13.13.1/img/profileicon/5320.png")
    print(embed.image.width)
    print(embed.image.height)

    embed.image.width = 1
    embed.image.height = 1

    print(embed.image.width)
    print(embed.image.height)"""




    #await ctx.send(embed=embed)


    #await ctx.send("hello")
    """a = str(Path("BRONZE.png").absolute()).replace("\\", "/")
    print(a)"""

    """print(lol_watcher.champion_mastery.by_summoner("na1", summonerID))"""

    """
    
    VEry IMPROTANT STUFFS!!!! 
    THIS IS FOR GETTING TOP 3 PLAYed WINRATE CHAMPS OKS?? YES!
    
    
    """
    """matchIDs = lol_watcher.match.matchlist_by_puuid("na1", "6CusSU6ICOQfsOO5tmyocyvJKf89X_OG3IzKtluNWwzmnWFjFcJmSkRch8zOHkJROh3nhHm1yh3xoQ", 0, 3, None, "ranked")

    championGames = {}
    championWins = {}
    championLosses = {}

    win = 0
    for i in matchIDs:
        match = lol_watcher.match.by_id("na1", i)
        participants = (match["info"])["participants"]
        for j in participants:
            if(j["puuid"] == "6CusSU6ICOQfsOO5tmyocyvJKf89X_OG3IzKtluNWwzmnWFjFcJmSkRch8zOHkJROh3nhHm1yh3xoQ"):
                championId = str(j["championId"])
                
                if(championId not in championGames):
                    championGames[championId] = 0
                championGames[championId] += 1
    #championGames.values()
    print(championGames)
    print(champList['91'])
    print(champList['69'])
    print(type(championGames.values()))"""
  
    """print(win)
    print(len(matchIDs))
    print((win/len(matchIDs))*100)"""


    # IMPORTANT STUFFS ENDS HERES!!!! OKKKKKKK LISTENNNN ME BIG YES YES OKOK NO YES UP DOWN ONLY GO UP FROM HERE GOOGOGOGOGOG





    print(lol_watcher.spectator.by_summoner("na1", (lol_watcher.summoner.by_name('na1', "astrotan"))["id"]))














@bot.command()
async def show(ctx):
    embed = discord.Embed(color=0xFF5733, title="hello", type="rich", description="this is a test")
    
    for i in range(3):
        await ctx.send(embed=embed)

"""

possibly make a summary of stats of the most important things in the last 20 games (or watever riot api allows):::::

i.e avg cs/min, avg wrds/min, avg gold/min, avg dmg dealt/min, avg kda, avg kills/min @14, avg cs@14, winrate 






"""


@bot.command()
async def gtc(ctx):
    win = False
    champindex = random.randint(0,162)
    champ = champlist[champindex]

    msg=""
    for i in champ:
        msg += "a"
    # :white_large_square:
    while win == False:

        embed = discord.Embed(color=0xFF5733, title="hello", description=msg)
        await ctx.send(embed=embed)

        await ctx.send(champ)
        message = await bot.wait_for("message")

        for i in range(len(champ)):
            if champ[i].lower() == message.content.lower():
                msg[i] == champ[i]

        if(msg.lower() == champ.lower()):
            await ctx.send("Win")
            win = True
        #else:
            #await ctx.send("Wrong")





"""


{

    RANKED FLEX

    "gameId": 4705278269,
    "mapId": 11,
    "gameMode": "CLASSIC",
    "gameType": "MATCHED_GAME",
    "gameQueueConfigId": 440,
    "participants": [
        {
            "teamId": 100,
            "spell1Id": 14,
            "spell2Id": 4,
            "championId": 34,
            "profileIconId": 4086,
            "summonerName": "ImpulseIV",
            "bot": false,
            "summonerId": "OmkqMuL99MZO3ODNUb5R7zaadHOQ7Xg_GkJZNo8tjIFD3Jc",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8230,
                    8226,
                    8210,
                    8236,
                    8009,
                    9105,
                    5008,
                    5008,
                    5003
                ],
                "perkStyle": 8200,
                "perkSubStyle": 8000
            }
        },
        {
            "teamId": 100,
            "spell1Id": 11,
            "spell2Id": 4,
            "championId": 64,
            "profileIconId": 682,
            "summonerName": "Later2That",
            "bot": false,
            "summonerId": "XDaC73u0_mtxPvcWdxgRKI5JPE6IkA81nKgBWljP6Of6WR8",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8010,
                    9111,
                    9104,
                    8014,
                    8347,
                    8304,
                    5005,
                    5008,
                    5002
                ],
                "perkStyle": 8000,
                "perkSubStyle": 8300
            }
        },
        {
            "teamId": 100,
            "spell1Id": 4,
            "spell2Id": 14,
            "championId": 497,
            "profileIconId": 3861,
            "summonerName": "FoxChar2",
            "bot": false,
            "summonerId": "ei-32Muh5pnyUrO4nSOLs0WlVJq3vJ_TVxWI6V2SipgVORic",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8465,
                    8401,
                    8473,
                    8242,
                    8136,
                    8106,
                    5008,
                    5008,
                    5002
                ],
                "perkStyle": 8400,
                "perkSubStyle": 8100
            }
        },
        {
            "teamId": 100,
            "spell1Id": 4,
            "spell2Id": 12,
            "championId": 57,
            "profileIconId": 3592,
            "summonerName": "RAT 23",
            "bot": false,
            "summonerId": "uPMgh0UnQzUYLwzKUZCjAZpVZaj7mtAylFk6BmuZkCVhIG8-U4rimoVP3Q",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8437,
                    8446,
                    8429,
                    8451,
                    8304,
                    8345,
                    5008,
                    5003,
                    5001
                ],
                "perkStyle": 8400,
                "perkSubStyle": 8300
            }
        },
        {
            "teamId": 100,
            "spell1Id": 4,
            "spell2Id": 6,
            "championId": 22,
            "profileIconId": 3543,
            "summonerName": "AndrewLinco",
            "bot": false,
            "summonerId": "uO9-Pax6cDN70oWMO2xYCrZ0hPrl0sW729U-cFtteVOi-gGCdpbskGMJyQ",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8008,
                    9111,
                    9104,
                    8017,
                    8304,
                    8410,
                    5005,
                    5008,
                    5002
                ],
                "perkStyle": 8000,
                "perkSubStyle": 8300
            }
        },
        {
            "teamId": 200,
            "spell1Id": 6,
            "spell2Id": 11,
            "championId": 154,
            "profileIconId": 4991,
            "summonerName": "Grab Yo Þussy",
            "bot": false,
            "summonerId": "ZYSrWkK5qpW6KrEKivf6sJj9BOSFDPqek7LAQoZojucKhv0",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8010,
                    9111,
                    9105,
                    8014,
                    8210,
                    8236,
                    5007,
                    5008,
                    5001
                ],
                "perkStyle": 8000,
                "perkSubStyle": 8200
            }
        },
        {
            "teamId": 200,
            "spell1Id": 14,
            "spell2Id": 4,
            "championId": 412,
            "profileIconId": 5675,
            "summonerName": "Lifelookstough",
            "bot": false,
            "summonerId": "7814WhmOo4iZdkvpInXEPZnkrhG3UZUJyl5CBaN9eI3OOvE",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8351,
                    8306,
                    8345,
                    8347,
                    8473,
                    8242,
                    5008,
                    5008,
                    5002
                ],
                "perkStyle": 8300,
                "perkSubStyle": 8400
            }
        },
        {
            "teamId": 200,
            "spell1Id": 12,
            "spell2Id": 4,
            "championId": 517,
            "profileIconId": 5738,
            "summonerName": "Dècîmàtê",
            "bot": false,
            "summonerId": "LVs7xx0vT4TjN5cNDOWZtfkRzOL04hwDnCxO95pUjr8CVfY",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8010,
                    8009,
                    9105,
                    8299,
                    8444,
                    8242,
                    5008,
                    5008,
                    5003
                ],
                "perkStyle": 8000,
                "perkSubStyle": 8400
            }
        },
        {
            "teamId": 200,
            "spell1Id": 12,
            "spell2Id": 4,
            "championId": 54,
            "profileIconId": 14,
            "summonerName": "RTO Slayer",
            "bot": false,
            "summonerId": "rDCoKlTa7aoJHABPT5pJPjUPogLVMQ32lSyieKOuS2QiEd2RcneB4htyYw",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8437,
                    8401,
                    8429,
                    8451,
                    8304,
                    8345,
                    5005,
                    5002,
                    5003
                ],
                "perkStyle": 8400,
                "perkSubStyle": 8300
            }
        },
        {
            "teamId": 200,
            "spell1Id": 4,
            "spell2Id": 3,
            "championId": 81,
            "profileIconId": 4648,
            "summonerName": "Biu u d1e ",
            "bot": false,
            "summonerId": "7Fzpg71Ym6BLyGMI6SI1NEuanaM7_M_NxLdGSULpvSsWlNw",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8005,
                    8009,
                    9104,
                    8017,
                    8345,
                    8347,
                    5005,
                    5008,
                    5002
                ],
                "perkStyle": 8000,
                "perkSubStyle": 8300
            }
        }
    ],
    "observers": {
        "encryptionKey": "/ubN0nUX1kLAr4PAybAZYeNnyAxuzrhI"
    },
    "platformId": "NA1",
    "bannedChampions": [
        {
            "championId": 9,
            "teamId": 100,
            "pickTurn": 1
        },
        {
            "championId": 80,
            "teamId": 100,
            "pickTurn": 2
        },
        {
            "championId": 203,
            "teamId": 100,
            "pickTurn": 3
        },
        {
            "championId": 360,
            "teamId": 100,
            "pickTurn": 4
        },
        {
            "championId": 91,
            "teamId": 100,
            "pickTurn": 5
        },
        {
            "championId": 121,
            "teamId": 200,
            "pickTurn": 6
        },
        {
            "championId": 117,
            "teamId": 200,
            "pickTurn": 7
        },
        {
            "championId": 110,
            "teamId": 200,
            "pickTurn": 8
        },
        {
            "championId": 902,
            "teamId": 200,
            "pickTurn": 9
        },
        {
            "championId": 7,
            "teamId": 200,
            "pickTurn": 10
        }
    ],
    "gameStartTime": 1688694340469,
    "gameLength": 963
}

"""

"""

RANKED SOLO DUO


{
    "gameId": 4705305039,
    "mapId": 11,
    "gameMode": "CLASSIC",
    "gameType": "MATCHED_GAME",
    "gameQueueConfigId": 420,
    "participants": [
        {
            "teamId": 100,
            "spell1Id": 11,
            "spell2Id": 4,
            "championId": 121,
            "profileIconId": 29,
            "summonerName": "Mir fangirl",
            "bot": false,
            "summonerId": "h-uic_pBUrHxrxA0sDlJfLQzdQYnEpmjDN6ibNBLR3cWlstsFuEGYhHkHQ",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8369,
                    8304,
                    8321,
                    8347,
                    8136,
                    8143,
                    5008,
                    5008,
                    5002
                ],
                "perkStyle": 8300,
                "perkSubStyle": 8100
            }
        },
        {
            "teamId": 100,
            "spell1Id": 4,
            "spell2Id": 3,
            "championId": 119,
            "profileIconId": 29,
            "summonerName": "DA GIP",
            "bot": false,
            "summonerId": "9ad9XHKSZsawFcI3IuyZvECIzIgUdp-QH5gHAzVVLTweeuFXEsqn2fmOrQ",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8008,
                    9111,
                    9103,
                    8014,
                    8304,
                    8345,
                    5005,
                    5008,
                    5002
                ],
                "perkStyle": 8000,
                "perkSubStyle": 8300
            }
        },
        {
            "teamId": 100,
            "spell1Id": 12,
            "spell2Id": 6,
            "championId": 412,
            "profileIconId": 4025,
            "summonerName": "I am Súnlight",
            "bot": false,
            "summonerId": "WuDZrWQXlcBTk-2mpvwcTuorTe3rEPriQeU490vnkZAtTBk",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8351,
                    8313,
                    8345,
                    8347,
                    8429,
                    8242,
                    5005,
                    5002,
                    5001
                ],
                "perkStyle": 8300,
                "perkSubStyle": 8400
            }
        },
        {
            "teamId": 100,
            "spell1Id": 7,
            "spell2Id": 4,
            "championId": 902,
            "profileIconId": 23,
            "summonerName": "sup line",
            "bot": false,
            "summonerId": "kxYQ62VJXDl8JtX0XEnEznqukCa76EwS0SLagxEi0_HS2s2q",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8214,
                    8226,
                    8210,
                    8237,
                    8345,
                    8347,
                    5007,
                    5008,
                    5002
                ],
                "perkStyle": 8200,
                "perkSubStyle": 8300
            }
        },
        {
            "teamId": 100,
            "spell1Id": 4,
            "spell2Id": 14,
            "championId": 17,
            "profileIconId": 5629,
            "summonerName": "Little Meat Pete",
            "bot": false,
            "summonerId": "D0ZOesJsERlqAfjr5JjQ_NuKtt8uJeSjmlnpnxu-jGx2dEA",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8021,
                    9111,
                    9104,
                    8299,
                    8473,
                    8451,
                    5005,
                    5008,
                    5002
                ],
                "perkStyle": 8000,
                "perkSubStyle": 8400
            }
        },
        {
            "teamId": 200,
            "spell1Id": 6,
            "spell2Id": 4,
            "championId": 22,
            "profileIconId": 29,
            "summonerName": "C9 Berzerker",
            "bot": false,
            "summonerId": "F8b4FAcs2Rmc66WSx3IKwIjqb_uZVuxGRX3Z8Ewt5-dqw0MGx-iEEDE7nw",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8008,
                    8009,
                    9103,
                    8014,
                    8410,
                    8345,
                    5005,
                    5008,
                    5002
                ],
                "perkStyle": 8000,
                "perkSubStyle": 8300
            }
        },
        {
            "teamId": 200,
            "spell1Id": 4,
            "spell2Id": 11,
            "championId": 107,
            "profileIconId": 3,
            "summonerName": "rege",
            "bot": false,
            "summonerId": "1y3IKAn1NvS0Cpfl8hR4QB_n_s3V5Re9fnkgoL3tDzfQTAk",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8021,
                    9111,
                    9104,
                    8014,
                    8321,
                    8304,
                    5005,
                    5008,
                    5002
                ],
                "perkStyle": 8000,
                "perkSubStyle": 8300
            }
        },
        {
            "teamId": 200,
            "spell1Id": 12,
            "spell2Id": 4,
            "championId": 897,
            "profileIconId": 5454,
            "summonerName": "uni13",
            "bot": false,
            "summonerId": "WjyiWD7m-ndNmeCG2KO9sm4HPxvAdURY5YaaF-gSWtXT6Q0",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8437,
                    8446,
                    8429,
                    8451,
                    8304,
                    8410,
                    5005,
                    5003,
                    5003
                ],
                "perkStyle": 8400,
                "perkSubStyle": 8300
            }
        },
        {
            "teamId": 200,
            "spell1Id": 14,
            "spell2Id": 4,
            "championId": 201,
            "profileIconId": 1627,
            "summonerName": "Isles2",
            "bot": false,
            "summonerId": "LLFzj31oqH8iq-dIYR_OquGOQ_9VB46d_zzgXqcQ_sXY0xJO6P7N-9TtCA",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8465,
                    8463,
                    8473,
                    8242,
                    8347,
                    8316,
                    5005,
                    5002,
                    5002
                ],
                "perkStyle": 8400,
                "perkSubStyle": 8300
            }
        },
        {
            "teamId": 200,
            "spell1Id": 12,
            "spell2Id": 4,
            "championId": 134,
            "profileIconId": 29,
            "summonerName": "time chamber0",
            "bot": false,
            "summonerId": "avDLfQU2mqlqsvNuBITwYnx6AIBj3BBpgAqQnBnFk65hajL52jIF5spH8w",
            "gameCustomizationObjects": [],
            "perks": {
                "perkIds": [
                    8369,
                    8304,
                    8345,
                    8347,
                    8226,
                    8237,
                    5005,
                    5008,
                    5003
                ],
                "perkStyle": 8300,
                "perkSubStyle": 8200
            }
        }
    ],
    "observers": {
        "encryptionKey": "YkY4aSr0Y2ymqh6DBhORbTZu/VdRki1Z"
    },
    "platformId": "NA1",
    "bannedChampions": [
        {
            "championId": 126,
            "teamId": 100,
            "pickTurn": 1
        },
        {
            "championId": 76,
            "teamId": 100,
            "pickTurn": 2
        },
        {
            "championId": -1,
            "teamId": 100,
            "pickTurn": 3
        },
        {
            "championId": 498,
            "teamId": 100,
            "pickTurn": 4
        },
        {
            "championId": 7,
            "teamId": 100,
            "pickTurn": 5
        },
        {
            "championId": -1,
            "teamId": 200,
            "pickTurn": 6
        },
        {
            "championId": 887,
            "teamId": 200,
            "pickTurn": 7
        },
        {
            "championId": 518,
            "teamId": 200,
            "pickTurn": 8
        },
        {
            "championId": 498,
            "teamId": 200,
            "pickTurn": 9
        },
        {
            "championId": 203,
            "teamId": 200,
            "pickTurn": 10
        }
    ],
    "gameStartTime": 1688695472923,
    "gameLength": 179
}


"""



@bot.command()
async def profile(ctx, user):
    #await ctx.send(lol_watcher.data_dragon.profile_icons(version, '5310'))
    #print(lol_watcher.summoner.by_name('na1', user))
    #print(lol_watcher.summoner.by_id('na1', '7XDvEqQlzo1ffnt7XNJ6rl59Uz6ZqAwvSG0s5Djs3aGG7Ob2'))
    #print(type(user))

    user = user.replace("_", " ")

    summonerID = (lol_watcher.summoner.by_name('na1', user))["id"]
    summoner = lol_watcher.league.by_summoner('na1', summonerID)
    #print(summoner)
    #summonerInfo = summoner[0]
    profileIcon = str((lol_watcher.summoner.by_name('na1', user))["profileIconId"])
    level = (lol_watcher.summoner.by_name('na1', user))["summonerLevel"]
    name = (lol_watcher.summoner.by_name('na1', user))["name"]
    
    mastery = ""
    masteryList = lol_watcher.champion_mastery.by_summoner("na1", summonerID)

    if(len(masteryList) > 3):
        for i in range(0,3):
            mastery += str(i+1) + ". " + champList[str((masteryList[i])["championId"])] + " - " + str((masteryList[i])["championPoints"]) + "\n"



    #print(summoner)
    #await ctx.send(lol_watcher.data_dragon.profile_icons("13.12.1"))
    #file = discord.File("C:/Users/yug27/VSCode Projects/we test the discord bot arc/Iron.png", filename="Iron.png")

    embed = discord.Embed(title=name + "'s Profile")
    description = "Level: " + str(level)
    embed.description = description
    embed.set_thumbnail(url="https://ddragon.leagueoflegends.com/cdn/13.13.1/img/profileicon/" + profileIcon + ".png")
    embed.add_field(name="Top 3 Champion Mastery", value=mastery, inline=False)
    
    rankedButton = Button(style=discord.ButtonStyle.green, label="Ranked Profile")
    mainButton = Button(style=discord.ButtonStyle.green, label="Main Profile")
    spectateButton = Button(style=discord.ButtonStyle.blurple, label="Live Game")

    view = View()
    view.add_item(mainButton)


    try:
        summonerInfo = summoner[0]

        rank = summonerInfo["tier"]
        wins = summonerInfo["wins"]
        losses = summonerInfo["losses"]
        tier = summonerInfo["rank"]
        lp = summonerInfo["leaguePoints"]
        
        
        
        
        view.add_item(rankedButton)
    except:
        print("hehexd")


    try:
        spectateInfo = lol_watcher.spectator.by_summoner("na1", summonerID)
        print(spectateInfo)
        
        queueType = spectateInfo["gameQueueConfigId"]
        gameMode = ""
        if(queueType == 450):
            gameMode = "Aram"
        elif(queueType == 420):
            gameMode = "Ranked Solo/Duo"
        elif(queueType == 440):
            gameMode = "Ranked Flex"
        elif(queueType == 400):
            gameMode = "Draft Pick"
        else:
            gameMode = "Blind Pick"

        #gameMode = spectateInfo["gameMode"]
        
        #champion = champList
        participants = spectateInfo["participants"]
        #print(participants)
        for i in participants:
            if(i["summonerId"] == summonerID):
                champion = champList[str(i["championId"])]






        view.add_item(spectateButton)
    except:
        print("FALSEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

    
    




    "https://ddragon.leagueoflegends.com/cdn/13.13.1/img/profileicon/5320.png"
    #if(rank == "PLATINUM"):
    #    embed.set_image(url="attachment://Iron.png")
    """elif(rank == "BRONZE"):
    elif(rank == "SILVER"):
    elif(rank == "GOLD"):
    elif(rank == "PLATINUM"):
    elif(rank == "DIAMOND"):
    elif(rank == "MASTER"):
    elif(rank == "GRANDMASTER"):
    elif(rank == "CHALLENGER"):"""
    #print(embed.image.height)
    #await ctx.send(file=file, embed=embed)
    async def mainProfile(interaction):
        
        embed = discord.Embed(title=name + "'s Profile")
        description = "Level: " + str(level)
        embed.description = description
        embed.set_thumbnail(url="https://ddragon.leagueoflegends.com/cdn/13.13.1/img/profileicon/" + profileIcon + ".png")
        embed.add_field(name="Top 3 Champion Mastery", value=mastery, inline=False)
        
        await message.edit(attachments=[], embed=embed)
        await interaction.response.defer()




    async def rankedProfile(interaction):
        
        embed = discord.Embed(title=name + "'s Profile")
        description = rank + " " + tier + ": " + str(lp) + " LP" + "\n" + "Wins: " + str(wins) + " Losses: " + str(losses) + "\n" + str(round((wins/(losses+wins))*100, 1)) + "%" + " Winrate"
        embed.description = description
        file = discord.File(str(Path(rank + ".png").absolute()).replace("\\", "/"), filename=rank + ".png")
        embed.set_thumbnail(url="attachment://" + rank + ".png")



        await message.edit(attachments=[file], embed=embed)
        await interaction.response.defer()

    async def spectateProfile(interaction):

        embed = discord.Embed(title=name + "'s Profile")
        description = "Champion: " + champion + "\n" + "Gamemode: " + gameMode

        blueTeam = ""
        redTeam = ""
        for i in participants:
            if(i["teamId"] == 100):
                blueTeam += i["summonerName"] + "\n"
            else:
                redTeam += i["summonerName"] + "\n"
        
        embed.add_field(name=":blue_square: Blue Team", value=blueTeam)
        embed.add_field(name=":red_square: Red Team", value=redTeam)


        embed.description = description
        embed.set_thumbnail(url="https://ddragon.leagueoflegends.com/cdn/13.13.1/img/champion/" + champion + ".png")



        await message.edit(attachments=[], embed=embed)
        await interaction.response.defer()



    mainButton.callback = mainProfile
    rankedButton.callback = rankedProfile
    spectateButton.callback = spectateProfile



    message = await ctx.send(embed=embed, view=view)

    #print(lol_watcher.data_dragon.profile_icons(version, "5292"))



min=0
max=10

@bot.command()
async def mastery(ctx, user):
    masteryList = lol_watcher.champion_mastery.by_summoner("na1", (lol_watcher.summoner.by_name('na1', user))["id"])
    #champNames = list((lol_watcher.data_dragon.champions("13.12.1")["data"]).keys())
    #print(masteryList)
    #print(champNames)
    #min=0
    #max=3
    description = ""


    nextButton = Button(label="Next", style=discord.ButtonStyle.green)
    previousButton = Button(label="Previous", style=discord.ButtonStyle.green)
    view = View()
    view.add_item(nextButton)
    view.add_item(previousButton)

    for i in range(min, max):
        description += str(i+1) + ". " + champList[str((masteryList[i])["championId"])] + " - " + str((masteryList[i])["championPoints"]) + "\n"
    """for i in masteryList:
        champList[str(i["championId"])]"""
    
    embed = discord.Embed(title="Mastery", description=description)
    embed.set_footer(text="Page " + str((min//10)+1) + " of " + str((len(masteryList)//10)+1))

    async def next(interaction):
        """
        min=3 max=6

        index 3,4,5    want 0,1,2
        
        min=6 max=9

        index = 6,7,8 want 0,1,2
        """
        """
        
        1. Talon - 999999
        2. Aphelios - 888888
        3. Diana - 777777
        
        
        """
        global min
        global max
        
        if(max+10 > len(masteryList)):
            min+= 10
            max=len(masteryList)
        else:
            min+=10
            max+=10
        
        description = ""
        for i in range(min,max):
            description += str(i+1) + ". " + champList[str((masteryList[i])["championId"])] + " - " + str((masteryList[i])["championPoints"]) + "\n"
        
        embed = discord.Embed(title="Mastery", description=description)
        embed.set_footer(text="Page " + str((min//10)+1) + " of " + str((len(masteryList)//10)+1))
        
        await message.edit(embed=embed)
        await interaction.response.defer()
    
    async def previous(interaction):
        """
        min=3 max=6

        index 3,4,5    want 0,1,2
        
        min=6 max=9

        index = 6,7,8 want 0,1,2





        1
        2
        3
        4
        5
        6
        7
        8
        9
        10



        11
        12
        13
        14



        """
        global min
        global max
        if(min-10 < 0):
            min=0
            max=10
        elif(max==len(masteryList)):
            max-=max%10
            min-=10
        else:
            min-=10
            max-=10
        description = ""
        for i in range(min,max):
            description += str(i+1) + ". " + champList[str((masteryList[i])["championId"])] + " - " + str((masteryList[i])["championPoints"]) + "\n"
        
        embed = discord.Embed(title="Mastery", description=description)
        embed.set_footer(text="Page " + str((min//10)+1) + " of " + str((len(masteryList)//10)+1))

        await message.edit(embed=embed)
        await interaction.response.defer()

    nextButton.callback = next
    previousButton.callback = previous

    message = await ctx.send(embed=embed, view=view)
    #print((lol_watcher.data_dragon.champions("13.12.1")["data"]))
    #print(masteryList)


@bot.command()
async def cr(ctx):
    print(lol_watcher.champion.rotations("na1"))
    rotation = lol_watcher.champion.rotations("na1")
    allChampIDs = rotation["freeChampionIds"]
    newChampIDs = rotation['freeChampionIdsForNewPlayers']

    embed = discord.Embed(title="Free Champion Rotation")

    description = ""
    for i in allChampIDs:
        description += champList[str(i)] + "\n"
    
    embed.add_field(name="All Players", value=description)

    description=""
    for i in newChampIDs:
        description += champList[str(i)] + "\n"
    
    embed.add_field(name="New Players", value=description)

    await ctx.send(embed=embed)

@bot.command()
async def matchhistory(ctx, user):
    puuid = lol_watcher.summoner.by_name("na1", user)['puuid']
    
    matchIds = lol_watcher.match.matchlist_by_puuid("na1", puuid)
    """match = lol_watcher.match.by_id("na1", 'NA1_4702228372')
    info = match['info']
    participants = info['participants']"""

    embed = discord.Embed(title="Match History")

    stats = None
    for matchId in matchIds:
        match = lol_watcher.match.by_id("na1", matchId)
        info = match['info']
        participants = info['participants']
        for participant in participants:
            if(participant['puuid'] == puuid):
                stats = participant
                name = stats['championName'] + " - " + str(stats['kills']) + "/" + str(stats['deaths']) + "/" + str(stats['assists'])
                mode = "Gamemode: " + info['gameMode']
                kda = str(round((stats['challenges'])['kda']), 2) + " KDA"
                value = mode + "\n" + kda
                embed.add_field(name=name, value=value, inline=False)
  
    #print(stats.keys())
    print(info)

    """participant = participants[0]
    print(participant)"""

    await ctx.send(embed=embed)






@bot.command()
async def status(ctx):

    #embed.add_field(name="Incidents", value=)
    nastatus = lol_watcher.lol_status_v4.platform_data('na1')
    incidents = nastatus['incidents']
    #print(nastatus)
    #print(nastatus['id'])
    #print()
    #print((incidents[0])['maintenance_status'])
    #print((incidents[0])['incident_severity'])

    #print((((((incidents[0])['updates'])[0])['author'])))
    #print((incidents[0])['incident_severity'])
    #print((((((incidents[0])['updates'])[0])['translations'])[0])['content'])
    #print((((((incidents[1])['updates'])[0])['translations'])[0])['content'])
    
    incidentmsg = ""
    
    for i in range(len(incidents)):
        incidentmsg += (((((incidents[i])['updates'])[0])['translations'])[0])['content'] + "\n\n"
        #embed.add_field(name="Incidents", value=(((((incidents[i])['updates'])[0])['translations'])[0])['content'])
    
    if(incidentmsg == ""):
        embed = discord.Embed(title="Server Status", colour=0x07ff03)
        embed.add_field(name="All Clear!", value="No recent issues or events to report")
    else:
        embed = discord.Embed(title="Server Status", colour=0xfbff03)
        embed.add_field(name="Incidents", value=incidentmsg)

    await ctx.send(embed=embed)



    """

    NUMBER OF INCIDENTS ACTIVE
    print(len(incidents))
    NUMBER OF UPDATES ON FIRST INCIDENT
    print(len((incidents[0])['updates']))
    NUMBER OF UPDATES ON SECOND INCIDENT
    print(len((incidents[1])['updates']))
    NUMBER OF TRANSLATIONS AVAILABLE FOR THE DESCRIPTION OF THE UPDATE
    print(len((((incidents[0])['updates'])[0])['translations']))


    """

    """for i in range(len(incidents)):
        embed.add_field()
"""


"""

class Embed(
    *,
    colour: int | Colour | None = None,
    color: int | Colour | None = None,
    title: Any | None = None,
    type: EmbedType = 'rich',
    url: Any | None = None,
    description: Any | None = None,
    timestamp: datetime | None = None
)


"""

#bot.add_command(test)

bot.run("MTExNzIxNTk2ODU5NTI4ODIwNQ.GufZEL.Uob2SAt_SEV1E6_hEq3pnw9Pr4iij_BT-J9400")