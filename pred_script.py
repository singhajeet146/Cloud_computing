#Flask
import json
from flask import Flask, request

import joblib
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')


flask_app = Flask(__name__)



classes = ['Negative','Positive']

#Load the model
model = joblib.load("./model/model_LR.pkl")
count_vect = joblib.load("./model/count_vect.pkl")

# Data Cleaning
def review_to_words( raw_review ):
    # Function to convert a raw review to a string of words
    # The input is a single string (a raw movie review), and
    # the output is a single string (a preprocessed movie review)
    #
    # 1. Remove HTML
    review_text = BeautifulSoup(raw_review,"lxml").get_text()
    #
    # 2. Remove non-letters
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))
    #
    # 5. Remove stop words and perform stemming
    manualStops = ['user','day']
    ps = PorterStemmer()
    meaningful_words = [ps.stem(w) for w in words if not w in set(stops)]
    meaningful_words = [w for w in meaningful_words if not w in set(manualStops)]
    #
    # 6. Join the words back into one string separated by space,
    # and return the result.
    return( " ".join( meaningful_words ))

#get prediction from loaded model

@flask_app.route('/',methods=['GET'])
def get_default():
    print('Welcome to the prediction page')
    return "API is working Fine"

@flask_app.route('/predict_sentiment/<string:input_text>',methods=['GET'])
def getPrediction(input_text):
    print(input_text)
    # input_text = request.form['text']
    text = review_to_words(input_text)

    input_features = count_vect.transform([text]).toarray()
    pred = model.predict_proba(input_features)[0]
    return dict(zip(classes,pred))



if __name__ == '__main__':
    flask_app.run(host ='0.0.0.0',port=5021, debug=False)
