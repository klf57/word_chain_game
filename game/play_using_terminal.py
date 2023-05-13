def play_using_terminal(game_session):

    print("Enter a word that starts with the last letter of this word!")
    while game_session.not_game_over:
        game_session.prepare_next_round()
        game_session.wait_for_valid_input()
