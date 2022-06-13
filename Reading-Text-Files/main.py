# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as f:
        cont = f.read()
    return cont


def count_words():
    text = read_file_content("story.txt")
    text = text.split(" ")
    glass = text.count('glass')
    a = text.count('a')
    
    return {"glass": glass , "a": a}


read_file_content("story.txt")
count_words()