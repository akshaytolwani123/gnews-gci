from flask import Flask, render_template,abort
from newsapi import NewsApiClient

app = Flask(__name__)

newsapi = NewsApiClient(api_key='0cae0ef493f1426ba9b13ec730ce8019')
@app.route('/')
def news():
    news = newsapi.get_everything(q='Open-Source OR Android OR Linux',language = 'en',sort_by = 'publishedAt' )
    return render_template('home.html',news = news)

if __name__ == '__main__':
    app.run()
