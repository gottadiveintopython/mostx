import pytest

@pytest.fixture()
def qgen():
    import random
    from mostx import QuizGenerator
    return QuizGenerator(lang='ja', random=random.Random(0))


def test_wrong_argument(qgen):
    with pytest.raises(ValueError):
        qgen.gen_mostx_quiz(choices='AB', n_adjs=0)
    with pytest.raises(ValueError):
        qgen.gen_mostx_quiz(choices='AB', n_adjs=-1)
    with pytest.raises(ValueError):
        qgen.gen_mostx_quiz(choices='AB', n_adjs=qgen.max_adjs + 1)
    with pytest.raises(ValueError):
        qgen.gen_mostx_quiz(choices='', n_adjs=1)
    with pytest.raises(ValueError):
        qgen.gen_mostx_quiz(choices='A', n_adjs=1)


def test_one_adjective(qgen):
    q = qgen.gen_mostx_quiz(choices=range(3), n_adjs=1)
    assert tuple(q.choices) == (0, 1, 2)
    assert q.answer == 0
    assert tuple(q.statements) == \
        ('2は0より遅い', '1は0より遅い', '2は1より速い')
    assert q.question == '最も速いのは?'


def test_two_adjectives(qgen):
    q = qgen.gen_mostx_quiz(choices='AB', n_adjs=2)
    assert tuple(q.choices) == ('A', 'B')
    assert q.answer == 'B'
    assert tuple(q.statements) == ('BはAより遅くて遠い', )
    assert q.question == '最も遠いのは?'
