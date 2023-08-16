def word_count(words_string):
    words = words_string.split()
    return len(words)

def letter_count(letters_string):
    letters = {}
    letters_string_lower = letters_string.lower()
    for i in letters_string_lower:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters

def book_report(w_count, l_count):  
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{w_count} words found in the document")
    

def main():   
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    w_count = word_count(file_contents)
    print(w_count)
    l_count = letter_count(file_contents)
    print(l_count)
    book_report(w_count, l_count)

main()