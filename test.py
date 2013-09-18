import copy
import matplotlib.pyplot as plt
import sys
import time
import os
import bookservice
import trie
import AVL
import pickle

def checkResults(res1, res2, res3, res4, res5, res6):
    return res1 == res2 == res3 == res4 and res5 == res6

test_items = []
start = [0,0,0,0,0,0,0,0]
end = [0,0,0,0,0,0,0]
avg = [0,0,0,0,0,0,0]
endresults = {}
debug = False

with open("sample.txt") as f:
    test_items = pickle.load(f)

for size in range(500,8500,500):
    print("Size is {}".format(size))
    b = bookservice.Books()
    b.load_books("books.csv",size)
    t = trie.Trie()
    t2 = trie.Trie()
    avl = AVL.AVLTree()
    avl = AVL.AVLTree()
    if debug: print("creating trie + AVL....")
    t.build_tree(b.arr)
    avl._buildMe(b.arr)
    t2.build_authors(b.arr)
    if debug: print("I'm ready, LET'S TEST!")

    for (iid, ttitle, ssurname) in test_items:
        if debug: print("PSAXNW TO {}".format(iid))
        start[0] = time.time()
        res1 = b.disp_id(iid)
        end[0] = time.time()

        start[1] = time.time()
        res2 = b.binary_search(iid)
        end[1] = time.time()
        start[2] = time.time()
        res3 = t.lookup(ttitle)
        end[2] = time.time()

        start[3] = time.time()
        res4 = b.disp_title(ttitle)
        end[3] = time.time()

        start[4] = time.time()
        res5 = avl.find(iid)
        end[4] = time.time()

        start[5] = time.time()
        ll1 = b.disp_surname(ssurname)
        if ll1 is not None:
            temp = [str(i) for i in ll1 if ll1]
            res5 = " ".join(temp)
            if debug: print(res5)
        else:
            res5 = None
        end[5] = time.time()

        start[6] = time.time()
        ll2 = t2.lookup(ssurname)
        if ll2 is not None:
            temp2 = [str(i) for i in ll2]
            res6 = " ".join(temp2)
            if debug: print(res6)
        else:
            res6 = None
        end[6] = time.time()
        avg = [a + e - s for a, e, s in zip(avg,end,start)]

        if not checkResults :
            print("Error!")
            exit()
        else:
            endresults[size] = copy.deepcopy(avg)  #create a copy of avg and store it

for item in endresults:
    if True:

        print("===============Times===============")
        print("id Linear search: {}".format(endresults[item][0]))
        print("id Binary search: {}".format(endresults[item][1]))
        print("id avl search: {}".format(endresults[item][4]))
        print("----------------------------------")
        print("string trie search: {}".format(endresults[item][2]))
        print("string linear search: {}" .format(endresults[item][3]))
        print("---------------------------------")
        print("surname linear: {}".format(endresults[item][5]))
        print("surname trie: {}".format(endresults[item][6]))

sizes = endresults.keys()
tmp = [0,0,0,0,0,0,0]
for it in range(7):
    tmp[it] = [endresults[i][it] for i in endresults.keys() ]

plt.figure(1)
#plt.plot(sizes, tmp[0], 'go', label="Linear id search", sizes, tmp[1], 'bo', label="Binary id search",sizes, tmp[4], 'ro', label="Avl search")
p1 = plt.plot(sizes, tmp[0], 'bo')
p2 = plt.plot(sizes, tmp[1], 'go')
p3 = plt.plot(sizes, tmp[4], 'ro')
p11 = plt.Circle(1, 1, fc="b")
p12 = plt.Circle(1, 1, fc="g")
p13 = plt.Circle(1, 1, fc="r")
plt.legend([p11, p12, p13], ["Linear id search", "Binary id search", "Avl id search"])
plt.ylabel("Time in seconds")
plt.xlabel("Database size")
plt.figure(2)
p4 = plt.plot(sizes, tmp[2], 'go')
p5 = plt.plot(sizes, tmp[3], 'bo')
p21 = plt.Circle(1, 1, fc="g")
p22 = plt.Circle(1, 1, fc="b")
plt.legend([p21, p22], ["Linear title search", "Trie title search"])
plt.ylabel("Time in seconds")
plt.xlabel("Database size")
plt.figure(3)
p6 = plt.plot(sizes, tmp[5], 'go')
p7 = plt.plot(sizes, tmp[6], 'bo')
p31 = plt.Circle(1, 1, fc="g")
p32 = plt.Circle(1, 1, fc="b")
plt.legend([p31, p32], ["Linear authors search", "Trie authors search"])
plt.ylabel("Time in seconds")
plt.xlabel("Database size")
plt.show()
