# ASSETS
# system access
import sys

# liau index formula
def liau(letters, words, sentences):
    # letters / words = letters (per 100 words) / 100
    # therefore: (letters / words) * 100 = letters (per 100 words)
    # same applys for sentences / words

    # letters per 100 words
    L = (letters / words) * 100
    # sentences per 100 words
    S = (sentences / words) * 100

    index = 0.0588 * L - 0.296 * S - 15.8
    return index

# manual
def usage():
    print()
    print('USAGE: {python{3}} readability.py [-u] [-p STATE]')
    print('       ALIASES: (-p, --usage)')
    print('              : (-p, --precise, --precision)')
    print('       STATES: (0, false, False); (1, true, True)')
    print()

    sys.exit(0)


# main
def main():
    # precise calculations
    precision = False

    # acceptable paramsters (precision)
    pparams = ['-p', '--precision', '--precise']
    # acceptable paramaterd (usage)
    uparams = ['-u', '--usage']

    # acceptable paramater responses
    resps = ['true', 'True', '1']

    # amount of arguements
    length = len(sys.argv)

    # arguement handling
    try:
        # check args for precise calculations
        if sys.argv[1] in pparams and sys.argv[2] in resps:
            precision = True
        # usage or INVALID
        elif sys.argv[1] in uparams or length > 1:
            usage()
    except IndexError: # sys.argv at insufficient length
        usage()


    # get input
    text = input('Text: ')

    # text
    letters = 0
    words = 1
    sentences = 0

    for i in text:
        if i == ' ':
            words += 1
        elif i == '.' or i == '!'or i == '?':
            sentences += 1
        elif i.isalpha():
            letters += 1

    index = liau(letters, words, sentences)


    # precise calculations
    if precision:
        print("Exact Index: " + str(index))
        print("Approximate Index: " + str(round(index)))
        print() # empty line

    elif index >= 16:
        print('Grade 16+')
    elif index < 0:
        print('Before Grade 1')
    else:
        print('Grade ' + str(round(index)))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print() # empty line
