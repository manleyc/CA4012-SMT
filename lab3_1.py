import sys
import sys
from collections import Counter

sen = "The gunman was shot dead by the police ."
refList = ["The gunman was shot dead by the police .",  "The gunman was shot to death by the police . "]



def word_counter(input_string):
    input_list = input_string.lower().split()
    list_len = len(input_list)
    counts = Counter(input_list)
    print("-" * 10)
    print("New Sentence")

    for key, value in counts.items():
        print("The token " + key + " frequency is :", value/list_len)

def main():
    fileN = sys.argv[1]
    file1 = open(fileN, "r")

    lines = file1.readlines()
    for line in lines:
        word_counter(line)

if __name__ == "__main__":
    main()
