__all__ = ('get_max_adjectives', 'generate_statement', 'generate_question', )


ADJ_TEXT = '''
快/慢 高/矮 早/晚 寬/窄 厚/薄 細/粗 容易/難 好/壞 長/短 大/小 熱/冷 新/舊
近/遠 貴/便宜 美/醜
'''
ADJS = [i.split(sep='/', maxsplit=1) for i in ADJ_TEXT.split()]


def get_max_adjectives():
    return len(ADJS)


def generate_statement(a, b, adjpart):
    if len(adjpart) == 1:
        (index, is_fwd_direction,) = adjpart[0]
        return f'{a}比{b}{ADJS[index][0 if is_fwd_direction else 1]}'
    else:
        return '{}比{}又{}'.format(
            a, b, '又'.join(
                [ADJS[index][0 if is_fwd_direction else 1]
                for (index, is_fwd_direction) in adjpart]
            )
        )


def generate_question(index, is_fwd_direction):
    return f'哪個最{ADJS[index][0 if is_fwd_direction else 1]}?'
