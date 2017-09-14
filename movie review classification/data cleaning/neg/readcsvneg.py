import csv
import codecs
with open('neg.csv') as f:
  reader = csv.reader(f)
  for num in range(1001,2001):
    row1 = next(reader)
    s=str(num)+'.txt'
    f = codecs.open(s, 'w', 'UTF-8')
    f.write(''.join(row1))
    f.close()
