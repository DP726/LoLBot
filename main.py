import config

import discord
from discord import app_commands

import random
from riotwatcher import LolWatcher, RiotWatcher
from pathlib import Path

from discord.ui import Button, View, Select
from discord.ext import commands

prefix = "."
intents=discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents, prefix=".")
tree = app_commands.CommandTree(client)

lol_watcher = LolWatcher(config.API_KEY)
riot_watcher = RiotWatcher(config.API_KEY)

version = lol_watcher.data_dragon.versions_for_region('na1')

bot = commands.Bot(command_prefix=prefix, intents=intents)

champList = {'266': 'Aatrox', '103': 'Ahri', '84': 'Akali', '166': 'Akshan', '12': 'Alistar', '799': 'Ambessa', '32': 'Amumu', '34': 'Anivia', '1': 'Annie', '523': 'Aphelios', '22': 'Ashe', '136': 'AurelionSol', '893': 'Aurora', '268': 'Azir', '432': 'Bard', '200': 'Belveth', '53': 'Blitzcrank', '63': 'Brand', '201': 'Braum', '233': 'Briar', '51': 'Caitlyn', '164': 'Camille', '69': 'Cassiopeia', '31': 'Chogath', '42': 'Corki', '122': 'Darius', '131': 'Diana', '119': 'Draven', '36': 'DrMundo', '245': 'Ekko', '60': 'Elise', '28': 'Evelynn', '81': 'Ezreal', '9': 'Fiddlesticks', '114': 'Fiora', '105': 'Fizz', '3': 'Galio', '41': 'Gangplank', '86': 'Garen', '150': 'Gnar', '79': 'Gragas', '104': 'Graves', '887': 'Gwen', '120': 'Hecarim', '74': 'Heimerdinger', '910': 'Hwei', '420': 'Illaoi', '39': 'Irelia', '427': 'Ivern', '40': 'Janna', '59': 'JarvanIV', '24': 'Jax', '126': 'Jayce', '202': 'Jhin', '222': 'Jinx', '145': 'Kaisa', '429': 'Kalista', '43': 'Karma', '30': 'Karthus', '38': 'Kassadin', '55': 'Katarina', '10': 'Kayle', '141': 'Kayn', '85': 'Kennen', '121': 'Khazix', '203': 'Kindred', '240': 'Kled', '96': 'KogMaw', '897': 'KSante', '7': 'Leblanc', '64': 'LeeSin', '89': 'Leona', '876': 'Lillia', '127': 'Lissandra', '805': 'Locke', '236': 'Lucian', '117': 'Lulu', '99': 'Lux', '54': 'Malphite', '90': 'Malzahar', '57': 'Maokai', '11': 'MasterYi', '800': 'Mel', '902': 'Milio', '21': 'MissFortune', '62': 'MonkeyKing', '82': 'Mordekaiser', '25': 'Morgana', '950': 'Naafiri', '267': 'Nami', '75': 'Nasus', '111': 'Nautilus', '518': 'Neeko', '76': 'Nidalee', '895': 'Nilah', '56': 'Nocturne', '20': 'Nunu', '2': 'Olaf', '61': 'Orianna', '516': 'Ornn', '80': 'Pantheon', '78': 'Poppy', '555': 'Pyke', '246': 'Qiyana', '133': 'Quinn', '497': 'Rakan', '33': 'Rammus', '421': 'RekSai', '526': 'Rell', '888': 'Renata', '58': 'Renekton', '107': 'Rengar', '92': 'Riven', '68': 'Rumble', '13': 'Ryze', '360': 'Samira', '113': 'Sejuani', '235': 'Senna', '147': 'Seraphine', '875': 'Sett', '35': 'Shaco', '98': 'Shen', '102': 'Shyvana', '27': 'Singed', '14': 'Sion', '15': 'Sivir', '72': 'Skarner', '901': 'Smolder', '37': 'Sona', '16': 'Soraka', '50': 'Swain', '517': 'Sylas', '134': 'Syndra', '223': 'TahmKench', '163': 'Taliyah', '91': 'Talon', '44': 'Taric', '17': 'Teemo', '412': 'Thresh', '18': 'Tristana', '48': 'Trundle', '23': 'Tryndamere', '4': 'TwistedFate', '29': 'Twitch', '77': 'Udyr', '6': 'Urgot', '110': 'Varus', '67': 'Vayne', '45': 'Veigar', '161': 'Velkoz', '711': 'Vex', '254': 'Vi', '234': 'Viego', '112': 'Viktor', '8': 'Vladimir', '106': 'Volibear', '19': 'Warwick', '498': 'Xayah', '101': 'Xerath', '5': 'XinZhao', '157': 'Yasuo', '777': 'Yone', '83': 'Yorick', '804': 'Yunara', '350': 'Yuumi', '904': 'Zaahen', '154': 'Zac', '238': 'Zed', '221': 'Zeri', '115': 'Ziggs', '26': 'Zilean', '142': 'Zoe', '143': 'Zyra'}

