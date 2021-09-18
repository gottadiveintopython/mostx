__all__ = ('get_available_langs', 'QuizGenerator', )
import itertools
from functools import lru_cache
from typing import Iterable
import random as random_module
from .datatypes import SortQuiz, MostxQuiz, Translator, Choice

LANGS = ('ja', 'ko', 'zh', 'en', )


def get_available_langs() -> Iterable[str]:
    return LANGS


@lru_cache(maxsize=None)
def get_translator(lang: str) -> Translator:
    import importlib
    return importlib.import_module('mostx.translator.' + lang).Translator()


class QuizGenerator:
    def __init__(self, *, lang='en', random=random_module):
        self._lang = lang
        self._translator = get_translator(lang)
        self._random = random

    @property
    def lang(self) -> str:
        return self._lang

    @property
    def max_adjs(self) -> int:
        return self._translator.max_adjs

    def gen_mostx_quiz(self, *, choices: Iterable[Choice], n_adjs: int) -> MostxQuiz:
        choices = tuple(choices)
        n_choices = len(choices)
        if n_choices < 2:
            raise ValueError(f"At least two choices are required. (was {n_choices})")
        if n_adjs < 1:
            raise ValueError(f"'n_adjs' must be 1 or greater. (was {n_adjs})")
        if n_adjs > self.max_adjs:
            raise ValueError(f"'n_adjs' must be {self.max_adjs} or smaller. (was {n_adjs})")
        translator = self._translator
        random = self._random

        # 無作為に選んだ形容詞組それぞれにおいて順序を決定
        #
        # table = (
        #     (3, ['C', 'B', 'A', ], ),
        #     (0, ['A', 'B', 'C', ], ),
        #     (2, ['C', 'A', 'B', ], ),
        # )
        table = tuple(
            (adjp_idx, random.sample(choices, n_choices))
            for adjp_idx in random.sample(range(self.max_adjs), n_adjs)
        )

        # 答えの選択肢を2つ取り出す場合に有り得る組み合わせを求める
        #
        # combinations = [
        #     ['A', 'C'],
        #     ['B', 'C'],
        #     ['B', 'A'],
        # ]
        combinations = [
            random.sample(c, 2)
            for c in itertools.combinations(choices, 2)
        ]
        random.shuffle(combinations)

        # 定義文を生成
        #
        # statements = (
        #     'AはBより大きい',
        #     'CはBより小さい',
        #     'AはCより大きい',
        # )
        statements = tuple(
            (
                adjmats := [
                    (adjp_idx, order.index(a) < order.index(b), )
                    for (adjp_idx, order) in table
                ],
                random.shuffle(adjmats),
            ) and translator.gen_statement(a, b, adjmats)
            for a, b in combinations
        )

        # 問題の答えを決めて、質問文(例: 最も大きのは？)を生成
        adjp_idx, order = random.choice(table)
        answer_idx = random.choice((0, -1))
        return MostxQuiz(
            statements=statements,
            question=translator.gen_mostx_question((adjp_idx, answer_idx == 0)),
            answer=order[answer_idx],
            choices=choices,
        )

    def gen_sort_quiz(self, *, choices: Iterable[Choice], n_adjs: int) -> SortQuiz:
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
        translator = self.translator
        random = self.random

        # 無作為に選んだ形容詞それぞれにおいて順序を決定
        table = tuple(
            (adj_idx, random.sample(choices, n_choices))
            for adj_idx in random.sample(range(self.max_adjs), n_adjs)
        )

        # choicesの要素を2つ取り出す場合に有り得る組み合わせを求める
        combinations = [
            random.sample(c, 2)
            for c in itertools.combinations(choices, 2)
        ]
        random.shuffle(combinations)

        # 定義文(例: AはBより大きい)を生成
        statements = []
        for combination in combinations:
            a, b = combination
            adjmats = [
                (adj_idx, order.index(a) < order.index(b), )
                for adj_idx, order in table
            ]
            random.shuffle(adjmats)
            statements.append(translator.generate_statement(
                a, b, adjmats))

        # 問題の答えを決めてから命令文(例: 小さい順に並べ替えよ)を生成
        adj_idx, order = random.choice(table)
        is_fwd_direction = random.random() > 0.5
        return SortQuiz(
            statements=statements,
            request=translator.generate_sort_request(
                adj_idx, is_fwd_direction),
            answer=(order if is_fwd_direction else tuple(reversed(order))),
            choices=choices,
        )
