import pandas as pd

with open('day2.txt','r') as file:
    content = file.read()
    
df = pd.DataFrame(content.split('\n'), columns=['input'])

df['intList']=df['input'].apply(lambda x: [int(y) for y in x.split()])
df['diffList']=df['intList'].apply(lambda a: [x - a[i - 1] for i, x in enumerate(a)][1:])
df['sameSign']=df['diffList'].apply(lambda x: all(item > 0 for item in x) or all(item <0 for item in x))
df['oneThree']=df['diffList'].apply(lambda x: all(abs(item) >= 1 for item in x) and all(abs(item) <=3 for item in x))
df['and']=df.apply(lambda row: row['sameSign'] & row['oneThree'], axis=1)
#part1
print(df['and'].sum())