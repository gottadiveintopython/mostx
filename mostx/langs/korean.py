__all__ = (
    'get_max_adjectives', 'generate_statement', 'generate_mostx_question',
    'generate_sort_request',
)

ADJ_TEXT = '''
작/크 적/많 짧/길 가볍/무겁 좁/넓 가늘/굵 가깝/멀 춥/덥
쉽/어렵 조용하/시끄럽 예쁘/더럽 맛있/맛없
'''
ADJS = [i.split(sep='/', maxsplit=1) for i in ADJ_TEXT.split()]


def get_max_adjectives():
    return len(ADJS)


def generate_statement(a, b, adjpart):
    return '{}는 {}보다 {}다'.format(
        a, b, '고 '.join(
            ADJS[index][0 if is_fwd_direction else 1]
            for (index, is_fwd_direction) in adjpart
        )
    )


def generate_mostx_question(index, is_fwd_direction):
    return '어느 것이 가장 {}다?'.format(
        ADJS[index][0 if is_fwd_direction else 1]
    )


def generate_sort_request(index, is_fwd_direction):
    adj = ADJS[index]
    if not is_fwd_direction:
        adj = reversed(adj)
    return '{}은 것부터 {} 것까지 순서대로 나열하다'.format(*adj)
