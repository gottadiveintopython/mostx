import pytest


def test_wrong_argument():
    import mostx
    qgen = mostx.QuizGenerator(lang='japanese')
    with pytest.raises(ValueError):
        q = qgen(choices='AB', n_adjs=0)
    with pytest.raises(ValueError):
        q = qgen(choices='AB', n_adjs=-1)
    with pytest.raises(ValueError):
        q = qgen(choices='AB', n_adjs=qgen.max_adjs + 1)
    with pytest.raises(ValueError):
        q = qgen(choices='', n_adjs=1)
    with pytest.raises(ValueError):
        q = qgen(choices='A', n_adjs=1)


def test_one_adjective():
    import random
    import mostx
    qgen = mostx.QuizGenerator(lang='japanese', random=random.Random(0))
    q = qgen(choices=range(3), n_adjs=1)
    assert tuple(q.choices) == (0, 1, 2)
    assert q.answer == 0
    assert tuple(q.statements) == \
        ('2は0より速い', '1は0より速い', '2は1より遅い')
    assert q.question == '最も遅いのは?'


def test_two_adjectives():
    import random
    import mostx
    qgen = mostx.QuizGenerator(lang='japanese', random=random.Random(100))
    q = qgen(choices='AB', n_adjs=2)
    assert tuple(q.choices) == ('A', 'B')
    assert q.answer == 'A'
    assert tuple(q.statements) == ('BはAより高くて大きい', )
    assert q.question == '最も小さいのは?'
