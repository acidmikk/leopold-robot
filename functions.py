import requests, os

word_and_synonims = []
words_discription = []
real_name = []
url = os.environ.get('URL', None)


def update():
    response = requests.get(url).json()
    word_list = response['data']
    for word in word_list:
        real_name.append(word['attributes']['main'].lower())
        word_and_synonims.append([word['attributes']['main'].lower(),
                                  *list(map(lambda x: x.lower(), word['attributes']['synonims']))])
        words_discription.append(word['attributes']['description'])