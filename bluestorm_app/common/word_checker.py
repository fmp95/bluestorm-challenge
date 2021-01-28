from json import dump
from os.path import isfile, join

from pandas import read_csv
from spellchecker import SpellChecker

from settings import DATABASE_FILE_PATH, WORD_FREQUENCY_FILE_PATH
from ..logs import common_logs


class WordChecker:
    def __init__(self):
        self.spell = SpellChecker(language=None, distance=2)

        if isfile(WORD_FREQUENCY_FILE_PATH):
            self.spell.word_frequency.load_dictionary(WORD_FREQUENCY_FILE_PATH)
        else:
            self.create_word_frequency_file()
            self.spell.word_frequency.load_dictionary(WORD_FREQUENCY_FILE_PATH)

    def create_word_frequency_file(self):

        file = read_csv(
            DATABASE_FILE_PATH,
            delimiter="~",
            usecols=["Trade_Name"],
        )

        words = self.get_frequency(file).to_dict()

        with open(WORD_FREQUENCY_FILE_PATH, "w") as output_file:
            dump(words, output_file)
            common_logs.info(f"Word Frequency File Created Successfully!")

    def get_frequency(self, dataframe):

        frequency = dataframe["Trade_Name"].str.split(";").explode()
        frequency = frequency.str.split(" ").explode()
        frequency = frequency.str.lower()
        frequency = frequency.groupby(by=frequency).count()
        frequency = frequency.sort_values(ascending=False)

        return frequency

    def get_correction(self, word):

        corrected = self.spell.correction(word.lower())

        common_logs.info(f"(Word corrected) Before: {word} | After: {corrected}")
        return corrected