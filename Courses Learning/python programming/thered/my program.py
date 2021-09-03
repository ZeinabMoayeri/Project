""" open file """
import csv

def copy_book_list():
    with open("BooksRead.csv") as infile:
        csv_reader = csv.reader(infile)
    
        with open("new_book_list.csv", "w") as new_file:
            new_csv = csv.writer(new_file, delimiter='\t')
        
            for line in csv_reader:
                new_csv.writerow(line)
#%%
def read_csv_file(): 
    with open("BooksRead.csv", "r") as new_file:
        new_csv = csv.reader(new_file, delimiter='\t')
        
    for line in new_csv:
        print(line)
        
#%%
def csv_book_list():
    """This is Function use for Normal people """
    """return to Dictionary"""
    
    with open("BooksRead.csv") as infile:
        csv_reader = csv.DictReader(infile)
        
        for line in csv_reader:
            print(line["WRITHER"])
csv_book_list()

#%%
import csv
with open("BooksRead.csv", "r") as infile:
    csv_reader = csv.DictReader(infile)
    
    with open("new_book_list.csv", "w") as new_file:
        fielname = ["WRITHER", "NAME BOOK", "CATEGOURY"]
        new_csv = csv.DictWriter(new_csv, fieldnames = fielname, delimiter = "\t")
     
        new_csv.writeheader()
        for line in csv_reader:
            new_csv.writerow(line)


