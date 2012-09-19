import os
import random

from flask import Flask


app = Flask(__name__)


class WordNet(object):

    def __init__(self, path='.'):
        self.verbs = tuple(self.load_words(path, 'verb'))
        self.nouns = tuple(self.load_words(path, 'noun'))

    def load_words(self, path, category):
        words = set()
        filename = os.path.join(path, 'index.' + category)
        with open(filename) as data:
            for line in data:
                word = line.split(None, 1)[0]
                if not word.isalpha():
                    continue
                words.add(word)
        return words

    def random_slug(self):
        verb = random.choice(self.verbs)
        noun = random.choice(self.nouns)
        return "{0} {1}".format(verb, noun)

wordnet = WordNet('data')


@app.route('/')
def index():
    return wordnet.random_slug()


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
