from flask import Flask,render_template
from main import NewsAggregator

app=Flask(__name__)

@app.route('/index')
def index():
    obj=NewsAggregator()
    
    toiNews=obj.getToiNews()
    htNews=obj.getHtNews()
    googleNews=obj.getGoogleNews()
    return render_template('index.html',tNews=toiNews,hNews=htNews)




if __name__=='__main__':
    app.run(debug=True)