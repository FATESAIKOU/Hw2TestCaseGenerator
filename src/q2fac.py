import random


def genWords(word_num, min_len, max_len, alpha_bet):
    words = []

    for i in xrange(word_num):
        new_word_len = random.randint(min_len, max_len)
        new_word = ''.join([random.choice(alpha_bet) for _ in xrange(new_word_len)])

        words.append(new_word)

    return words

def createGenerator(cfg):
    q_size = cfg['question_size']
    q_min_word_num = cfg['min_word_num']
    q_max_word_num = cfg['max_word_num']
    q_min_word_len = cfg['min_word_len']
    q_max_word_len = cfg['max_word_len']
    q_alpha_bet = cfg['alpha_bet']

    yield q_size, None

    for _ in xrange(q_size):
        words = genWords(
            random.randint(q_min_word_num, q_max_word_num),
            q_min_word_len,
            q_max_word_num,
            q_alpha_bet
        )

        ip = ' '.join(words)
        op = ' '.join(reversed(words))

        yield ip, op
    
    yield None, None
    

