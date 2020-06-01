from shutil import make_archive as archive

def main():
    # zip this directory
    fn = 'Harvard-CS-Readability'
    archive(fn, 'zip', fn) # '../' + 

if __name__ == '__main__':
    main()
