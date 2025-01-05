def number_of_words(contents):
    contents=contents.split()
    words = len(contents)
    return words

def count_characters(contents):
    contents=contents.lower()
    letters_freq = {}
    for content in contents:
        if content in letters_freq:
            letters_freq[content]+=1
        else:
            letters_freq[content]=1
    return letters_freq



def main():
    with open("books/frankenstein.txt") as f:
        file_contents=f.read()
    file_contents=file_contents.lower()
    print(file_contents)
    print(f"\n{number_of_words(file_contents)} words found in the document")
    count_char=count_characters(file_contents)
   
    for char in count_char:
        if char.isalpha()==True:
            print(f"The {char} was found {count_char[char]} times")



main()