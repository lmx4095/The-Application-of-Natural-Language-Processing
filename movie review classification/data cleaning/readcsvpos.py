import csv
import codecs
with open('pos.csv') as f:
  reader = csv.reader(f)
  for num in range(1,1001):
    row1 = next(reader)
    s=str(num)+'.txt'
    f = codecs.open(s, 'w', 'UTF-8')
    f.write(''.join(row1))
    f.close()
