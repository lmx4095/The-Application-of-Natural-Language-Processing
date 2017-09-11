from random import randint

def word_sum(word_list):
    sum = 0
    for word, value in word_list.items():
        sum += value
    return sum


def retrieve_random_word(word_list):

    rand_index = randint(1, word_sum(word_list))
    for word, value in word_list.items():
        rand_index -= value
        if rand_index <= 0:
            return word

def build_dictionary(string):

    string = string.replace("\n", " ")
    string = string.replace("\"", "")


    punctuation = ['.',',',';',':']
    for symbol in punctuation:
        string = string.replace(symbol, " "+symbol+" ")

    words = string.split(" ")
    words = [word for word in words if word != ""]

    dictionary = {}
    for i in range(1, len(words)):
        if words[i-1] not in dictionary:
            #Create a new dictionary for this word
            dictionary[words[i-1]] = {}
        if words[i] not in dictionary[words[i-1]]:
            dictionary[words[i-1]][words[i]] = 0
        dictionary[words[i-1]][words[i]] += 1

    return dictionary

string =open("1929-Hoover.txt").read()
wordDict = build_dictionary(string)

length = 50
output = ""
word = "I"
for i in range(0, length):
    output += word+" "
    word = retrieve_random_word(wordDict[word])

print(output)