__all__ = ('get_available_langs', 'Quiz', 'QuizGenerator', )
import dataclasses
from typing import Iterable, Any, Sequence


def get_available_langs() -> Iterable[str]:
    return ('japanese', 'korean', 'chinese', 'english', )


@dataclasses.dataclass
class Quiz:
    statements: Sequence[str]
    question: str
    choices: Sequence[Any]
    answer: Any


class QuizGenerator:

    def __init__(self, *, lang:str, random=None):
        import importlib
        import random as random_module
        self.lang_module = importlib.import_module('mostx.langs.' + lang)
        self._lang = lang
        self.random = random or random_module

    @property
    def lang(self) -> str:
        return self._lang

    @property
    def max_adjs(self) -> int:
        return self.lang_module.get_max_adjectives()

    def __call__(self, *, choices:Iterable[Any], n_adjs:int) -> Quiz:
        import itertools

        choices = tuple(choices)
        n_choices = len(choices)
        if n_choices < 2:
            raise ValueError(
                f"At least two choices are required. (was {n_choices})")
        if n_adjs < 1:
            raise ValueError(
                f"'n_adjs' must be 1 or greater. (was {n_adjs})")
        if n_adjs > self.max_adjs:
            raise ValueError(
                f"'n_adjs' must be {self.max_adjs} or smaller. "
                f"(was {n_adjs})")
        lang_module = self.lang_module
        random = self.random

        # 無作為に選んだ形容詞それぞれにおいて順序を決定
        table = tuple(
            (index, random.sample(choices, n_choices))
            for index in random.sample(range(self.max_adjs), n_adjs)
        )

        # choicesの要素を2つ取り出す場合に有り得る組み合わせを求める
        combinations = [
            random.sample(c, 2) for c in itertools.combinations(choices, 2)
        ]
        random.shuffle(combinations)

        # 定義文(例: AはBより大きい)を生成
        statements = []
        for combination in combinations:
            a, b = combination[0], combination[1],
            adjpart_arg = [(index, order.index(a) < order.index(b),) for (index, order) in table]
            random.shuffle(adjpart_arg)
            statements.append(lang_module.generate_statement(a, b, adjpart_arg))

        # 問題の答えを決めて、質問文(例: 最も大きのは？)を生成
        index, order = random.choice(table)
        answer_index = random.choice([0, -1])
        return Quiz(
            statements=statements,
            question=lang_module.generate_question(index, answer_index == 0),
            answer=order[answer_index],
            choices=choices,
        )
