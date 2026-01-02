''' 
Function: Give total word count of book
Input: Book text
Output: Total word count 
'''
def word_count(texts):

    split = texts.split()  

    print(f"Found {len(split)} total words")
