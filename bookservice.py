import json
from bisect import bisect_left
import os
import csv


class Books(object):
    """Books contains a list of all the books loaded.
       It also contains functions to add, delete, search books via multiple ways."""

    def __init__(self):
        super(Books, self).__init__()
        self.arr = []
        self.arrsorted = []

    def load_books(self, file, limit):
        '''Loads the array with books given a filename.
           Returns True if successfull, False otherwise.'''

        if not os.path.exists(file):
            print("The filename that you entered does not exist! ")
            file = input("Please provide the correct filename")

        if file.endswith(".json"):
            try:
                self.arr = json.load(file)
                return True
            except Exception as e:
                print ("Something went wrong while trying to load a json file")
                return False

        elif file.endswith(".csv"):
            with open(file) as csvf:
                spamreader = csv.reader(csvf, delimiter=';', quotechar='|')
                for n, row in enumerate(spamreader):

                    if n == 0:
                        continue
                    if n == limit:
                        break
                    id = row[0].strip('"')
                    title = row[1].strip('"')
                    iter = 0
                    authors = []

                    while True:
                        st = row[2 + iter].split()
                        if len(st) > 1:  # if it's 1, then it's the year
                            map(lambda s: s.strip() + " ", st)
                            name = "".join(st[:-2])
                            surname = st[-1]
                            authors.append(Author(name, surname))
                            iter += 1
                        else:
                            break

                    summary = " ".join(row[2 + iter:])

                    self.arr.append(Book(id, title, summary, authors))
                self.arrsorted = sorted(self.arr, key = lambda x: x.id, reverse = False)

        else:
            print("Unsupported file format, please try a csv of json file")
            return False

    def save_books(file):
        '''Exports the array of books as a json file for later use.
            Returns True if successful, False if not.'''
        try:
            with open(file, 'w') as f:
                json.dump(self.arr, f)
                return True
        except OSError:
            print("The file cannot be opened for writing")
            return False

    def add_book(self):
        '''An interractive way to add a new book to the list.'''

        id = input("Please enter the id")
        title = input("Please enter the title of the book")
        descr = input("Now enter the description of the book")
        authors_string = input("Finally enter the authors of the books," /
                               + "separated by commas (e.g." /
                               +"John Douratsos, Grigoris Douratsos")
        auth_list = authors_string.split(',')
        authors = []

        for auth in auth_list:
            name_surname = auth.split()
            name = name_surname[0]
            surname = name_surname[1]
            authors.append(Author(name, surname))

        try:
            self.arr.append(Book(name, surname, descr, authors))
            self.arrsorted = sorted(self.arr, key = lambda x: x.id, reverse = False)
            return True
        except:
            print("Couldn't add the book to the list")

            return False

    def delete_book(self, id):
        """Delete a book based on id.Linear time."""
        for book in self.arr:
            if book.id == id:
                self.arr.remove(id)

    def disp_books(self):
        """Print all books in the database."""
        for book in self.arr:
            print (book)

    def disp_id(self, id):
        """Print a book based on id. Linear time."""
        for book in self.arr:
            if book.id == id:
                return book
        return None

    def disp_title(self, title):
        """Print a book that has the title given in title. Linear time."""
        for book in self.arr:
            if book.title.startswith(title):
                return book
        return None

    def disp_surname(self, surname):
        """Returns a list of books based on the surname of the author.
         Will return ALL the books created by the author, whether alone
         or collaborative. Time is again linear."""

        l = []
        for book in self.arr:
            surnames = [a.lastname for a in book.authors]
            if surname in surnames:
                l.append(book)
        if len(l) > 0 :
            return l
        else:
            return None

    def binary_search(self, x, a = None, lo=0, hi=None):
        """Search for a book based on id.
        Implements binary search, which should have an average complexity of log(n)."""

        if hi is None:
            a = self.arrsorted
            hi = len(a)
        while lo < hi:
            mid = (lo+hi)//2
            midval = a[mid]
            if midval.id < x:
                lo = mid+1
            elif midval.id > x:
                hi = mid
            else:
                return a[mid]
        return None


class Author(object):
        """Author has a name and a surname for each author"""

        def __init__(self, name, surname):
            super(Author, self).__init__()
            self.firstname = name
            self.lastname = surname

        def __str__(self):
            return "Name:" + self.firstname + " Surname " + self.lastname


class Book(object):
                    """Book has an id, title, description and some Authors.
                    Each book can also print itself.Books can be compaired with each other
		    based on the id that they have."""
                    authors = []
                    def __init__(self, id, title, summary, authors):
                        super(Book, self).__init__()
                        self.id = id
                        self.title = title
                        self.summary = summary
                        self.authors = authors

                    def __str__(self):
                        auth = [ str(x) + " " for x in self.authors ]
                        temp  = " Id : {}".format( self.id ) +  " " + "Title : " + self.title + " " + "Authors : "
                        temp += ''.join(auth)
                        return temp

                    def __lt__(self, other):
                        if type(other) == Book:
                            return self.id < other.id
                        elif type(other) == str:
                            return self.id < other
                        else:
                            raise Exception("don't know how to compare")

                    def __gt__(self, other):
                        if type(other) == Book:
                            return self.id > other.id
                        elif type(other) == str:
                            return self.id > other
                        else:
                            raise Exception("don't know how to compare")




__defaultfile__   = ""
