import sys, bookservice

def menu():
	print("Please choose from 1-9")
	print("1. Load books from file")
	print("2. Save books to file")
	print("3. Add a book")
	print("4. Delete a book by id")
	print("5. Display a book by id")
	print("6. Display a book by title")
	print("7. Display books")
	print("8. Display books by surname search")
	print("9. Exit")
	c = raw_input()
	return int(c)

def main():
	if len(sys.argv) > 1:
		name = sys.argv[1]
	else:
		name = "books.csv"
	choice = 0
	b = bookservice.Books()
	print("ENA")
	while choice != 9:
		choice = menu()
		if choice == 1:
			size = 3000
			s = "n"
			if len(b.arr) > 1:
				del b.arr[0:len(b.arr)]
			#s = raw_input("Default size is 3000, do you want to change it? y/n")
			if s == "y":
				size = int(raw_input("Please enter a size for the database"))
			b.load_books("books.csv",size)
		elif choice  == 2:
			if not b.save_books(name):
				print("Oups, something went wrong!")
		elif choice == 3:
			b.add_book()
		elif choice == 4:
			iid = raw_input("Please enter the ID that you want to delete")
			b.delete_book(iid)
		elif choice == 5:
			iid = str(raw_input("Please enter the ID that you want to display"))
			mybook = b.disp_id(iid)
			print(mybook)
		elif choice == 6:
			title = raw_input("Please enter the title that you want to display")
			mybook = b.disp_title(title)
			print(mybook)
		elif choice == 7:
			b.disp_books()
		elif choice == 8:
			title = raw_input("Please enter the surname of the author that you want to display")
			mybook_list = b.disp_surname(title)
			for b1 in mybook_list:
				print(b1)



main()
__author = "John Douratsos"
