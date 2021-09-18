__all__ = ('Translator', )

from typing import List
from ..datatypes import AdjMat, Choice, Translator as TranslatorProtocol

PADJ_TEXT = '''
작/크 적/많 짧/길 가볍/무겁 좁/넓 가늘/굵 가깝/멀 춥/덥
쉽/어렵 조용하/시끄럽 예쁘/더럽 맛있/맛없
'''
PADJS = [i.split(sep='/', maxsplit=1) for i in PADJ_TEXT.split()]


class Translator(TranslatorProtocol):
    @property
    def max_adjs(self) -> int:
        return len(PADJS)

    def gen_statement(self, a: Choice, b: Choice, adjmats: List[AdjMat]) -> str:
        return '{}는 {}보다 {}다'.format(
            a, b, '고 '.join(
                PADJS[idx][is_fwd]
                for (idx, is_fwd) in adjmats
            )
        )

    def gen_mostx_question(self, adjmat: AdjMat) -> str:
        idx, is_fwd = adjmat
        return f'어느 것이 가장 {PADJS[idx][is_fwd]}다?'

    def gen_sort_request(self, adjmat: AdjMat) -> str:
        idx, is_fwd = adjmat
        from_, to_ = PADJS[idx]
        if is_fwd:
            from_, to_ = to_, from_
        return f'{from_}은 것부터 {to_} 것까지 순서대로 나열하다'
