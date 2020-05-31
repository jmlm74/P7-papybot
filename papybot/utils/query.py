import json
import unicodedata
from papybot import app


class Query:
    """
    Query Class
    contains  the query to be parsed and its treatment
    """

    def __init__(self, query):
        """
        init the query

        argument :
            the query itself in human language.
            punctuation is authorized
        Return: None
        """

        self.query = query
        self.ficstopwords = str(app.root_path) + '/static/json/stopwords.txt'
        self.ficperso = str(app.root_path) + '/static/json/stopwordsperso.txt'

    def parse_query(self):
        """
        The parser

        argument : None
            the query is used as self.query (in the init)
        Return:
            the parsed query as a string (words are space sparated)
        """
        stop_words_minus = []
        ponctuation = ['.', ',', '?', '!', '-', "'", '"', '[', ']', '/', '{', '}', '<', '>', '&',
        '^', '#', '$']
        list_words_ok = []
        list_query = []
        list_query2 = []
        t = ""

        # 1st --> delete punctuation
        for char in ponctuation:
            if char in self.query:
                self.query = self.query.replace(char, ' ')

        # 2nd --> suppress weird chars
        list_query = self.query.split()
        for word in list_query:
            try:
                word = unicode(word, 'utf-8')
            except (TypeError, NameError):
                pass
            word = unicodedata.normalize('NFD', word)
            word = word.encode('ascii', 'ignore')
            word = word.decode("utf-8")
            list_query2.append(word.lower())

        # 3rd --> put the std stopwords file into list and lower the list
        with open(self.ficstopwords, 'r') as f:
            stop_words = json.load(f)
        for t in stop_words:
            stop_words_minus.append(t.lower())
        # 4th --> put my stopwords file into list and lower it appending the 1st one
        with open(self.ficperso, 'r') as f:
            stop_words = json.load(f)
        for t in stop_words:
            stop_words_minus.append(t.lower())
        # 5th suppress  items in the query which are in the stopwords
        for t in list_query2:
            if len(t) > 0 and t.lower() not in stop_words_minus:
                list_words_ok.append(t.lower())

        self.query = ' '.join(list_words_ok)
        return(self.query)
