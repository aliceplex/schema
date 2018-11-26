from aliceplex.schema import verify


def test_has_diacritics():
    assert not verify.has_diacritics("ご")
    assert verify.has_diacritics("ご")
