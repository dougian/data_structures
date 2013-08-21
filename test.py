import sys
import time
import os
import bookservice
import trie
import AVL
if len(sys.argv) < 2:
    lines = 1500
else:
    lines = sys.argv[1]

b = bookservice.Books()
b.load_books("books.csv",int(sys.argv[1]))
print("PSAXNW TO 0425176428")
t = trie.Trie()
t2 = trie.Trie()
avl = AVL.AVLTree()
avl = AVL.AVLTree()
print("creating trie + AVL....")
t.build_tree(b.arr)
avl._buildMe(b.arr)
t2.build_authors(b.arr)
print("I'm ready, LET'S TEST!")
start1 = time.time()
print("id linear",str(b.disp_id("0425176428")))
end1 = time.time()


start2 = time.time()
print("id binary" + str(b.binary_search("0425176428")))
end2 = time.time()

start3 = time.time()
print("string via trie:", str(t.lookup("What If?: The World\'s Foremost Military Historians Imagine What Might Have Been")))
end3 = time.time()

start4 = time.time()
print("string linear:" ,str(b.disp_title("What If?: The World\'s Foremost Military Historians Imagine What Might Have Been")))
end4 = time.time()

start5 = time.time()
print("id avl:" ,str(avl.find("0425176428")))
end5 = time.time()

start6 = time.time()
temp = [str(i) for i in b.disp_surname('Cowley"')]
print("surname linear:", " ".join(temp))
end6 = time.time()


start7 = time.time()
temp2 = [str(i) for i in t2.lookup('Cowley"')]
print("surname via trie:", " ".join(temp2))
end7 = time.time()


print("===============Times===============")
print("id Linear search:", end1-start1)
print("id Binary search : ", end2-start2)
print("id avl search : ", end5-start5)
print("----------------------------------")
print("string trie search : ", end3-start3)
print("string linear search: " ,end4-start4)
print("----------------------------------")
print("surname linear: ", end6-start6)
print("surname trie: ", end7-start7)

