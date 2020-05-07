import eel
import random
import json
import requests
from json2table import convert

eel.init('web')

@eel.expose
def reset_all():
    matches = '{ "Matches": { "Solo BR": {}, "Duo BR": {}, "Trio BR": {}, "Quad BR": {}, "Solo Plunder": {}, "Duo Plunder": {}, "Trio Plunder": {}, "Quad Plunder": {} }}'
    players = '{"Players" : {} }'

    with open("matches.json", "w") as f:
        f.write(matches)
    f.close()

    with open("players.json", "w") as f:
        f.write(players)
    f.close()

@eel.expose
def addUi(x):

    gamemodes = ["Solo BR", "Duo BR", "Trio BR", "Quad BR", "Solo Plunder", "Duo Plunder", "Trio Plunder", "Quad Plunder"]

    i = 0
    with open("players.json", "r") as f:
        players = json.load(f)
    f.close()

    fields = ""

    if "Solo" in x:
        for i in range(1):

            names = f"<select class=\"NameList form-control\" name=\"Names\" id=\"Names_{i+1}\">"
            for name in players["Players"]:
                names += f"<option> {name} </option>"
            names += "</select>"

            fields += f"<form> <div class=\"row\"> <div class=\"col\"> {names}  </div> <div class=\"col\"> <input class=\"field form-control\" type=\"number\" id=\"kills_{i+1}\" placeholder=\"Kills\"> </div> <div class=\"col\"> <input class=\"field form-control\" type=\"number\" id=\"position_{i+1}\" placeholder=\"Position\"> </div> <div class=\"col\"> <input class=\"field form-control\" type=\"number\" id=\"score_{i+1}\" placeholder=\"Score\"> </div> </div> </form> </br>"
    
    elif "Duo" in x:
        for i in range(2):

            names = f"<select class=\"NameList form-control\" name=\"Names\" id=\"Names_{i+1}\">"
            for name in players["Players"]:
                names += f"<option> {name} </option>"
            names += "</select>"

            fields += f"<form> <div class=\"row\"> <div class=\"col\"> {names}  </div> <div class=\"col\"> <input class=\"field form-control\" type=\"number\" id=\"kills_{i+1}\" placeholder=\"Kills\"> </div> <div class=\"col\"> <input class=\"field form-control\" type=\"number\" id=\"position_{i+1}\" placeholder=\"Position\"> </div> <div class=\"col\"> <input class=\"field form-control\" type=\"number\" id=\"score_{i+1}\" placeholder=\"Score\"> </div> </div> </form> </br>"
    
    elif "Trio" in x:
        for i in range(3):

            names = f"<select class=\"NameList form-control\" name=\"Names\" id=\"Names_{i+1}\">"
            for name in players["Players"]:
                names += f"<option> {name} </option>"
            names += "</select>"

            fields += f"<form> <div class=\"row\"> <div class=\"col\"> {names}  </div> <div class=\"col\"> <input class=\"field form-control\" type=\"number\" id=\"kills_{i+1}\" placeholder=\"Kills\"> </div> <div class=\"col\"> <input class=\"field form-control\" type=\"number\" id=\"position_{i+1}\" placeholder=\"Position\"> </div> <div class=\"col\"> <input class=\"field form-control\" type=\"number\" id=\"score_{i+1}\" placeholder=\"Score\"> </div> </div> </form> </br>"
    
    elif "Quad" in x:
        for i in range(4):

            names = f"<select class=\"NameList form-control\" name=\"Names\" id=\"Names_{i+1}\">"
            for name in players["Players"]:
                names += f"<option> {name} </option>"
            names += "</select>"

            fields += f"<form> <div class=\"row\"> <div class=\"col\"> {names}  </div> <div class=\"col\"> <input class=\"field form-control\" type=\"number\" id=\"kills_{i+1}\" placeholder=\"Kills\"> </div> <div class=\"col\"> <input class=\"field form-control\" type=\"number\" id=\"position_{i+1}\" placeholder=\"Position\"> </div> <div class=\"col\"> <input class=\"field form-control\" type=\"number\" id=\"score_{i+1}\" placeholder=\"Score\"> </div> </div> </form> </br>"
    
    return fields

