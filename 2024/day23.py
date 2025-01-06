import pandas as pd
import networkx as nx
from itertools import combinations

filename = 'day23.txt'
df=pd.read_csv(filename, names=['conn'])
df['connL'] = df['conn'].apply(lambda x: x.split('-')[0])
df['connR'] = df['conn'].apply(lambda x: x.split('-')[1])

G = nx.Graph()
for ix,row in df.iterrows():
    G.add_edge(row['connL'], row['connR'])

#part1 
is_good=0
for a,b,c in combinations(G.nodes,3):
    if (G.has_edge(a, b)) and (G.has_edge(b, c)) and (G.has_edge(a, c)):
        if any(x.startswith('t') for x in [a,b,c]):
            is_good+=1
print(is_good)

#part2
cq=sorted(list(nx.find_cliques(G)), key=len, reverse=True)
print(','.join(sorted(cq[0])))