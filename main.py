import sys, menu, bookservice
import json

def main():
    if len(sys.argv) != 2 :
        print("No filename provided , defaulting to {}".format(bookservice.__defaultfile__))
        filename  = bookservice.__defaultfile__
    else:
        filename  = sys.argv[1]
    with open(filename) as file:
        data = json.load(file)



if '__name__' == '__main__' :
    main()

__author = "John Douratsos"
