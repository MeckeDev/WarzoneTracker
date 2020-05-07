function get_random() {
  eel.getRandom()(function(x) {document.getElementById("location").value = x}) 
}

function addFields() {
  var mode = document.getElementById("Gamemodes");
  var gamemode = mode.options[mode.selectedIndex].text;

  eel.addUi(gamemode)(function(x) { document.getElementById("fields").innerHTML = x })
  showMatches()
}

function showPlayers() {
  var mode = document.getElementById("Gamemodes");
  var gamemode = mode.options[mode.selectedIndex].text;

  eel.playerStats(gamemode)(function(x) {document.getElementById("playerStats").innerHTML = x})
}

function showMatches() {
  var mode = document.getElementById("Gamemodes");
  var gamemode = mode.options[mode.selectedIndex].text;
  document.getElementById("playerStats").innerHTML = ""
  eel.showMatches(gamemode)(function(x) {document.getElementById("playerStats").innerHTML = x})
}

function addName() {
  var name = document.getElementById("newName").value
  eel.addName(name)
}

function reset() {
  document.getElementById("reset").innerHTML = '<input type="button" class="btn btn-success btn-lg btn-block" onclick="reset_no()" value="Cancel"> <input type="button" class="btn btn-danger btn-lg btn-block" onclick="reset_yes()" value="I want to Reset">'
}

function reset_yes() {
  eel.reset_all()
  reset_no()
  addFields()
}

function reset_no() {
  document.getElementById("reset").innerHTML = '<input type="button" class="btn btn-danger btn-lg btn-block" onclick="reset(), addFields()" value="Reset All">'
  addFields()
}

function addMatch() {

  var mode = document.getElementById("Gamemodes");
  var gamemode = mode.options[mode.selectedIndex].text;

  var solo = gamemode.includes("Solo")
  var duo = gamemode.includes("Duo")
  var trio = gamemode.includes("Trio")
  var quad = gamemode.includes("Quad")
  
  if (solo) {
    
    var names = document.getElementById("Names_1");
    var name_1 = names.options[names.selectedIndex].text;

    kill_1 = document.getElementById("kills_1").value
    position_1 = document.getElementById("position_1").value
    score_1 = document.getElementById("score_1").value
  
    console.log(name_1, kill_1, position_1, score_1)

    var player_1 = [name_1, kill_1, position_1, score_1 ] 
    eel.addMatch(gamemode, player_1)
  }
  else if (duo) {
    
    var names = document.getElementById("Names_1");
    var name_1 = names.options[names.selectedIndex].text;
    
    kill_1 = document.getElementById("kills_1").value
    position_1 = document.getElementById("position_1").value
    score_1 = document.getElementById("score_1").value
  
    var player_1 = [name_1, kill_1, position_1, score_1 ] 


    var names = document.getElementById("Names_2");
    var name_2 = names.options[names.selectedIndex].text;

    kill_2 = document.getElementById("kills_2").value
    position_2 = document.getElementById("position_2").value
    score_2 = document.getElementById("score_2").value

    var player_2 = [name_2, kill_2, position_2, score_2 ] 

    eel.addMatch(gamemode, player_1, player_2)
  }

  else if (trio) {
    
    var names = document.getElementById("Names_1");
    var name_1 = names.options[names.selectedIndex].text;
    
    kill_1 = document.getElementById("kills_1").value
    position_1 = document.getElementById("position_1").value
    score_1 = document.getElementById("score_1").value
  
    var player_1 = [name_1, kill_1, position_1, score_1 ] 


    var names = document.getElementById("Names_2");
    var name_2 = names.options[names.selectedIndex].text;

    kill_2 = document.getElementById("kills_2").value
    position_2 = document.getElementById("position_2").value
    score_2 = document.getElementById("score_2").value

    var player_2 = [name_2, kill_2, position_2, score_2 ] 


    var names = document.getElementById("Names_3");
    var name_3 = names.options[names.selectedIndex].text;

    kill_3 = document.getElementById("kills_3").value
    position_3 = document.getElementById("position_3").value
    score_3 = document.getElementById("score_3").value

    var player_3 = [ name_3, kill_3, position_3, score_3 ] 

    eel.addMatch(gamemode, player_1, player_2, player_3)
  }

  else if (quad) {
    
    var names = document.getElementById("Names_1");
    var name_1 = names.options[names.selectedIndex].text;
    
    kill_1 = document.getElementById("kills_1").value
    position_1 = document.getElementById("position_1").value
    score_1 = document.getElementById("score_1").value
  
    var player_1 = [name_1, kill_1, position_1, score_1 ] 


    var names = document.getElementById("Names_2");
    var name_2 = names.options[names.selectedIndex].text;

    kill_2 = document.getElementById("kills_2").value
    position_2 = document.getElementById("position_2").value
    score_2 = document.getElementById("score_2").value

    var player_2 = [name_2, kill_2, position_2, score_2 ] 


    var names = document.getElementById("Names_3");
    var name_3 = names.options[names.selectedIndex].text;

    kill_3 = document.getElementById("kills_3").value
    position_3 = document.getElementById("position_3").value
    score_3 = document.getElementById("score_3").value

    var player_3 = [ name_3, kill_3, position_3, score_3 ] 


    var names = document.getElementById("Names_4");
    var name_4 = names.options[names.selectedIndex].text;

    kill_4 = document.getElementById("kills_4").value
    position_4 = document.getElementById("position_4").value
    score_4 = document.getElementById("score_4").value

    var player_4 = [ name_4, kill_4, position_4, score_4 ] 

    eel.addMatch(gamemode, player_1, player_2, player_3, player_4)
  }
}