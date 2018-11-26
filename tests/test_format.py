from aliceplex.schema import format


def test_remove_trailing_space():
    source = "test \n test  \ntest\n"
    result = "test\n test\ntest"
    assert format.remove_trailing_space(source) == result


def test_remove_leading_space():
    source = " test \n test  \n  test\n"
    result = "test \ntest  \ntest\n"
    assert format.remove_leading_space(source) == result


def test_replace_continuous_newlines():
    source = "test\ntest\n\ntest\n\n\ntest"
    result = "test\ntest\n\ntest\n\ntest"
    assert format.replace_continuous_newlines(source) == result


def test_replace_continuous_space():
    source = "test  test \t test"
    result = "test test test"
    assert format.replace_continuous_space(source) == result


def test_replace_tilde():
    assert format.replace_tilde("~a~") == "〜a〜"


def test_replace_dot():
    assert format.replace_dot(".") == "."
    assert format.replace_dot("..") == "…"
    assert format.replace_dot("...") == "…"
    assert format.replace_dot("....") == "……"
    assert format.replace_dot(".....") == "……"
    assert format.replace_dot("......") == "……"
    assert format.replace_dot("........") == "………"


def test_replace_full_stop():
    assert format.replace_full_stop("a．B") == "a・B"


def test_replace_arrow_brackets():
    assert format.replace_arrow_brackets("<as>") == "〈as〉"


def test_replace_ending_space():
    assert format.replace_ending_space("test?  test! ") == "test?test!"


def test_remove_single_linebreak():
    expected = "Hello\n\nWorld?Test"
    assert format.remove_single_linebreak("Hello\n\nWorld?\nTest") == expected


def test_normalize():
    assert format.normalize("。 \n! ") == "。!"
    assert format.normalize("test.....") == "test……"
    assert format.normalize("Hello     World!") == "Hello World!"
