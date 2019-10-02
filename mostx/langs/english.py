__all__ = ('get_max_adjectives', 'generate_statement', 'generate_question', )


ADJ_TEXT = '''
smaller,smallest/larger,largest
longer,longest/shorter,shortest
colder,coldest/hotter,hottest
newer,newest/older,oldest
faster,fastest/slower,slowest
nearer,nearest/farther,farthest
harder,hardest/softer,softest
fatter,fattest/thinner,thinnest
sadder,saddest/happier,happiest
quieter,quietest/noisier,noisiest
'''
ADJS = tuple(
    tuple(map(lambda s: s.split(','), line.split(sep='/')))
    for line in ADJ_TEXT.split()
)


def get_max_adjectives():
    return len(ADJS)


def generate_statement(a, b, adjpart):
    if len(adjpart) == 1:
        (index, is_fwd_direction) = adjpart[0]
        return f'{a} is {ADJS[index][0 if is_fwd_direction else 1][0]} than {b}'
    else:
        adjs = [
            ADJS[index][0 if is_fwd_direction else 1][0]
            for (index, is_fwd_direction) in adjpart
        ]
        lastadj = adjs.pop()
        return f"{a} is {','.join(adjs)} and {lastadj} than {b}"


def generate_question(index, is_fwd_direction):
    return 'Which is the {}?'.format(
        ADJS[index][0 if is_fwd_direction else 1][1]
    )
