from collections import deque

cur_lst= deque(["Marc", "Sylvie", "Julien", "Christine", "Axel"])
cur_lst2 = cur_lst.copy()
Pre_len = len(cur_lst)
rtn_lst = []
group_size = 3

if group_size > 1:
    Cnt = 1
    while Cnt < group_size:
        rtn_lst = []
        for i in cur_lst2:
            cnt = 0
            cur_lst.reverse()
            for k, x in enumerate(cur_lst):
                if i in x: break
            k = len(cur_lst) - k
            cur_lst.reverse()
            while k + cnt < len(cur_lst):
                rtn_lst.append(f"{i}-{cur_lst[cnt + k]}")
                cnt += 1
        cur_lst = deque([])
        for i in rtn_lst: cur_lst.append(i)
        Cnt += 1
    print(rtn_lst)
else:
    print(cur_lst)
