import pytest

@pytest.fixture
def translator():
    from mostx.translator.zh import Translator
    return Translator()


def test_get_max_adjs(translator):
    assert translator.max_adjs > 3


def test_gen_statement(translator):
    gs = translator.gen_statement
    assert 'A比B快' == gs('A', 'B', [(0, False)])
    assert 'A比B高' == gs('A', 'B', [(1, False)])
    assert 'A比B矮' == gs('A', 'B', [(1, True)])
    assert '2比0又矮又快' == gs(2, 0, [(1, True), (0, False)])
    assert '湯唯比A又細又小' == gs('湯唯', 'A', [(5, False), (9, True)])


def test_gen_mostx_question(translator):
    gmq = translator.gen_mostx_question
    assert '哪個最快?' == gmq((0, False))
    assert '哪個最慢?' == gmq((0, True))
    assert '哪個最大?' == gmq((9, False))


def test_gen_sort_request(translator):
    gsr = translator.gen_sort_request
    assert '由快到慢排列' == gsr((0, False))
    assert '由慢到快排列' == gsr((0, True))
    assert '由大到小排列' == gsr((9, False))
