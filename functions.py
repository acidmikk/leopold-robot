import requests, os

word_and_synonims = []
words_discription = []


def update():
    url = os.environ.get('URL', None)
    response = requests.get(url).json()
    word_list = response['data']
    for word in word_list:
        word_and_synonims.append([word['attributes']['main'],
                                  *word['attributes']['synonims'][:]])
        words_discription.append(word['attributes']['description'])