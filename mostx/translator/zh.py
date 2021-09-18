__all__ = ('Translator', )

from typing import List
from ..datatypes import AdjMat, Choice, Translator as TranslatorProtocol

PADJ_TEXT = '''
快/慢 高/矮 早/晚 寬/窄 厚/薄 細/粗 容易/難 好/壞 長/短 大/小 熱/冷 新/舊
近/遠 貴/便宜 美/醜
'''
PADJS = [i.split(sep='/', maxsplit=1) for i in PADJ_TEXT.split()]


class Translator(TranslatorProtocol):
    @property
    def max_adjs(self) -> int:
        return len(PADJS)

    def gen_statement(self, a: Choice, b: Choice, adjmats: List[AdjMat]) -> str:
        if len(adjmats) == 1:
            idx, is_fwd = adjmats[0]
            return f'{a}比{b}{PADJS[idx][is_fwd]}'
        else:
            return '{}比{}又{}'.format(
                a, b, '又'.join(
                    PADJS[idx][is_fwd]
                    for (idx, is_fwd) in adjmats
                )
            )

    def gen_mostx_question(self, adjmat: AdjMat) -> str:
        idx, is_fwd = adjmat
        return f'哪個最{PADJS[idx][is_fwd]}?'

    def gen_sort_request(self, adjmat: AdjMat) -> str:
        idx, is_fwd = adjmat
        from_, to_ = PADJS[idx]
        if is_fwd:
            from_, to_ = to_, from_
        return f'由{from_}到{to_}排列'
