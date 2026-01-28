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
    print(self.name)
    print(self.yearLaunch)
    print(self.multiplayer)
    print(self.note)
    
  def evaluate(self, note):
    self.totalEvaluation += note
    self.evaluators += 1
  
  def average(self):
    print(f"Média: {self.name} : {self.totalEvaluation / self.evaluators}")
    
  
class SinglePlayerGame(Game):
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0, storyLine=""):
      super().__init__(name, yearLaunch, multiplayer=False, note=note)
      self.storyLine = storyLine
      
    def technical_sheet(self):
      super().technical_sheet()
      print(f"Enredo: {self.storyLine}\n")

singlePlayer = SinglePlayerGame("só", 2020, 8, "triste")
singlePlayer.technical_sheet()

  
  
game1 = Game("GTA", 2025, True, 9.9)

