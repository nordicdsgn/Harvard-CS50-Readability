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
    print('USAGE: {python{3}} readability.py [-p STATE]')
    print('       Aliases: (-p, --precise, --precision)')
    print('       States: (0, false, False); (1, true, True)')
    print()

    sys.exit(0)


# main
def main():
    text = input('Text: ')

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
    precision = False
    # acceptable paramters
    params = ['-p', '--precision', '--precise']
    # acceptable paramater responses
    resps = ['true', 'True', '1']

    # check args for precise calculations
    if len(sys.argv) == 3:
        if sys.argv[1] in params and sys.argv[2] in resps:
            precision = True
        else:
            usage()
    elif len(sys.argv) > 1:
        usage()


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
