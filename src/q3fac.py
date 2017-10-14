import random


def genWord(min_len, max_len, alpha_bet):
    word_len = random.randint(min_len, max_len)
    word = ''.join([random.choice(alpha_bet) for _ in xrange(word_len)])
    return word


def randomInsert(min_insert, max_insert, sample, ele):
    sample_len = len(sample)
    insert_time = random.randint(min_insert, max_insert)

    insert_idx = sorted(
        [random.randint(0, sample_len) for _ in range(insert_time)],
        reverse=True
    )

    for i in insert_idx:
        sample = sample[:i] + ele + sample[i:]
    

    return sample
    
    


def createGenerator(cfg):
    q_size = cfg['question_size']
    q_min_sample_len = cfg["min_sample_len"]
    q_max_sample_len = cfg["max_sample_len"]
    q_min_insert = cfg["min_insert"]
    q_max_insert = cfg["max_insert"]
    q_min_ori_word_len = cfg["min_ori_word_len"]
    q_max_ori_word_len = cfg["max_ori_word_len"]
    q_min_new_word_len = cfg["min_new_word_len"]
    q_max_new_word_len = cfg["max_new_word_len"]
    q_alpha_bet = cfg['alpha_bet']

    yield q_size, None

    for _ in xrange(q_size):
        ori_word = genWord(q_min_ori_word_len, q_max_ori_word_len, q_alpha_bet)
        new_word = genWord(q_min_new_word_len, q_max_new_word_len, q_alpha_bet)
        sample = genWord(q_min_sample_len, q_max_sample_len, q_alpha_bet)
        sample = randomInsert(q_min_insert, q_max_insert, sample, ori_word)

        result = sample.replace(ori_word, new_word)

        yield sample + '\n' + ori_word + ' ' + new_word, result

    yield None, None
    
    
    
    

    
