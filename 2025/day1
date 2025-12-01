import pandas as pd

df = pd.read_csv('one.txt', header=None)
df['way'] = df[0].apply(lambda x: x[0])
df['count'] = df[0].apply(lambda x: int(x[1:]))

dial = 50
z = 0

for ix, row in df.iterrows():
    if row['way'] == 'R':
        dial += row['count']
    else:
        dial -= row['count']
    dial = dial % 100
    if dial == 0:
        z+=1
print(z) #part1

dial = 50
z = 0

for ix, row in df.iterrows():
    for i in range(row['count']):
        if row['way'] == 'R':
            dial = (dial+1)%100
        else:
            dial = (dial-1)%100
        if dial==0:
            z+=1
print(z) #part2
