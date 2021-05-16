def trans_ans(ans_list):
    trans_ans_list = []
    for single_answer in ans_list:
        new_single_ans = single_answer.split(' ')[0]
        new_single_ans = int(new_single_ans)
        trans_ans_list.append(new_single_ans)
    return trans_ans_list