@eel.expose
def playerStats(mode):

    with open("players.json", "r") as f:
        players = json.load(f)
    f.close()

    i = 1

    table = f"""<h1 class=\"blockquote text-center h1\"> {mode} </h1>
    <form> 
      <div class="row"> 
        <div class="col"> <input type="button" class="form-control" value="show Matches" onclick="showMatches()"> </div>
        <div class="col"><input type="button" class="form-control" value="show Players" onclick="showPlayers()"> </div>
      </div>
    </form>"""

    table += "</br><table class=\"table table-info\"> <tr> <th>Name</th> <th>total Kills</th> <th>best Position</th> <th>most Kills</th> <th>highest Score</th> </tr>"
    
    for player in players["Players"]:
        p = players["Players"][player]
        if i%2 == 0:
            table += f'<tr class="bg-primary">'
        else:
            table += f'<tr class="bg-success">'

        table += f'<td> { player } </td> <td> { p["Kills"] } </td> <td> { p["best Position"] } </td> <td> { p["most Kills"] } </td> <td> { p["highest Score"] } </td> </tr>'
        i += 1
    table += "</table>"
    
    return table

@eel.expose
def showMatches(mode):

    with open("matches.json", "r") as f:
        matches = json.load(f)
    f.close()

    rs = 1

    if "Solo" in mode:
        rs = 1
    if "Duo" in mode:
        rs = 2
    if "Trio" in mode:
        rs = 3
    if "Quad" in mode:
        rs = 4

    table = f"""<h1 class=\"blockquote text-center h1\"> {mode} </h1>
    <form> 
      <div class="row"> 
        <div class="col"> <input type="button" class="form-control" value="show Matches" onclick="showMatches()"> </div>
        <div class="col"><input type="button" class="form-control" value="show Players" onclick="showPlayers()"> </div>
      </div>
    </form>"""

    table += f"</br><table class=\"table table-info\"> <thead> <tr> <th>Round</th> <th>Players</th> <th>Kills</th> <th>Position</th> <th>Score</th> </tr> </thead>"
    
    i = 1
    m = matches["Matches"][mode]
    for r in m:
        x = f"{i}"
        if i%2 == 0:
            table += f'<tr class="bg-primary"> <td rowspan="{rs}"> { x } </td>'
        else:
            table += f'<tr class="bg-success"> <td rowspan="{rs}"> { x } </td>'
        if rs == 1:
            for pl in m[x]:
                table += f'<td> { m[x][pl] } </td>'
            table += f'</tr>'
        elif rs > 1:
            for pl in m[x]:
                table += f'<td> { pl } </td> <td> { m[x][pl]["Kills"] } </td> <td> { m[x][pl]["Position"] } </td> <td> { m[x][pl]["Score"] } </td></tr>'
            table += f'</tr>'
        i += 1

    table += "</table>"
    
    return table

