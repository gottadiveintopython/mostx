def test_get_max_adj():
    from mostx.langs.korean import get_max_adjectives
    assert get_max_adjectives() >= 1


def test_generate_statement():
    from mostx.langs.korean import generate_statement as gs
    assert 'A는 B보다 작다' == gs('A', 'B', [(0, True)])
    assert 'A는 B보다 적다' == gs('A', 'B', [(1, True)])
    assert 'A는 B보다 많다' == gs('A', 'B', [(1, False)])
    assert '2는 0보다 많고 작다' == gs(2, 0, [(1, False), (0, True)])
    assert '湯唯는 A보다 가늘고 시끄럽다' == gs('湯唯', 'A', [(5, True), (9, False)])


def test_generate_mostx_question():
    from mostx.langs.korean import generate_mostx_question as gq
    assert '어느 것이 가장 작다?' == gq(0, True)
    assert '어느 것이 가장 크다?' == gq(0, False)
    assert '어느 것이 가장 조용하다?' == gq(9, True)


def test_generate_sort_request():
    from mostx.langs.korean import generate_sort_request as gsc
    assert '크은 것부터 작 것까지 순서대로 나열하다' == gsc(0, False)
