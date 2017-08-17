#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string
try:
    maketrans = ''.maketrans
except AttributeError:
    # fallback for Python 2
    from string import maketrans

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        # text = text.translate(str.maketrans('','',string.punctuation))
        text_string = content[1].translate(maketrans("", "", string.punctuation))

        ### project part 2: comment out the line below
        # words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        # stemmer = SnowballStemmer("english", ignore_stopwords=True)
        stemmer = SnowballStemmer("english")
        tokens = text_string.split();
        for word in tokens:
            stemmed = stemmer.stem(word)
            words = words+ " " +stemmed;
    return words

    

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print(text)



if __name__ == '__main__':
    main()

