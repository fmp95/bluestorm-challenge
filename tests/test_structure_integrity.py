from os.path import isfile

from pytest import fixture

from settings import DATABASE_FILE_PATH
from bluestorm_app.common import WordChecker

checker = WordChecker()


@fixture
def check_file_existence():
    return isfile(DATABASE_FILE_PATH)


def test_database_file():
    assert isfile(DATABASE_FILE_PATH)


def test_dictionary_creation(check_file_existence):
    checker.create_word_frequency_file()
