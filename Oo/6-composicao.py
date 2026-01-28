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

class GameStudio():
  def __init__(self, name=""):
    self.name = name
    self.games = []
    
  def add_game(self, game):
    self.games.append(game)
    
  def evaluate_studio_quality(self):
    total_notes = sum(game.note for game in self.games)
    num_games = len(self.games)
    if num_games == 0:
      print(f"Ainda não lançou jogo: {self.name}")
    else:
      average_note = total_notes / num_games
      print(f"Avarege: {average_note:.2f}")



  
game1 = Game("GTA", 2025, True, 9.9)
game2 = Game("JOGO2", 2040, False, 7.9)
game3 = Game("JOGO3", 2021, True, 9.1)

studio = GameStudio("WERbertRichard")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality()

for game in studio.games:
  game.technical_sheet()

