import asyncio
import word_chaining
#import sys
#sys.path.append('') #trying to remove this caused a ModuleNotFoundError: No module named 'bot_for_game'
#from bot_for_game.chain_bot import *

from dotenv import load_dotenv
from play_using_terminal import play_using_terminal


load_dotenv()


"""
Runs the game main menu"""
def main():

    #nested in the main block so it can be seen by code in here.
    async def running_a_botgame(play_game):
        await wake_up_bot(play_game)

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
            waiting_for_mode = False
            play_using_terminal(play_game)

        elif mode_choice == "2":
            print("WARNING, discord_bot not fully implemented yet")
            waiting_for_mode = False

            #create a coroutine object
            #running_a_botgame  = running_a_botgame(play_game)
            #command it to run the corouting object
            #asyncio.run(running_a_botgame)


        else:
            print(mode_choice == 2)
            print("invalid choice, please choose another")


main()