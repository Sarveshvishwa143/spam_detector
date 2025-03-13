from django.shortcuts import render
import pickle
import nltk
import string
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
ps = PorterStemmer()


def index(request):
    return render(request, "index.html")

def secondpage(request):
    return render(request, "second.html")

def loginpage(request):
    return render(request, "login.html")

def phishing(request):
    return render(request, "phishing.html")

def spoofing(request):
    return render(request, "spoofing.html")

def dos(request):
    return render(request, "dos.html")
def about(request):
    return render(request, "about.html")

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

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

def classify(request):
    if request.method == 'POST':
        input_sms = request.POST['message']
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms])
        result = model.predict(vector_input)[0]

        if result == 1:
            classification = "Spam"
        else:
            classification = "Not Spam"

        return render(request, 'result.html', {'classification': classification})

    return render(request, 'second.html')
