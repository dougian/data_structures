import json, os
import csv

class Books(object):

    """Books contains a list of all the books loaded"""

    def __init__(self):
        super(Books, self).__init__()
        self.arr = [ ]

    def load_books(self,file):
        ''''Loads the array with books given a filename.
           Returns True if successfull, False otherwise.'''

        if not os.path.exists(file):
            print("The filename that you entered does not exist! ")
            file  = input("Please provide the correct filename")

        if file.endswith(".json"):
            try:
                self.arr = json.load(file)
                return True
            except Exception as e:
                print ("Something went wrong while trying to load a json file")
                return False


        elif file.endswith(".csv"):
            try:
                with open(file) as csvfile:
                    spamreader = csv.reader(csvfile,delimiter=';',quotechar='|')
                    for n,row in enumerate(spamreader):

                        if n == 0:
                            continue
                        id = row[0].strip('"')
                        title = row[1].strip('"')
                        iter = 0
                        authors = []

                        while True:
                            st = row[ 2 + iter ].split()
                            if len(st) > 1: #if it's 1, then we've moved to the year
                                map(lambda s: s.strip() + " ", st)
                                name = "".join( st[:-2] )
                                surname = st[-1]
                                authors.append(Author(name,surname))
                                iter += 1
                            else:
                                break

                        summary = " ".join(row[ 2 + iter : ])

                        self.arr.append(Book(id, title, summary, authors))

            except UnicodeDecodeError as e:
                        pass
        else:
            print("Unsupported file format, please try a csv of json file")
            return False

    def save_books(file):
        '''Exports the array of books as a json file for later use.
            Returns True if successful, False if not'''
        try:
            with open(file,'w') as f:
                json.dump(self.arr, f)
                return True
        except OSError:
            print("The file cannot be opened for writing")
            return False

    def add_book(self):
        id = input("Please enter the id")
        title = input("Please enter the title of the book")
        descr = input("Now enter the description of the book")
        authors_string = input("Finally enter the authors of the books, separated by commas (e.g. John Douratsos, Grigoris Douratsos")
        auth_list  = authors_string.split(',')
        authors = [ ]

        for auth in auth_list:
            name_surname = auth.split()
            name = name_surname[0]
            surname = name_surname[1]
            authors.append( Author(name, surname ) )

        try:
            self.arr.append( Book(name, surname, descr, authors) )
            return True
        except:
            print("Couldn't add the book to the list")
            return False

    def  disp_books(self):
        """Print all books in the database."""
        for book in self.arr:
            print (book )

    def disp_id(self,id):
        """Print a book based on id."""
        for book in self.arr:
            if book.id == id:
                print(book)

    def disp_title(self,title):
        """Print a book that has the title given in title."""
        for book in self.arr:
            if book.title.startswith(title):
                print(book)

    def disp_surname(self,surname):
        """Print a book based on the surname of the author"""
        for book in self.arr:
            surnames = [a.surname for a in book.authors]
            if surname in surnames:
                print(book)



class Author(object):
        """Author has a name and a surname for each author"""
        def __init__(self, name, surname):
            super(Author, self).__init__()
            self.firstname = name
            self.lastname = surname

        def __str__(self):
            return self.firstname + " " + self.lastname


class Book(object):
                    """Book has an id, a title, a description and some Authors"""
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
__defaultfile__   = ""

