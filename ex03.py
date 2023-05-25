def text_analyser(string):
    upper_case = 0
    lower_case = 0
    punctuation = 0
    spaces = 0
    for i in string:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
        elif i in ".,;:!?":
            punctuation += 1
        elif i.isspace():
            spaces += 1
    return upper_case, lower_case, punctuation, spaces
