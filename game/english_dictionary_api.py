"""Contains logic for connectin to an english language api used for the game so it can access words.
It uses the api from https://rapidapi.com/uiopuiopuiop3385/api/random-word-api"""
import os
import sys
import requests
# lets python be able to find env variables
from dotenv import load_dotenv

load_dotenv()

"""Always returns a valid English word that will start with given letter."""


def get_word_matching_letter(first_letter):
    url = 'https://random-word-api.p.rapidapi.com/S/{}'.format(first_letter)

    word_dict = send_request(url)

    return word_dict.get('word')


"""
returns a random word. No requirements are needed for the generated word."""


def get_random_word():
    url = 'https://random-word-api.p.rapidapi.com/get_word'

    word_dict = send_request(url)

    return word_dict.get('word')


"""
A generalised Helper-function to send the requests to api. Also checks for the status code, stopping the program if http request was
 not successful """
def send_request(url):
    headers = {
        "X-RapidAPI-Key": os.getenv('API_KEY'),
        "X-RapidAPI-Host": "random-word-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    # convert content to dictionary
    word_dict = response.json()

    if response.status_code != 200:
        print("error, http response status {} exiting code".format(response.status_code))
        print(word_dict.get('message'))
        sys.exit(1)  # stop running game as it can't function without working api requests

    else:
        return word_dict
