import time
import os
import bookservice
import trie
b = bookservice.Books()
b.load_books("books.csv")
start1 = time.time()
print("PSAXNW TO 0425176428")
print("l",str(b.disp_id("0425176428")))
end1 = time.time()
t = trie.Trie()
print("creating trie....")

for book in b.arr:
    t.add(book.title,book)
    print(book)
print("trie is ready, LET'S TEST!")


start2 = time.time()
print("b" + str(b.binary_search("0425176428")))
end2 = time.time()

start3 = time.time()
print("t:", str(t.lookup("What If?: The World\'s Foremost Military Historians Imagine What Might Have Been")))
end3 = time.time()

start4 = time.time()
print("l2:" ,str(b.disp_title("What If?: The World\'s Foremost Military Historians Imagine What Might Have Been")))
end4 = time.time()

print("Linear search:", end1-start1)
print("Binary search : ", end2-start2)

print("trie search : ", end3-start3)

print("linear2  search : ", end4-start4)
