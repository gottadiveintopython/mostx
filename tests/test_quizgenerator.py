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
