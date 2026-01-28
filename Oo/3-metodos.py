class Game:
  def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
    self.name = name
    self.yearLaunch = yearLaunch
    self.multiplayer = multiplayer
    self.note = note
  
  def __str__(self):
    return f"Game: {self.name}"
  
  
game1 = Game("GTA", 2025, True, 9.9)

print(game1.note)