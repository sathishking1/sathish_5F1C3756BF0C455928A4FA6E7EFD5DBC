class Player:
  def Play(self):
      print("The Player is Playing cricket.")
    
class Batsman(Player):
    def Play(self):
        print("The batsman is       batting.")
        
class Bowler(Player):
  
    def Play(self):
        print("The bowler is bowling.")
                 
batsman = Batsman()
bowler = Bowler()


batsman.Play()
bowler.Play()