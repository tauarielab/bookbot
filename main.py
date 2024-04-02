
def word_count(str):
    words=str.split()
    return len(words)

def letter_count(str):
    letter_dict=[]
    lower_str=str.lower()
    for letter in "abcdefghijklmnoppqrstuvwxyz":
        letter_dict.append({"letter":letter,"num":0})
    for char in lower_str:
        if char in "abcdefghijklmnopqrstuvwxyz":
            for i in range(len(letter_dict)):
                if letter_dict[i]["letter"]==char:
                    letter_dict[i]["num"]=letter_dict[i]["num"]+1
    return letter_dict

def sort_on(dict):
    return dict["num"]

path_to_file="books/frankenstein.txt"
with open(path_to_file) as f:
    file_contents = f.read()
    word_num=word_count(file_contents)
    letter_dict=letter_count(file_contents)
    letter_dict.sort(reverse=True, key=sort_on)
    print("--- Begin report of", path_to_file ,"---")
    print(word_num,"words found in the document")
    for dict in letter_dict:
        print("The", dict["letter"] ,"character was found", dict["num"] ,"times")
    print("--- End report ---")
