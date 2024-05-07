import datetime
import random
from Models.User import User
class DiceGame():
        
    
    def load_scores():
        pass
    
    def save_scores():
        pass
    
    def play_game(self, player):
            turns = 0
            cpuScore = 0
            while turns < 4:
                playerDice ,cpuDice = random.randrange(1,7), random.randrange(1,7)
                print(f"{player.username} rolled: {playerDice}")
                print(f"CPU rolled: {cpuDice}")
                if playerDice > cpuDice:
                    print(f"{player.username} won the turn")
                    player.score += 1
                elif playerDice < cpuDice:
                    print(f"CPU won this turn")
                    cpuScore += 1
                else:
                    print("the turn is a tie")
                turns += 1
            return cpuScore
                
    
    def show_top_scores():
        pass
    
    