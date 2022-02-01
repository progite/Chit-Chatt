file1 = open('chat.txt','r',encoding = 'utf8')
file = file1.readlines()
text = []

for line in file:
    if line[0].isalpha():
        text[-1].extend(line)
        continue
    if line[31] ==':':
        text.append([line[33:]])
        continue
    line = line[20:]
    pos = line.index(':')
    if pos + 2 < len(line) and line[pos + 2] != '<':
        text.append([line[pos + 2:]])
file1.close()

file = open('trainer_file.txt','w',encoding = 'utf8')
for line in text:
    line = ' '.join(map(str,line))
    file.write(line + '\n')
file.close()