def find_anagram (word, anagram):
    word = sorted(word)
    anagram = sorted(anagram)
    print("first stage done and dusted")
    if word == anagram:
        return True
    else:
        return False


