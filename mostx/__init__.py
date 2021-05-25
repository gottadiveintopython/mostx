__all__ = (
    'get_available_langs', 'QuizGenerator', 'MostxQuiz', 'SortQuiz',
)
import itertools
import random as random_module
from dataclasses import dataclass
from typing import Iterable, Any, Sequence


def get_available_langs() -> Iterable[str]:
    return ('japanese', 'korean', 'chinese', 'english', )


@dataclass
class MostxQuiz:
    statements: Sequence[str]
    question: str
    choices: Sequence[Any]
    answer: Any


@dataclass
class SortQuiz:
    statements: Sequence[str]
    request: str
    choices: Sequence[Any]
    answer: Sequence[Any]


class QuizGenerator:

    def __init__(self, *, lang='english', random=random_module):
        import importlib
        self.lang_module = importlib.import_module('mostx.langs.' + lang)
        self._lang = lang
        self.random = random

    @property
    def lang(self) -> str:
        return self._lang

    @property
    def max_adjs(self) -> int:
        return self.lang_module.get_max_adjectives()

    def __call__(self, *args, **kwargs) -> MostxQuiz:
        import warnings
        warnings.warn(
            r"'QuizGenerator.__call__()' is deprecated, "
            r"use 'QuizGenerator.gen_mostx_quiz()' instead.")
        return self.gen_mostx_quiz(*args, **kwargs)

    def gen_mostx_quiz(self, *, choices: Iterable[Any], n_adjs: int) \
            -> MostxQuiz:
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
            a, b = combination
            adjpart_arg = [
                (index, order.index(a) < order.index(b), )
                for (index, order) in table
            ]
            random.shuffle(adjpart_arg)
            statements.append(lang_module.generate_statement(
                a, b, adjpart_arg))

        # 問題の答えを決めて、質問文(例: 最も大きのは？)を生成
        index, order = random.choice(table)
        answer_index = random.choice([0, -1])
        return MostxQuiz(
            statements=statements,
            question=lang_module.generate_mostx_question(
                index, answer_index == 0),
            answer=order[answer_index],
            choices=choices,
        )

    def gen_sort_quiz(self, *, choices: Iterable[Any], n_adjs: int) \
            -> SortQuiz:
        choices = tuple(choices)
        n_choices = len(choices)
        if n_choices < 3:
            raise ValueError(
                f"At least three choices are required. (was {n_choices})")
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
            (adj_idx, random.sample(choices, n_choices))
            for adj_idx in random.sample(range(self.max_adjs), n_adjs)
        )

        # choicesの要素を2つ取り出す場合に有り得る組み合わせを求める
        combinations = [
            random.sample(c, 2) for c in itertools.combinations(choices, 2)
        ]
        random.shuffle(combinations)

        # 定義文(例: AはBより大きい)を生成
        statements = []
        for combination in combinations:
            a, b = combination
            adjpart_arg = [
                (adj_idx, order.index(a) < order.index(b), )
                for adj_idx, order in table
            ]
            random.shuffle(adjpart_arg)
            statements.append(lang_module.generate_statement(
                a, b, adjpart_arg))

        # 問題の答えを決めてから命令文(例: 小さい順に並べ替えよ)を生成
        adj_idx, order = random.choice(table)
        is_fwd_direction = random.random() > 0.5
        return SortQuiz(
            statements=statements,
            request=lang_module.generate_sort_request(
                adj_idx, is_fwd_direction),
            answer=(order if is_fwd_direction else tuple(reversed(order))),
            choices=choices,
        )
