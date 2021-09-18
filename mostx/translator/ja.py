__all__ = ('Translator', )

from typing import Iterable
from ..datatypes import AdjMat, Choice, Translator as TranslatorBase

PADJ_TEXT = '''
熱/冷た 厚/薄 大き/小さ 新し/古 鋭/鈍 美し/醜 近/遠 高/低 細/太 堅/柔らか
易し/難し 明る/暗 強/弱 速/遅 優し/厳し
'''
PADJS = tuple(tuple(i.split(sep='/', maxsplit=1)) for i in PADJ_TEXT.split())


class Translator(TranslatorBase):
    @property
    def get_max_adjs(self) -> int:
        return len(PADJS)

    def gen_statement(self, a: Choice, b: Choice, adjmats: Iterable[AdjMat]) -> str:
        return '{}は{}より{}い'.format(
            a, b, 'くて'.join(
                PADJS[index][is_fwd_direction]
                for (index, is_fwd_direction) in adjmats
            )
        )

    def gen_mostx_question(self, adjmat: AdjMat) -> str:
        index, is_fwd_direction = adjmat
        return '最も{}いのは?'.format(PADJS[index][is_fwd_direction])

    def gen_sort_request(self, adjmat: AdjMat) -> str:
        index, is_fwd_direction = adjmat
        return '{}い順に並べ替えよ'.format(PADJS[index][is_fwd_direction])
