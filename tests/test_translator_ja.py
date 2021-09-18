import pytest

@pytest.fixture
def translator():
    from mostx.translator.ja import Translator
    return Translator()


def test_get_max_adjs(translator):
    assert translator.max_adjs > 3


def test_gen_statement(translator):
    gs = translator.gen_statement
    assert 'AはBより熱い' == gs('A', 'B', [(0, False)])
    assert 'AはBより厚い' == gs('A', 'B', [(1, False)])
    assert 'AはBより薄い' == gs('A', 'B', [(1, True)])
    assert '2は0より薄くて熱い' == gs(2, 0, [(1, True), (0, False)])
    assert '湯唯はAより美しくて柔らかい' == gs('湯唯', 'A', [(5, False), (9, True)])


def test_gen_mostx_question(translator):
    gmq = translator.gen_mostx_question
    assert '最も熱いのは?' == gmq((0, False))
    assert '最も冷たいのは?' == gmq((0, True))
    assert '最も堅いのは?' == gmq((9, False))


def test_gen_sort_request(translator):
    gsr = translator.gen_sort_request
    assert '熱い順に並べ替えよ' == gsr((0, False))
    assert '冷たい順に並べ替えよ' == gsr((0, True))
    assert '堅い順に並べ替えよ' == gsr((9, False))
