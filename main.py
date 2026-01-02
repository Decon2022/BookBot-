from stats import word_count


'''
Function: Get book from user
Input: book directory
Output: return a list of str of the book

'''
def get_book_text(userDirectory):

    with open(userDirectory) as f:
        
        # read book content
        book_content = f.read()
       
        # typecast to string 
        str(book_content)

        return book_content

def main():
    
    book_dir = "./books/frankenstein.txt"

    word_count(get_book_text(book_dir))
    

main()

