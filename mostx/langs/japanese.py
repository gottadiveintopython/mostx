__all__ = ('get_max_adjectives', 'generate_statement', 'generate_question', )


ADJ_TEXT = '''
熱/冷た 厚/薄 大き/小さ 新し/古 鋭/鈍 美し/醜 近/遠 高/低 細/太 堅/柔らか
易し/難し 明る/暗 強/弱 速/遅 優し/厳し
'''
ADJS = [i.split(sep='/', maxsplit=1) for i in ADJ_TEXT.split()]


def get_max_adjectives():
    return len(ADJS)


def generate_statement(a, b, adjpart):
    return '{}は{}より{}い'.format(
        a, b, 'くて'.join(
            [ADJS[index][0 if is_fwd_direction else 1]
            for (index, is_fwd_direction) in adjpart]
        )
    )


def generate_question(index, is_fwd_direction):
    return '最も{}いのは?'.format(
        ADJS[index][0 if is_fwd_direction else 1]
    )
