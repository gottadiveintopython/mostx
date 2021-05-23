__all__ = ('get_max_adjectives', 'generate_statement', 'generate_question', )


ADJ_TEXT = '''
small/larg long/short cold/hott new/old fast/slow near/farth hard/soft
fatt/thinn sadd/happi quiet/noisi
'''
ADJS = tuple(tuple(i.split(sep='/', maxsplit=1)) for i in ADJ_TEXT.split())


def get_max_adjectives():
    return len(ADJS)


def generate_statement(a, b, adjpart):
    if len(adjpart) == 1:
        (index, is_fwd_direction) = adjpart[0]
        return r'{0} is {2}er than {1}'.format(
            a, b, ADJS[index][0 if is_fwd_direction else 1],
        )
    else:
        adjs = [
            ADJS[index][0 if is_fwd_direction else 1] + 'er'
            for (index, is_fwd_direction) in adjpart
        ]
        last_adj = adjs.pop()
        return f"{a} is {','.join(adjs)} and {last_adj} than {b}"


def generate_question(index, is_fwd_direction):
    return r'Which is the {}est?'.format(
        ADJS[index][0 if is_fwd_direction else 1]
    )
