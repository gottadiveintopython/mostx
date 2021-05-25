__all__ = (
    'get_max_adjectives', 'generate_statement', 'generate_mostx_question',
)

from typing import Tuple, Iterable

ADJ_TEXT = '''
熱/冷た 厚/薄 大き/小さ 新し/古 鋭/鈍 美し/醜 近/遠 高/低 細/太 堅/柔らか
易し/難し 明る/暗 強/弱 速/遅 優し/厳し
'''
ADJS = tuple(tuple(i.split(sep='/', maxsplit=1)) for i in ADJ_TEXT.split())


def get_max_adjectives():
    return len(ADJS)


def generate_statement(
        a: str, b: str, adjpart: Iterable[Tuple[int, bool]]) -> str:
    '''
    「AはBより熱くて遠い」といった感じの文を作る。
    '''
    return '{}は{}より{}い'.format(
        a, b, 'くて'.join(
            ADJS[index][0 if is_fwd_direction else 1]
            for (index, is_fwd_direction) in adjpart
        )
    )


def generate_mostx_question(index, is_fwd_direction):
    '''
    「最も大きのは？」といった感じの質問文を作る。
    '''
    return '最も{}いのは?'.format(ADJS[index][0 if is_fwd_direction else 1])
