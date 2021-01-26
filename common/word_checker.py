from json import dump
from os.path import isfile, join

from pandas import read_csv
from spellchecker import SpellChecker

FILE_PATH = join("files", "word_frequency.json")


class WordChecker:
    def __init__(self):
        self.spell = SpellChecker(language=None, distance=2)

        if isfile(FILE_PATH):
            self.spell.word_frequency.load_dictionary(FILE_PATH)
        else:
            self.create_word_frequency_file()
            self.spell.word_frequency.load_dictionary(FILE_PATH)

    def create_word_frequency_file(self):

        file = read_csv(
            "files/products.txt",
            delimiter="~",
            usecols=["Trade_Name"],
        )

        words = self.get_frequency(file).to_dict()

        with open(FILE_PATH, "w") as output_file:
            dump(words, output_file)

    def get_frequency(self, dataframe):

        frequency = dataframe["Trade_Name"].str.split(";").explode()
        frequency = frequency.str.split(" ").explode()
        frequency = frequency.str.lower()
        frequency = frequency.groupby(by=frequency).count()
        frequency = frequency.sort_values(ascending=False)

        return frequency

    def get_correction(self, word):
        return self.spell.correction(word.lower())

    def get_candidates(self, word):
        return self.spell.candidates(word.lower())