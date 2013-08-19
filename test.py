import time
import os
import bookservice
b = bookservice.Books()
b.load_books("books.csv")
start1 = time.time()
b.disp_id("074322678X")
end1 = time.time()
print("arr:")

for book in b.arr[0:10]:
    print(book.id)

print("sorted arr:")

for book in b.arrsorted[0:10]:
    print(book.id)

start2 = time.time()
b.binary_search("074322678X")
end2 = time.time()


print("Linear search:", end1-start1)
print("Binary search : ", end2-start2)
