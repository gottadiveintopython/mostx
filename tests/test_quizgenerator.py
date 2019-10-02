import pytest


def test_wrong_argument():
    import mostx
    qgen = mostx.QuizGenerator(lang='japanese')
    with pytest.raises(ValueError):
        q = qgen.generate(choices='AB', n_adjectives=0)
    with pytest.raises(ValueError):
        q = qgen.generate(choices='AB', n_adjectives=-1)
    with pytest.raises(ValueError):
        q = qgen.generate(choices='AB', n_adjectives=qgen.max_adjectives + 1)
    with pytest.raises(ValueError):
        q = qgen.generate(choices='', n_adjectives=1)
    with pytest.raises(ValueError):
        q = qgen.generate(choices='A', n_adjectives=1)


def test_one_adjective():
    import random
    import mostx
    qgen = mostx.QuizGenerator(
        lang='japanese',
        random_instance=random.Random(0),
    )
    q = qgen.generate(choices=range(3), n_adjectives=1)
    assert tuple(q.choices) == (0, 1, 2)
    assert q.answer == 1
    assert tuple(q.statements) == \
        ('1は0より遅い', '1は2より遅い', '0は2より速い')
    assert q.question == '最も遅いのは?'


def test_two_adjectives():
    import random
    import mostx
    qgen = mostx.QuizGenerator(
        lang='japanese',
        random_instance=random.Random(100),
    )
    q = qgen.generate(choices='AB', n_adjectives=2)
    assert tuple(q.choices) == ('A', 'B')
    assert q.answer == 'B'
    assert tuple(q.statements) == ('AはBより大きくて低い', )
    assert q.question == '最も高いのは?'
