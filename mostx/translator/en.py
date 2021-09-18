__all__ = ('Translator', )

from typing import List
from ..datatypes import AdjMat, Choice, Translator as TranslatorProtocol

PADJ_TEXT = '''
small/larg long/short cold/hott new/old fast/slow near/farth hard/soft
fatt/thinn sadd/happi quiet/noisi
'''
PADJS = tuple(tuple(i.split(sep='/', maxsplit=1)) for i in PADJ_TEXT.split())


class Translator(TranslatorProtocol):
    @property
    def max_adjs(self) -> int:
        return len(PADJS)


    def gen_statement(self, a: Choice, b: Choice, adjmats: List[AdjMat]) -> str:
        if len(adjmats) == 1:
            idx, is_fwd = adjmats[0]
            return f'{a} is {PADJS[idx][is_fwd]}er than {b}'
        else:
            adjs = [
                PADJS[idx][is_fwd] + 'er'
                for (idx, is_fwd) in adjmats
            ]
            last_adj = adjs.pop()
            return f"{a} is {','.join(adjs)} and {last_adj} than {b}"


    def gen_mostx_question(self, adjmat: AdjMat) -> str:
        idx, is_fwd = adjmat
        return f'Which is the {PADJS[idx][is_fwd]}est?'


    def gen_sort_request(self, adjmat: AdjMat) -> str:
        idx, is_fwd = adjmat
        from_, to_ = PADJS[idx]
        if is_fwd:
            from_, to_ = to_, from_
        return f'Put from {from_}est to {to_}est'
