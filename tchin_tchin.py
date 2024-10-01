cur_lst= ["Marc", "Sylvie", "Julien", "Christine", "Axel"]
rtn_lst = []

for i in range(0, len(cur_lst)):
    cur_pers = cur_lst[i]
    cnt = i + 1
    while len(cur_lst) - cnt > 0:
        rtn_lst.append(f"{cur_pers}-{cur_lst[cnt]}")
        cnt += 1

print(rtn_lst)
