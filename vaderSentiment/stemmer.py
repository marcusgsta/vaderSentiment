# stemming
from nltk.stem import snowball
#from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("swedish")


def readFile(filename):
    """
    Read text file
    Return a list of lines 
    """
    with open (filename) as f:
        lines = f.read().splitlines()
    return lines
    
def saveListToFile(itemList, filename):
    """
    ( Save list of lists to file
    Each list gets its own line
    Append to the end of the file with filename - ("a") )
    """
    f = open(filename, "a")
    for line in itemList:

        #line = word[0] + "\t" + ' '.join(word[1][0:]).strip() + "\n"
        #print(line)
        # line = word[0] + " " + word[1] + "\n"
        f.write(line + "\n")
    f.close()


lexicon = readFile("vader_lexicon_swedish.txt")
# print(stemmer.stem(text_token_list[1]))
# print(text_token_list[1])

# loop through lexicon. Split each item
stemmed_lexicon = []
for line in lexicon:
    token = line.split()[:-1]
    valence = line.split()[-1]
    # if a token contains more than one word, only send the first word (to simplify)
    # print(token[0])
    # print(valence)
    # stem
    stemmed_word = stemmer.stem(token[0])
    # put it together again
    t = stemmed_word + " " + valence
    
    stemmed_lexicon.append(t)

#save stemmed_lexicon
saveListToFile(stemmed_lexicon, "vader_lexicon_swedish_stemmed_2.txt")



    


