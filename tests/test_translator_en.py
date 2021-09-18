import pytest

@pytest.fixture
def translator():
    from mostx.translator.en import Translator
    return Translator()


def test_get_max_adjs(translator):
    assert translator.max_adjs > 3


def test_gen_statement(translator):
    gs = translator.gen_statement
    assert 'A is smaller than B' == gs('A', 'B', [(0, False)])
    assert 'A is longer than B' == gs('A', 'B', [(1, False)])
    assert 'A is shorter than B' == gs('A', 'B', [(1, True)])
    assert '2 is shorter and smaller than 0' == gs(2, 0, [(1, True), (0, False)])
    assert '湯唯 is nearer,noisier and shorter than A' == gs('湯唯', 'A', [(5, False), (9, True), (1, True)])


def test_gen_mostx_question(translator):
    gmq = translator.gen_mostx_question
    assert 'Which is the smallest?' == gmq((0, False))
    assert 'Which is the largest?' == gmq((0, True))
    assert 'Which is the quietest?' == gmq((9, False))


def test_gen_sort_request(translator):
    gsr = translator.gen_sort_request
    assert 'Put from smallest to largest' == gsr((0, False))
    assert 'Put from largest to smallest' == gsr((0, True))
    assert 'Put from quietest to noisiest' == gsr((9, False))
