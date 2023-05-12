import english_dictionary_api as eng_dict


class WordChainingGame:

    def __init__(self):
        self.players_word = None
        self.computed_word = None
        self.current_last_letter = None

        self.chain_count = 0
        self.not_game_over = True

    def start_game(self):
        print("Enter a word that starts with the last letter of this word!")

        while self.not_game_over:
            self.prepare_next_round()
            self.wait_for_valid_input()

            # because player has added a valid word, put chain count up
            self.chain_count += 1

    """
    Retrieves a new word that matches the last letter of previous word.
    """
    def prepare_next_round(self):
        if self.players_word:
            self.current_last_letter = self.players_word[-1]
            self.computed_word = eng_dict.get_word_matching_letter(self.current_last_letter)

        else:
            self.computed_word = eng_dict.get_random_word()

        # because computer has added its own word
        self.chain_count += 1
        print(self.computed_word)

    """Checks the player's input and makes sure the input is valid.
    A none value is considered the initial first roud."""
    def wait_for_valid_input(self):
        word_not_valid = True

        while word_not_valid:
            self.players_word = input('enter a word: ')

            if len(self.players_word) >= 3 and self.players_word.isalpha():

                # none checks if this is the initial round where no none value  is expected.
                if self.players_word == None or self.computed_word[-1] == self.players_word[0]:
                    word_not_valid = False

                else:
                    print("first letter doesnt match previous word's last letter,game over")
                    self.end_game()
                    self.not_game_over = False
                    break

            else:
                print("only use letters and a word of at least 3 letters long")

    """
    Prints the player's score"""
    def end_game(self):
        print("ended with a chain {} words long".format(self.chain_count))
