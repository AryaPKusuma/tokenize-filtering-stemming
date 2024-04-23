import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class TextPreprocessor:
    def __init__(self):
        nltk.download('punkt') # download dataset punkt tokenizer
        nltk.download('stopwords') # download dataset stopword
        self.stop_words = set(stopwords.words('indonesian')) # menggunakan dataset stopword bahasa indonesia dari nltk
        self.stemmer = PorterStemmer()

    def tokenize(self, text):
        tokens = word_tokenize(text)
        return tokens

    def filter_tokens(self, tokens):
        filtered_tokens = []
        for token in tokens:
            if token.lower() not in self.stop_words and token.isalpha():
                filtered_tokens.append(token.lower())
        return filtered_tokens

    def stem_tokens(self, tokens):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        # stemmed_tokens = [stemmer.stem(token) for token in tokens]
        return stemmed_tokens