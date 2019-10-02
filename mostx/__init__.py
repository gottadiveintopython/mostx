__version__ = '0.1.0'
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

    def __init__(self, *, lang:str, random_instance=None):
        import importlib
        import random
        self.lang_module = importlib.import_module('mostx.langs.' + lang)
        self._lang = lang
        self.random_instance = random_instance or random.Random()

    @property
    def lang(self) -> str:
        return self._lang

    @property
    def max_adjectives(self) -> int:
        return self.lang_module.get_max_adjectives()

    def generate(self, *, choices:Iterable[Any], n_adjectives:int) -> Quiz:
        import itertools

        choices = tuple(choices)
        if len(choices) < 2:
            raise ValueError(
                f"At least two choices are required. (was {len(choices)})")
        if n_adjectives < 1:
            raise ValueError(
                f"'n_adjectives' must be 1 or greater. (was {n_adjectives})")
        if n_adjectives > self.max_adjectives:
            raise ValueError(
                f"'n_adjectives' must be {self.max_adjectives} or smaller. "
                f"(was {n_adjectives})")
        lang_module = self.lang_module
        random_instance = self.random_instance
        # 問題文に使用する形容詞を無作為に選ぶ
        indices_of_adj_group = random_instance.sample(range(self.max_adjectives), n_adjectives)
        # 選ばれた形容詞毎にchoices内の要素の順序を決定
        table = []
        for index in indices_of_adj_group:
            order = list(choices)
            random_instance.shuffle(order)
            table.append((index, order,))
        # table = (

        #     for index in random_instance.sample(range(self.max_adjectives), n_adjectives)
        # )
        # choicesの要素を2つ取り出す場合に有り得る組み合わせを求める
        combinations = []
        for combination in itertools.combinations(choices, 2):
            combination = list(combination)  # tupleはShuffle出来ないのでlistに変換
            random_instance.shuffle(combination)
            combinations.append(combination)
        random_instance.shuffle(combinations)
        # --------------------------------------------------------------------
        # 文を生成
        # --------------------------------------------------------------------
        statements = []
        # 定義文(例: AはBより大きい)を生成
        for combination in combinations:
            a, b = combination[0], combination[1],
            adjpart_arg = [(index, order.index(a) < order.index(b),) for (index, order) in table]
            random_instance.shuffle(adjpart_arg)
            statements.append(lang_module.generate_statement(a, b, adjpart_arg))
        # Quizの答えを決定して、質問文(例: 最も大きのは？)を生成
        index, order = random_instance.choice(table)
        answer_index = random_instance.choice([0, -1])
        return Quiz(
            statements=statements,
            question=lang_module.generate_question(index, answer_index == 0),
            answer=order[answer_index],
            choices=choices,
        )
