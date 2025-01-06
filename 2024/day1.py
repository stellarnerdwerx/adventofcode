import pandas as pd
df = pd.read_csv('day1.txt', header=None)
df=pd.DataFrame(df[0].apply(lambda x:x.split()).tolist()).astype(int)

#part1
print(sum(abs(df[0].sort_values().reset_index(drop=True)-df[1].sort_values().reset_index(drop=True))))

#part2
keep=[]
for i, num in enumerate(df[0].tolist()):
    keep+=[num*df[1].tolist().count(num)]
print(sum(keep))