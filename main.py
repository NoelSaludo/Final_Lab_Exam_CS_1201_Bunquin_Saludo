from Managers.Dice_game import DiceGame
from Managers.User_Manager import UserManager

def main():
    usermanager = UserManager()
    while True: 
        
        while not usermanager.islogined:
            print ("Welcome to Dice Game!")
            print ("1. Register")
            print ("2. Login")
            print ("3. Exit ")
            try:
                choice = int(input("Enter choice: "))
                if choice == 1:
                    username = ''
                    password = ''
                    while True:
                        username = input ("Enter username: ")
                        if len(username) < 4:
                            print("4 characters needed")
                            continue
                        password = input ("Enter password: ")
                        if len(password) < 8:
                            print("8 characters needed")
                            continue
                        break
                    usermanager.register(username, password)
                    break
                elif choice == 2:
                    username = input ("Enter username: ")
                    password = input ("Enter password: ")
                    usermanager.log_in(username, password)
                elif choice == 3:
                    print ("Exiting game...")
                    break
                else:
                    print ("Invalid Input")
            except ValueError as e:
                print (f"Error Occured {e}")
                
        while usermanager.islogined:
            print (f"""
                   Welcome to Dice Game, {usermanager.curent_user.username}
                    Menu:
                    1. Start Game
                    2. Show Top Scores
                    3. Log Out
                   """)
            dice_game = DiceGame()
            choice = int(input("Enter choice: " ))
            loggedUser = usermanager.curent_user.username
            try:
                if choice == 1:
                    stagepoints = 0
                    while True:
                        cpuScore = dice_game.play_game(usermanager.curent_user)
                        if usermanager.curent_user.score > cpuScore:
                            usermanager.curent_user.score += 3
                            stagepoints += 1
                            print(f"{loggedUser} won this round with a score of {usermanager.curent_user.score}")
                            choice = input("Do you wish to continue (press y to continue): ")
                            if choice.lower() == "y":
                                continue
                            else:
                                break
                        else:
                            print(f"GameOver you have won {stagepoints}")
                            break
                elif choice == 2:
                    dice_game.show_top_scores()
                elif choice == 3:
                    print ("Logging Out")
                    usermanager.log_out()
                    break
            except ValueError as e:
                print (f"Error as occured: {e}")

if __name__ == "__main__":
    main()