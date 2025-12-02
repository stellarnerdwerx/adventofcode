with open('two.txt','r') as file:
    content = file.read()
    
def is_repeat_2(s):
    if len(s)%2==0:
        half = round(len(s)/2)
        if s[:half]==s[half:]:
            return True

invalid=[]
for rg_str in content.split(','):
    x,y = rg_str.split('-')
    rg_rg = range(int(x), int(y)+1) #ugh, include the end
    for i in rg_rg:
        if is_repeat_2(str(i)):
            invalid.append(i)
print(sum(invalid)) #part1

def is_repeat_n(s):
    for seq_len in range(1, round(len(s)/2)+1):
        if len(s)%seq_len==0: 
            seq = s[:seq_len]
            if s==seq*round(len(s)/seq_len):
                return True

invalid=[]
for rg_str in content.split(','):
    x,y = rg_str.split('-')
    rg_rg = range(int(x), int(y)+1) #ugh, include the end
    for i in rg_rg:
        if is_repeat_n(str(i)):
            invalid.append(i)
print(sum(invalid))#part2
