import os
os.chdir("C:\Documents and Settings\Φανη\Επιφάνεια εργασίας")
import bookservice
b = bookservice.Books()
b.load_books("Books.csv")
b.disp_books()
