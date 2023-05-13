import word_chaining
import discord
from play_using_terminal import play_using_terminal

"""
Runs the game main menu"""
if __name__ == '__main__':

    # game main menu
    play_game = word_chaining.WordChainingGame()
    # playgame.start_game()
    waiting_for_mode = True

    print("Select a game mode:")
    print("1 : Use terminal")
    print("2 : run discordbot")

    while(waiting_for_mode):

        mode_choice = input("Please enter option number: ")

        if mode_choice == "1":
            play_using_terminal(play_game)
            waiting_for_mode = False


        elif mode_choice == "2":
            print("discord_bot not created yet, choose another")

        else:
            print(mode_choice == 2)
            print("invalid choice, please choose another")

