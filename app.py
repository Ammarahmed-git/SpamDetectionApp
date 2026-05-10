import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer


ps=PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)


    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()


    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)


    text =y[:]
    y.clear()



    for i in text:
        y.append(ps.stem(i))


    return " ".join(y)


Tfid = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the Message")

if st.button('predict'):
    #1. Preprocess
    transform_text = transform_text(input_sms)

    #2.Vectorize 

    vectorized_input = Tfid.transform([transform_text])

    #3.Predict

    result = model.predict(vectorized_input)[0]

    #4.Display

    if result == 1:
        st.header("SPAM")

    else:
        st.header("Not SPAM")