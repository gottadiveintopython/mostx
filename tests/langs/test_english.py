import pytest


def test_get_max_adjectives():
    from mostx.langs.english import get_max_adjectives
    assert get_max_adjectives() >= 1


def test_generate_statement():
    from mostx.langs.english import generate_statement as gs
    assert 'A is smaller than B' == gs('A', 'B', [(0, True)])
    assert 'A is longer than B' == gs('A', 'B', [(1, True)])
    assert 'A is shorter than B' == gs('A', 'B', [(1, False)])
    assert '2 is shorter and smaller than 0' == \
        gs(2, 0, [(1, False), (0, True)])
    assert '湯唯 is nearer,noisier and shorter than A' == \
        gs('湯唯', 'A', [(5, True), (9, False), (1, False)])


def test_generate_mostx_question():
    from mostx.langs.english import generate_mostx_question as gq
    assert 'Which is the smallest?' == gq(0, True)
    assert 'Which is the largest?' == gq(0, False)
    assert 'Which is the quietest?' == gq(9, True)
