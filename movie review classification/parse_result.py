f = open('few_result.txt','r')
sStr4 = 'negati : positi'
sStr5 = 'positi : negati'
for line in open('few_result.txt'):
    line = f.readline()
    if(line.find(sStr5)==-1):
        continue
    else:
        sStr2 = '('
        sStr3 = ')'
        line = line[line.find(sStr2) + 1:line.find(sStr3)]
        print(line)
f.close()