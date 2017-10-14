import random


def createGenerator(cfg):
    q_size = cfg['question_size']
    q_from = 10 ** int(cfg['min_num_size'])
    q_to = 10 ** int(cfg['max_num_size'])

    yield q_size, None
    
    now = 0
    new = 0
    for _ in xrange(q_size):
        new = random.randint(q_from, q_to)
        now = now + new

        yield new, None
        
    yield None, now

    yield None, None
