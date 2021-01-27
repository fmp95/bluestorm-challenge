from bluestorm_app.common import WordChecker

checker = WordChecker()


def test_split():

    word = "tyl enol"

    assert "tylenol" == checker.get_correction(word)


def test_delete():

    word = "tlenol"

    assert "tylenol" == checker.get_correction(word)


def test_transpose():

    word = "tlyenol"

    assert "tylenol" == checker.get_correction(word)


def test_replace():

    word = "tilenol"

    assert "tylenol" == checker.get_correction(word)


def test_insert():

    word = "tiylenol"

    assert "tylenol" == checker.get_correction(word)