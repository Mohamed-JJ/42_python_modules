import sys

def text_analyser(string=None):
    """
    This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.
    """
    upper_case = 0
    lower_case = 0
    punctuation = 0
    spaces = 0
    if string == None:
        string = input("What is the text to analyse?\n")
    if (type(string) != str):
        print("The text must be a string")
    for i in string:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
        elif i in ".,;:!?":
            punctuation += 1
        elif i.isspace():
            spaces += 1
    print("The text contains", len(string))
    print("The amount of upper characters is", upper_case)
    print("The amount of lower characters is", lower_case)
    print("The amount of punctuation characters is", punctuation)
    print("The amount of spaces is", spaces)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("more arguments are needed in order to run this program")
        exit(1)
    else:
        number = text_analyser(sys.argv[1])