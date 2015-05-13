__author__ = 'clayton'


def stopwords(path = '../res/stop-words_brazil_1_br.txt'):
    f = open(path, 'r')
    list  = []

    line = 1
    word = f.readline()
    while(word != ''):
        list.append(str(word).replace('\n',''))
        word = f.readline()

    f.close()
    return list
