from collections import Counter
import sys

sen = "<s> a cat sat on the mat </s>"
fileN = open("corpus\lab-5-files\corpus2.txt", "r")

def bigram_scanner(input_string):
    grams = 2
    results = []
    input_list = input_string.split()
    # print(input_list)

    for i in range(len(input_list)-grams+1):
        results.append(input_list[i:i+grams])

    return results

def word_counter(input_list):
    input_list = [' '.join([str(c) for c in lst]) for lst in input_list]
    list_len = len(input_list)
    counts = Counter(input_list)
    print("-" * 10)
    print("New Sentence")
    word_frequencies = []

    for key, value in counts.items():
        word_frequency = value/list_len
        word_frequencies.append(word_frequency)

    for key, value in counts.items():
        print("The token " + key + " frequency is :", value/list_len)

    return word_frequencies

def main():
    sen_bigram_list = bigram_scanner(sen)
    file_bigram_list = bigram_scanner(fileN.read())

    word_counter(sen_bigram_list)
    word_counter(file_bigram_list)

if __name__ == "__main__":
    main()