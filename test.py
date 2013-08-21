import time
import os
import bookservice
import trie
import AVL

b = bookservice.Books()
b.load_books("books.csv",5000)
print("PSAXNW TO 0425176428")
t = trie.Trie()
avl = AVL.AVLTree()
print("creating trie + AVL....")
t.build_tree(b.arr)
avl._buildMe(b.arr)
#    print(book)
print("trie is ready, LET'S TEST!")
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


print("id Linear search:", end1-start1)
print("id Binary search : ", end2-start2)

print("id avl search : ", end5-start5)
print("string trie search : ", end3-start3)

print("string linear search: " ,end4-start4)