@eel.expose
def addMatch(mode, p1, p2=None, p3=None, p4=None):
    u = 0

    if "Solo" in mode:

        u = 1
        with open("matches.json" , "r") as f:
            matches = json.load(f)
        f.close()

        p = 0
        for x in matches["Matches"][mode]:
            p += 1

        matches["Matches"][mode][p+1] = { "Name": p1[0], "Kills" : p1[1], "Position" : p1[2], "Score" : p1[3] }

        with open("matches.json", "w") as f:
            json.dump(matches, f, indent=4)
        f.close()

    elif "Duo" in mode:
        
        u = 2
        with open("matches.json" , "r") as f:
            matches = json.load(f)
        f.close()

        p = 0
        for x in matches["Matches"][mode]:
            p += 1
        print(p)

        matches["Matches"][mode][p+1] = { p1[0] : { "Kills" : p1[1], "Position" : p1[2], "Score" : p1[3] },  p2[0] : {"Kills" : p2[1], "Position" : p2[2], "Score" : p2[3] }}

        with open("matches.json", "w") as f:
            json.dump(matches, f, indent=4)
        f.close()

    elif "Trio" in mode:
        
        u = 3
        with open("matches.json" , "r") as f:
            matches = json.load(f)
        f.close()

        p = 0
        for x in matches["Matches"][mode]:
            p += 1
        print(p)

        matches["Matches"][mode][p+1] = { p1[0] : { "Kills" : p1[1], "Position" : p1[2], "Score" : p1[3] },  p2[0] : {"Kills" : p2[1], "Position" : p2[2], "Score" : p2[3] }, p3[0] : { "Kills" : p3[1], "Position" : p3[2], "Score" : p3[3] }}

        with open("matches.json", "w") as f:
            json.dump(matches, f, indent=4)
        f.close()

    elif "Quad" in mode:
        
        u = 4
        with open("matches.json" , "r") as f:
            matches = json.load(f)
        f.close()

        p = 0
        for x in matches["Matches"][mode]:
            p += 1
        print(p)

        matches["Matches"][mode][p+1] = { p1[0] : { "Kills" : p1[1], "Position" : p1[2], "Score" : p1[3] },  p2[0] : {"Kills" : p2[1], "Position" : p2[2], "Score" : p2[3] }, p3[0] : { "Kills" : p3[1], "Position" : p3[2], "Score" : p3[3] }, p4[0] : { "Kills" : p4[1], "Position" : p4[2], "Score" : p4[3] }}

        with open("matches.json", "w") as f:
            json.dump(matches, f, indent=4)
        f.close()

    with open("players.json", "r") as f:
        players = json.load(f)
    f.close()

    
    players['Players'][p1[0]]['Kills'] += int(p1[1])

    if int(p1[2]) < players['Players'][p1[0]]['best Position']:
        players['Players'][p1[0]]['best Position'] = int(p1[2])
    
    if players['Players'][p1[0]]['most Kills'] < int(p1[1]):
        players['Players'][p1[0]]['most Kills'] = int(p1[1])
    
    if players['Players'][p1[0]]['highest Score'] < int(p1[3]):
        players['Players'][p1[0]]['highest Score'] = int(p1[3])

    if u > 1:
        players['Players'][p2[0]]['Kills'] += int(p2[1])
        pos = players['Players'][p2[0]]['best Position']
        new = int(p2[2])

        if new < pos:
            players['Players'][p2[0]]['best Position']= new

        if players['Players'][p2[0]]['most Kills'] < int(p2[1]):
            players['Players'][p2[0]]['most Kills'] = int(p2[1])
        
        if players['Players'][p2[0]]['highest Score'] < int(p2[3]):
            players['Players'][p2[0]]['highest Score'] = int(p2[3])

    if u > 2:
        players['Players'][p3[0]]['Kills'] += int(p3[1])
        pos = players['Players'][p3[0]]['best Position']
        new = int(p3[2])

        if new < pos:
            players['Players'][p3[0]]['best Position']= new

        if players['Players'][p3[0]]['most Kills'] < int(p3[1]):
            players['Players'][p3[0]]['most Kills'] = int(p3[1])
                
        if players['Players'][p3[0]]['highest Score'] < int(p3[3]):
            players['Players'][p3[0]]['highest Score'] = int(p3[3])


    if u > 3:
        players['Players'][p4[0]]['Kills'] += int(p4[1])
        pos = players['Players'][p4[0]]['best Position']
        new = int(p4[2])

        if new < pos:
            players['Players'][p4[0]]['best Position']= new

        if players['Players'][p4[0]]['most Kills'] < int(p4[1]):
            players['Players'][p4[0]]['most Kills'] = int(p4[1])
      
        if players['Players'][p4[0]]['highest Score'] < int(p4[3]):
            players['Players'][p4[0]]['highest Score'] = int(p4[3])


    with open("players.json", "w") as f:
        json.dump(players, f, indent=4)
    f.close()

@eel.expose
def addName(name):
    with open("players.json", "r") as f:
        players = json.load(f)
    f.close()

    names = []
    for player in players["Players"]:
        names.append(player)

    if name not in names:
        players["Players"][name] = { "Kills" : 0, "best Position" : 150, "most Kills" : 0, "highest Score" : 0 }

        with open("players.json", "w") as f:
            json.dump(players, f, indent=4)
        f.close()

    return 0

@eel.expose
def getRandom():
    
    locations = ["Airport", "Boneyard", "Dam", "Downtown", "Farmland", "Hills", "Hospital", "Lumber", "Military Base", "Park", "Port", "Prison", "Promenade West", "Promenade East", "Stadium", "Storage Town", "Superstore", "Train Station", "TV Station", "Quarry"]
    loc = len(locations)-1
    x = random.randint(0, loc)

    return locations[x]

eel.start('index.html')
