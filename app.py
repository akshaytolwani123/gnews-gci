from flask import Flask, render_template,abort
from newsapi imprt NewsApiClient

app = Flask(__name__)

@app.route('/')
def news():
    news = newsapi(q='Open-Source OR Android OR Linux',)
    return render_template('home.html',news = news)
    
