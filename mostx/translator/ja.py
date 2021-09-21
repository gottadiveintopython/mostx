__all__ = ('Translator', )

from typing import List
from ..datatypes import AdjMat, Choice, Translator as TranslatorProtocol

PADJ_TEXT = '''
熱/冷た 厚/薄 大き/小さ 新し/古 鋭/鈍 美し/醜 近/遠 高/低 細/太 堅/柔らか
易し/難し 明る/暗 強/弱 速/遅 優し/厳し 楽し/悲し
'''
PADJS = tuple(tuple(i.split(sep='/', maxsplit=1)) for i in PADJ_TEXT.split())


class Translator(TranslatorProtocol):
    @property
    def max_adjs(self) -> int:
        return len(PADJS)

    def gen_statement(self, a: Choice, b: Choice, adjmats: List[AdjMat]) -> str:
        return '{}は{}より{}い'.format(
            a, b, 'くて'.join(
                PADJS[idx][is_fwd]
                for (idx, is_fwd) in adjmats
            )
        )

    def gen_mostx_question(self, adjmat: AdjMat) -> str:
        idx, is_fwd = adjmat
        return '最も{}いのは?'.format(PADJS[idx][is_fwd])

    def gen_sort_request(self, adjmat: AdjMat) -> str:
        idx, is_fwd = adjmat
        return '{}い順に並べ替えよ'.format(PADJS[idx][is_fwd])
