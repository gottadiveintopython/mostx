def test_get_max_adj():
    from mostx.langs.chinese import get_max_adjectives
    assert get_max_adjectives() >= 1


def test_generate_statement():
    from mostx.langs.chinese import generate_statement as gs
    assert 'A比B快' == gs('A', 'B', [(0, True)])
    assert 'A比B高' == gs('A', 'B', [(1, True)])
    assert 'A比B矮' == gs('A', 'B', [(1, False)])
    assert '2比0又矮又快' == gs(2, 0, [(1, False), (0, True)])
    assert '湯唯比A又細又小' == gs('湯唯', 'A', [(5, True), (9, False)])


def test_generate_mostx_question():
    from mostx.langs.chinese import generate_mostx_question as gq
    assert '哪個最快?' == gq(0, True)
    assert '哪個最慢?' == gq(0, False)
    assert '哪個最大?' == gq(9, True)


def test_generate_sort_request():
    from mostx.langs.chinese import generate_sort_request as gsc
    assert '由快到慢排列' == gsc(0, True)
    assert '由慢到快排列' == gsc(0, False)
    assert '由大到小排列' == gsc(9, True)
