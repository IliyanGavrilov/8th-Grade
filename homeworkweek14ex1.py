a = str(input("Word 1 = "))
b = str(input("Word 2 = "))
c = str(input("Word 3 = "))
d = str(input("Word 4 = "))
e = str(input("Word 5 = "))
f = str(input("Word 6 = "))

words = [a, b, c, d, e, f]
words_mentioned = []

def count_words(words):
    for i in words:
        words_count = {i:words.count(i)}
        if i not in words_mentioned:
            print(wordscount)
            words_mentioned.append(i)

count_words(words)
