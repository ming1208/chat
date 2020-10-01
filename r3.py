lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5] #切割取出時間
    name = s[0][5:] #切割取出人名
    print(time) 
    print(name)