import pytest

@pytest.fixture
def translator():
    from mostx.translator.ko import Translator
    return Translator()


def test_get_max_adjs(translator):
    assert translator.max_adjs > 3


def test_gen_statement(translator):
    gs = translator.gen_statement
    assert 'A는 B보다 작다' == gs('A', 'B', [(0, False)])
    assert 'A는 B보다 적다' == gs('A', 'B', [(1, False)])
    assert 'A는 B보다 많다' == gs('A', 'B', [(1, True)])
    assert '2는 0보다 많고 작다' == gs(2, 0, [(1, True), (0, False)])
    assert '湯唯는 A보다 가늘고 시끄럽다' == gs('湯唯', 'A', [(5, False), (9, True)])


def test_gen_mostx_question(translator):
    gmq = translator.gen_mostx_question
    assert '어느 것이 가장 작다?' == gmq((0, False))
    assert '어느 것이 가장 크다?' == gmq((0, True))
    assert '어느 것이 가장 조용하다?' == gmq((9, False))


def test_gen_sort_request(translator):
    gsr = translator.gen_sort_request
    assert '크은 것부터 작 것까지 순서대로 나열하다' == gsr((0, True))
