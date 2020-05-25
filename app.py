from flask import Flask , render_template, request, Blueprint, redirect, url_for, flash
from flask import *
import pandas as pd
import io
import csv
import os
from werkzeug.utils import secure_filename
from tqdm import tqdm
from textblob import TextBlob
import emoji
#from cleantext import clean


app = Flask(__name__)


global sentiment_textblob
sentiment_textblob=''
emoji_textblob=''

# Get the polarity score using below function
def get_textBlob_score(sent):
    # This polarity score is between -1 to 1
    polarity = TextBlob(sent).sentiment.polarity
    return polarity


@app.route('/')
def load():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def sentiment():
    if request.method == 'POST':
        data= request.form['sampletext']
        # print('data:',data)
        #for i in range(len(data)):
        # sent=data['CleanText'][i]
        # print(sent)
        polarity=get_textBlob_score(data)
        print('polarity:',polarity)
        if polarity > 0:
           sentiment_textblob = 'The sentiment for input text is positive'
           emoji_textblob=emoji.emojize(":beaming_face_with_smiling_eyes:")
           print(emoji_textblob)
        elif polarity < 0:
            sentiment_textblob = 'The sentiment for input text is negative'
            emoji_textblob=emoji.emojize(":pensive_face:")
        else:
            sentiment_textblob = 'The sentiment for input text is neutral'
            emoji_textblob=emoji.emojize(":neutral_face:")
    return render_template('index.html', result=sentiment_textblob, emoj=emoji_textblob)

if __name__ == "__main__":
     app.run(debug = True,host='0.0.0.0', port=5000 )
