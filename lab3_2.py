import sys
import sys
from collections import Counter

sen = "the cat sat on the mat with a cat"
refList = ["The gunman was shot dead by the police .",  "The gunman was shot to death by the police . "]



def word_counter(input_string):
    input_list = input_string.lower().split()
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
    # fileN = sys.argv[1]
    # file1 = open(fileN, "r")

    # lines = file1.readlines()
    # for line in lines:
    #     word_counter(line)

    word_frequencies = word_counter(sen)
    product = 1

    for x in word_frequencies:
        product *= x

    print("Unigram Probability: ", product)

if __name__ == "__main__":
    main()
