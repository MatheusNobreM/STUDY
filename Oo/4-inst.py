class Game:
  total_games = 0
  def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
    self.name = name
    self.yearLaunch = yearLaunch
    self.multiplayer = multiplayer
    self.note = note
    self.totalEvaluation = 0
    self.evaluators = 0
    Game.total_games +=1
  
  def __str__(self):
    return f"Game: {self.name}"
  
  def technical_sheet(self):
    print(game1.name)
    print(game1.yearLaunch)
    print(game1.multiplayer)
    print(game1.note)
    
  def evaluate(self, note):
    self.totalEvaluation += note
    self.evaluators += 1
  
  def average(self):
    print(f"Média: {self.name} : {self.totalEvaluation / self.evaluators}")
    
  

game1 = Game("GTA", 2025, True, 9.9)

game1.evaluate(9.0)
game1.evaluate(7)

game1.average()

print(Game.total_games)