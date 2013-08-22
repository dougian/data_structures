import sys
import time
import os
import bookservice
import trie
import AVL
import pickle

def checkResults(res1, res2, res3, res4, res5, res6):
    return res1 == res2 == res3 == res4 == res5 == res6

lines = 1500
test_items = []
start = [0,0,0,0,0,0,0,0]
end = [0,0,0,0,0,0,0]
avg = [0,0,0,0,0,0,0]
endresults = []
with open("sample.txt") as f:
    test_items = pickle.load(f)
for (iid, ttitle, ssurname) in test_items[:2]:
    b = bookservice.Books()
    b.load_books("books.csv",int(lines))
    print("PSAXNW TO {}",iid)
    t = trie.Trie()
    t2 = trie.Trie()
    avl = AVL.AVLTree()
    avl = AVL.AVLTree()
    print("creating trie + AVL....")
    t.build_tree(b.arr)
    avl._buildMe(b.arr)
    t2.build_authors(b.arr)
    print("I'm ready, LET'S TEST!")

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
    temp = [str(i) for i in b.disp_surname(ssurname)]
    res5 = " ".join(temp)
    end[5] = time.time()

    start[6] = time.time()
    temp2 = [str(i) for i in t2.lookup(ssurname)]
    res6 = " ".join(temp2)
    end[6] = time.time()
    avg = [a + e - s for a, e, s in zip(avg,end,start)]

    if checkResults :
        print("All results are EQUAL!!!!")
    else:
        print("Error!")
        exit()
        endresults.append(size,list(avg))  #create a copy of avg and store it


print("===============Times===============")
print("id Linear search:", avg[0])
print("id Binary search : ",avg[1] )
print("id avl search : ", avg[4])
print("----------------------------------")
print("string trie search : ",avg[2])
print("string linear search: " ,avg[3])
print("----------------------------------")
print("surname linear: ", avg[5])
print("surname trie: ", avg[6])

