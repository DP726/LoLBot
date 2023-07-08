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

@bot.command()
async def profile(ctx, user):

    user = user.replace("_", " ")

    summonerID = (lol_watcher.summoner.by_name('na1', user))["id"]
    summoner = lol_watcher.league.by_summoner('na1', summonerID)
    profileIcon = str((lol_watcher.summoner.by_name('na1', user))["profileIconId"])
    level = (lol_watcher.summoner.by_name('na1', user))["summonerLevel"]
    name = (lol_watcher.summoner.by_name('na1', user))["name"]
    
    mastery = ""
    masteryList = lol_watcher.champion_mastery.by_summoner("na1", summonerID)

    if(len(masteryList) > 3):
        for i in range(0,3):
            mastery += str(i+1) + ". " + champList[str((masteryList[i])["championId"])] + " - " + str((masteryList[i])["championPoints"]) + "\n"

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

        participants = spectateInfo["participants"]
        for i in participants:
            if(i["summonerId"] == summonerID):
                champion = champList[str(i["championId"])]






        view.add_item(spectateButton)
    except:
        print("FALSEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

    
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

min=0
max=10

@bot.command()
async def mastery(ctx, user):
    masteryList = lol_watcher.champion_mastery.by_summoner("na1", (lol_watcher.summoner.by_name('na1', user))["id"])
    description = ""

    nextButton = Button(label="Next", style=discord.ButtonStyle.green)
    previousButton = Button(label="Previous", style=discord.ButtonStyle.green)
    view = View()
    view.add_item(nextButton)
    view.add_item(previousButton)

    for i in range(min, max):
        description += str(i+1) + ". " + champList[str((masteryList[i])["championId"])] + " - " + str((masteryList[i])["championPoints"]) + "\n"
    
    embed = discord.Embed(title="Mastery", description=description)
    embed.set_footer(text="Page " + str((min//10)+1) + " of " + str((len(masteryList)//10)+1))

    async def next(interaction):

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
  

    print(info)

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

bot.run("MTExNzIxNTk2ODU5NTI4ODIwNQ.GufZEL.Uob2SAt_SEV1E6_hEq3pnw9Pr4iij_BT-J9400")