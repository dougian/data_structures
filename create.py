import pickle
import csv

l = list()
limit = 10000
with open("books.csv") as csvf:
    spamreader = csv.reader(csvf, delimiter=';', quotechar='|')
    for n, row in enumerate(spamreader):
        if n == 0:
            continue
        if n == limit:
            break
        if n % 500 == 0:
            id = row[0].strip('"')
            title = row[1].strip('"')
            iter = 0
            while True:
                st = row[2 + iter].split()
                if len(st) > 1:  # if it's 1, then it's the year
                    map(lambda s: s.strip() + " ", st)
                    surname = st[-1]
                    iter += 1
                else:
                    break
            l.append((id,title,surname))

with open("sample.txt",'w') as f:
    pickle.dump(l,f)