# Retrieve the puuid of the player
def getPuuid(gameName, tag):
    accountData = riot_watcher.account.by_riot_id("AMERICAS", gameName, tag)
    return accountData["puuid"]

# Listens to the ready event and notifies user when it's ready
@client.event
async def on_ready():
    await tree.sync()
    print("Ready")

# Command to see the user's profile
@tree.command()
async def profile(interaction: discord.Interaction, username: str, tag: str):

    puuid = getPuuid(username, tag)
    summonerData = lol_watcher.summoner.by_puuid("na1", puuid)
    summoner = lol_watcher.league.by_puuid('na1', puuid)
    profileIcon = str(summonerData["profileIconId"])
    level = summonerData["summonerLevel"]
    name = username + "#" + tag
    
    mastery = ""
    masteryList = lol_watcher.champion_mastery.by_puuid("na1", puuid)

    if(len(masteryList) > 3):
        for i in range(0,3):
            mastery += str(i+1) + ". " + champList[str((masteryList[i])["championId"])] + " - " + str((masteryList[i])["championPoints"]) + "\n"

    embed = discord.Embed(title=name + "'s Profile")
    description = "Level: " + str(level)
    embed.description = description
    embed.set_thumbnail(url="https://ddragon.leagueoflegends.com/cdn/16.20.1/img/profileicon/" + profileIcon + ".png")
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
        print("NULL")

    try:
        spectateInfo = lol_watcher.spectator.by_summoner("na1", puuid)
        
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
            if(i["puuid"] == puuid):
                champion = champList[str(i["championId"])]

        view.add_item(spectateButton)
    except Exception as e:
        print(f"Error occurred: {e}") 

    # Switches to the main profile of the user
    async def mainProfile(inter):
        
        embed = discord.Embed(title=name + "'s Profile")
        description = "Level: " + str(level)
        embed.description = description
        embed.set_thumbnail(url="https://ddragon.leagueoflegends.com/cdn/16.20.1/img/profileicon/" + profileIcon + ".png")
        embed.add_field(name="Top 3 Champion Mastery", value=mastery, inline=False)
        
        await interaction.edit_original_response(embed=embed, attachments=[])
        await inter.response.defer()

    # Switches to the ranked profile of the user
    async def rankedProfile(inter):
        
        embed = discord.Embed(title=name + "'s Profile") 
        description = rank + " " + tier + ": " + str(lp) + " LP" + "\n" + "Wins: " + str(wins) + " Losses: " + str(losses) + "\n" + str(round((wins/(losses+wins))*100, 1)) + "%" + " Winrate"
        embed.description = description
        file = discord.File(str(Path().absolute()).replace("\\", "/") + "/img/rank/" + rank + ".png", filename=rank + ".png")
        embed.set_thumbnail(url="attachment://" + rank + ".png")

        await interaction.edit_original_response(embed=embed, attachments=[file])
        await inter.response.defer()

    # Switches to the user's live game (if the user is in a live match)
    async def spectateProfile(inter):

        embed = discord.Embed(title=name + "'s Profile")
        description = "Champion: " + champion + "\n" + "Gamemode: " + gameMode

        blueTeam = ""
        redTeam = ""
        for i in participants:
            if(i["teamId"] == 100):
                blueTeam += i["riotId"] + "\n"
            else:
                redTeam += i["riotId"] + "\n"
        
        embed.add_field(name=":blue_square: Blue Team", value=blueTeam)
        embed.add_field(name=":red_square: Red Team", value=redTeam)

        embed.description = description
        embed.set_thumbnail(url="https://ddragon.leagueoflegends.com/cdn/16.20.1/img/champion/" + champion + ".png")

        await interaction.edit_original_response(embed=embed, attachments=[])
        await inter.response.defer()

    mainButton.callback = mainProfile
    rankedButton.callback = rankedProfile
    spectateButton.callback = spectateProfile

    await interaction.response.send_message(embed=embed, view=view)

