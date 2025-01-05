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


def get_num(count):
    return count["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents=f.read()
    file_contents=file_contents.lower()
    print(file_contents)
    print(f"\n{number_of_words(file_contents)} words found in the document")
    count_char=count_characters(file_contents)
    sorted_list=[]
    for char in count_char:
        if char.isalpha()==True:
            sorted_list.append({"char":char,"num":count_char[char]})
    sorted_list.sort(reverse=True,key=get_num)
    for item in sorted_list:
        print(f"The {item["char"]} character was found {item["num"]}")
            



main()