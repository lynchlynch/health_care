def trans_ans(ans_list):
    trans_ans_list = []
    for single_answer in ans_list:
        new_single_ans = single_answer.split(' ')[0]
        new_single_ans = int(new_single_ans)
        trans_ans_list.append(new_single_ans)
    return trans_ans_list

def wearing_score(single_wearing):
    single_wearing_raw = single_wearing.split(' ')[0]
    if single_wearing_raw == '1' or single_wearing_raw == '2':
        single_wearing_score = 0
    elif single_wearing_raw == '3':
        single_wearing_score = 3
    else:
        single_wearing_score = 5

    return single_wearing_score

def hygiene_score(single_hygiene):
    single_hygiene_raw = single_hygiene.split(' ')[0]
    if single_hygiene_raw == '1':
        single_hygiene_score = 0
    elif single_hygiene_raw == '2':
        single_hygiene_score = 1
    elif single_hygiene_raw == '3':
        single_hygiene_score = 3
    else:
        single_hygiene_score = 7

    return single_hygiene_score


def toex_score(single_toilet,single_excrete):
    single_toilet_raw = single_toilet.split(' ')[0]
    single_excrete_raw = single_excrete.split(' ')[0]
    if max(single_toilet_raw,single_excrete_raw) == '1':
        single_toex_score = 0
    elif max(single_toilet_raw,single_excrete_raw) == '2':
        single_toex_score = 1
    elif max(single_toilet_raw,single_excrete_raw) == '3':
        single_toex_score = 5
    else:
        single_toex_score = 10

    return single_toex_score

def moving_score(single_moving):
    single_moving_raw = single_moving.split(' ')[0]
    if single_moving_raw == '1':
        single_moving_score = 0
    elif single_moving_raw == '2':
        single_moving_score = 1
    elif single_moving_raw == '3':
        single_moving_score = 5
    else:
        single_moving_score = 10

    return single_moving_score