import pandas as pd

df = pd.read_csv('three.txt', names=['bank'])
df['bank_lst'] = df['bank'].apply(lambda x: [int(y) for y in x])

def get_max_l2(lst):
    #get first max
    max_0 = max(lst) 
    max_0_ix = lst.index(max_0)
    
    #find next max
    if max_0_ix < len(lst)-1:
        max_1 = max(lst[max_0_ix+1:])
        return int(str(max_0)+str(max_1))
    else:
        #max is at the end, look for max before it
        lst2 = lst.copy()
        lst2.remove(max_0)
        max_1 = max(lst2)
        return int(str(max_1)+str(max_0))

df['max_l2'] = df['bank_lst'].apply(lambda x: get_max_l2(x))
print(sum(df['max_l2']))

def get_max_l12(lst):
    out = []
    ix = 0
    
    #find 12 maxes
    for i in range(12):
        #find max in sublist
        sublst = lst[ix:len(lst)-12+i+1]
        max_i = max(sublst)
        max_i_ix = lst.index(max_i,ix)
        out.append(max_i)
        
        #update to start after found max
        ix = max_i_ix+1
    
    return int(''.join([str(m) for m in out]))

df['max_l12'] = df['bank_lst'].apply(lambda x: get_max_l12(x))
print(sum(df['max_l12']))
