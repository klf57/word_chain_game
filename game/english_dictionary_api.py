"""Contains logic for connectin to an english language api used for the game so it can access words.
It uses the api from https://rapidapi.com/uiopuiop3385/api/random-word-api"""
import requests
import os

"""Always returns a valid English word that will start with given letter."""
def get_word_matching_letter(first_letter):

    url = 'https://random-word-api.p.rapidapi.com/S/{}'.format(first_letter)

    #required to gain access to api.
    headers = {
        "X-RapidAPI-Key": os.getenv("API_KEY"),
        "X-RapidAPI-Host": "random-word-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    # convert content to dictionary
    word_dict = response.json()
    return word_dict.get('word')


def get_random_word():
    url = 'https://random-word-api.p.rapidapi.com/get_word'

    headers = {
        "X-RapidAPI-Key": os.getenv("API_KEY"),
        "X-RapidAPI-Host": "random-word-api.p.rapidapi.com"
    }

    response = requests.get(url, headers = headers)
    # convert content to dictionary
    word_dict = response.json()
    return word_dict.get('word')



