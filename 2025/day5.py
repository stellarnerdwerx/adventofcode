import pandas as pd

df = pd.read_csv('five.txt', names=['rng'])

df['lst'] = df['rng'].apply(lambda x: x.split('-') if x else [])
df['type'] = df['lst'].apply(lambda x: 'fresh' if len(x)>1 else 'avail')

fresh_df = df[df['type'] == 'fresh'].copy()
fresh_df['start'] = fresh_df['lst'].apply(lambda x: int(x[0]))
fresh_df['end'] = fresh_df['lst'].apply(lambda x: int(x[1]))

avail_df = df[df['type'] == 'avail'].copy()
avail_df['id'] = avail_df['lst'].apply(lambda x: int(x[0]))

def check_fresh(id_val):
    return ((fresh_df['start']<=id_val) & (id_val<=fresh_df['end'])).any()

avail_df['is_fresh'] = avail_df['id'].apply(check_fresh)

print(sum(avail_df['is_fresh'])) #part1

fresh_df = fresh_df.sort_values('start').reset_index(drop=True)
merged = []
for ix, row in fresh_df.iterrows():
    if merged and row['start']<=merged[-1]['end']+1:
        #overlap
        merged[-1]['end']=max(merged[-1]['end'], row['end'])
    else:
        #no overlap
        merged.append({'start': row['start'], 'end': row['end']})

merged_df = pd.DataFrame(merged)
merged_df['count'] = merged_df['end']-merged_df['start']+1
print(sum(merged_df['count'])) #part2
