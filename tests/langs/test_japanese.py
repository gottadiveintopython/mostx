import pytest


def test_get_max_adj():
    from mostx.langs.japanese import get_max_adjectives
    assert get_max_adjectives() >= 1


def test_generate_statement():
    from mostx.langs.japanese import generate_statement as gs
    assert 'AはBより熱い' == gs('A', 'B', [(0, True)])
    assert 'AはBより厚い' == gs('A', 'B', [(1, True)])
    assert 'AはBより薄い' == gs('A', 'B', [(1, False)])
    assert '2は0より薄くて熱い' == gs(2, 0, [(1, False), (0, True)])
    assert '湯唯はAより美しくて柔らかい' == gs('湯唯', 'A', [(5, True), (9, False)])


def test_generate_question():
    from mostx.langs.japanese import generate_question as gq
    assert '最も熱いのは?' == gq(0, True)
    assert '最も冷たいのは?' == gq(0, False)
    assert '最も堅いのは?' == gq(9, True)
