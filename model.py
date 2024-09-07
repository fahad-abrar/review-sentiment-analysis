import re
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class Review_Prediction_model:
    '''
    # Initialize the PorterStemmer
    # Load the pre-fitted TfidfVectorizer
    # Load the pre-trained model

    '''
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.vectorizer = pickle.load(open('ml-model/vectorizer.sav', 'rb'))
        self.model = pickle.load(open('ml-model/model.sav', 'rb'))

    '''
    # define a fuction for
    # remove stopwords and apply stemming

    '''
    def stemming(self, content):
        if not isinstance(content, str):
            content = ''
        stem_content = re.sub('[^a-zA-Z]', ' ', content)
        stem_content = stem_content.lower()
        stem_content = stem_content.split()
        stem_content = [self.stemmer.stem(word) for word in stem_content if word not in stopwords.words('english')]
        stem_content = ' '.join(stem_content)
        return stem_content

    '''
    # Transform the content using the pre-fitted vectorizer
    # Return the single prediction
    '''
    def predict(self, content):
        content_stemmed = self.stemming(content)
        content_vectorized = self.vectorizer.transform([content_stemmed])
        result = self.model.predict(content_vectorized)
        return result[0]  

    '''
    # send the final result
    '''

    def print_result(self, content):
        result = self.predict(content)
        if result == 2:
            message = 'Positive review'
        elif result == 1:
            message = 'Neutral review'
        else:
            message = 'Negative review'

        return message

