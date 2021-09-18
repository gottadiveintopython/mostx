__all__ = (
    'PAdjIdx', 'AdjMat', 'Choice', 'Translator', 'MostxQuiz', 'SortQuiz',
)
from typing import Protocol, Iterable, Tuple, NewType, Any, Sequence
from dataclasses import dataclass


PAdjIdx = NewType('PAdjIdx', int)
'''
'PAdj' stands for paired-adjectives.
PAdjは「大きい/小さい」のような対になった反対の意味の形容詞を意味する。
各Translatorモジュールは複数のPadjを持っていて、その中の一つを指すのにPAdjIdxを用いる。
'''

AdjMat = Tuple[PAdjIdx, bool]
'''
'AdjMat' stands for Adjective Material.
形容詞を特定するのに必要な情報。例えばPAdjsIdx=0が「熱い/冷たい」を指しているなら、
(0, True, )と(0, False, )がそれぞれ「熱い」「冷たい」のどれかを指す事になる。
'''

Choice = Any
'''
問題の答えの選択肢
'''


class Translator(Protocol):
    @property
    def get_max_adjs(self) -> int:
        '''
        一つの定義文の中で利用可能な形容詞の最大数。``PAdjIdx``の値はこの値未満である必要がある。
        '''

    def gen_statement(self, a: Choice, b: Choice, adjmats: Iterable[AdjMat], /) -> str:
        '''
        「AはBより熱くて遠い」といった感じの定義文を作る。
        '''

    def gen_mostx_question(self, adjmat: AdjMat) -> str:
        '''
        「最も大きのは？」といった感じの質問文を作る。
        '''

    def gen_sort_request(self, adjmat: AdjMat) -> str:
        '''
        「小さい順に並べ替えよ」といった感じの命令文を作る。
        '''


@dataclass
class MostxQuiz:
    statements: Sequence[str]
    question: str
    choices: Sequence[Choice]
    answer: Choice


@dataclass
class SortQuiz:
    statements: Sequence[str]
    request: str
    choices: Sequence[Choice]
    answer: Sequence[Choice]
