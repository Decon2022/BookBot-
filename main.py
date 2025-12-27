
def get_book_text(userDirectory):

    with open(userDirectory) as f:
        
        # read book content
        book_content = f.read()
        
        # typecast to string 
        str(book_content)

        return book_content



def main():
    
    book_dir = "./books/frankenstein.txt"

    print (get_book_text(book_dir))

    






main()