min=0
max=10

# Command to see the user's full mastery list or mastery on a single champion
@tree.command()
async def mastery(interaction: discord.Interaction, username: str, tag: str, champion: str=None):

    puuid = getPuuid(username, tag)

    name = username + "#" + tag

    if(champion == None):
        masteryList = lol_watcher.champion_mastery.by_puuid("na1", puuid)
        description = ""

        nextButton = Button(label="Next", style=discord.ButtonStyle.green)
        previousButton = Button(label="Previous", style=discord.ButtonStyle.green)
        view = View()
        view.add_item(previousButton)
        view.add_item(nextButton)

        for i in range(min, max):
            description += str(i+1) + ". " + champList[str((masteryList[i])["championId"])] + " - " + str((masteryList[i])["championPoints"]) + "\n"
        
        embed = discord.Embed(title="Mastery", description=description)
        embed.set_footer(text="Page " + str((min//10)+1) + " of " + str((len(masteryList)//10)+1))

        async def next(inter):

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
            
            await interaction.edit_original_response(embed=embed)
            await inter.response.defer()
        
        async def previous(inter):

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

            await interaction.edit_original_response(embed=embed)
            await inter.response.defer()

        nextButton.callback = next
        previousButton.callback = previous

        await interaction.response.send_message(embed=embed, view=view)
    else:
        versionChampion = version["n"]["champion"]

        champion = champion.strip().capitalize()

        if("sol" in champion.lower()):
            champion = "AurelionSol"
        elif("lee" in champion.lower()):
            champion = "LeeSin"
        elif("master" in champion.lower()):
            champion = "MasterYi"
        elif("miss" in champion.lower()):
            champion = "MissFortune"
        elif("fate" in champion.lower()):
            champion = "TwistedFate"
        elif("xin" in champion.lower()):
            champion = "XinZhao"
        elif("ksante" in champion.lower()):
            champion = "KSante"
        elif("kog" in champion.lower()):
            champion = "KogMaw"
        elif("rek" in champion.lower()):
            champion = "RekSai"

        championID = lol_watcher.data_dragon.champions(versionChampion, False)["data"][champion]["key"]

        championMastery = lol_watcher.champion_mastery.by_puuid_by_champion("na1", puuid, int(championID))

        embed=discord.Embed(title=champList[championID] + " Mastery Points", description=name + " has " + str(championMastery["championPoints"]) + " points on " + champList[championID])

        await interaction.response.send_message(embed=embed)

# Command to see the current champion rotation on the live patch
@tree.command()
async def champion_rotation(interaction: discord.Interaction):

    rotation = lol_watcher.champion.rotations("na1")
    allChampIDs = rotation["sr"]
    newChampIDs = rotation["newplayer"]

    embed = discord.Embed(title="Free Champion Rotation")

    description = ""
    for i in allChampIDs:
        description += champList[str(i)] + "\n"
    
    embed.add_field(name="All Players", value=description)

    description=""
    for i in newChampIDs:
        description += champList[str(i)] + "\n"
    
    embed.add_field(name="New Players", value=description)

    await interaction.response.send_message(embed=embed)

# Command to see the user's recent match history (last 20 games)
@tree.command()
async def matchhistory(interaction: discord.Interaction, username: str, tag: str):

    await interaction.response.defer()
    
    puuid = getPuuid(username, tag)
    
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
                kda = str(round((stats['challenges'])['kda'], 2)) + " KDA"
                value = mode + "\n" + kda
                embed.add_field(name=name, value=value, inline=False)

    await interaction.followup.send(embed=embed)

# Command to see the server's health
@tree.command()
async def status(interaction: discord.Interaction):

    nastatus = lol_watcher.lol_status_v4.platform_data('na1')
    incidents = nastatus['incidents']
    
    incidentmsg = ""
    
    for i in range(len(incidents)):
        incidentmsg += (((((incidents[i])['updates'])[0])['translations'])[0])['content'] + "\n\n"
    
    if(incidentmsg == ""):
        embed = discord.Embed(title="Server Status", colour=0x07ff03)
        embed.add_field(name="All Clear!", value="No recent issues or events to report")
    else:
        embed = discord.Embed(title="Server Status", colour=0xfbff03)
        embed.add_field(name="Incidents", value=incidentmsg)

    await interaction.response.send_message(embed=embed)

client.run(config.TOKEN)