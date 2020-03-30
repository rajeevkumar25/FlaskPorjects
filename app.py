
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
#import urllib

import sys
sys.path.append('C:\Rajeev\Python\Projects\APIProjects')
sys.path.append('C:\Rajeev\Python\Projects\APIProjects\GoodReadsAPI')
sys.path.append('C:\Rajeev\Python\Projects\WebScraping')
sys.path.append('C:\Rajeev\Python\Projects\WebScraping\WordVocab')
sys.path.append('C:\Rajeev\Python\Projects\WebScraping\MoneyControl')

#from APIProjects.getNewsHeadlines.py import getTopNews

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')
    # return 'Alright !'


@app.route('/imdbrating', methods=['GET', 'POST'])
def imdbrating():
    if request.method == 'POST':
        mvname = request.form['txtmoviename']
        if mvname != '':
            from getMovieIMDBRating import getMovieOtherDetails
            moviedetails = getMovieOtherDetails(mvname)
            if len(moviedetails) > 0:
                return render_template('imdbrating.htm', results=moviedetails)
            #    moviedetails.append(mvname)
            else:
                return render_template('imdbrating.htm')
            # for item in moviedetails:
            #    print(item)
            # return mvname
    else:
        #print('in else')
        return render_template('imdbrating.htm')


@app.route('/news', methods=['GET', 'POST'])
def news():
    if request.method == 'POST':
        newssrc = request.form['txtnewssource']
        if newssrc != "":
            # getnewsheadlines(newssrc)
            # print(sys.path)
            from getNewsHeadlinesAPI import getTopNews
            headlines = getTopNews(newssrc.format())
            # print(headlines)
            articles = headlines['articles']
            return render_template('news.htm', results=articles)
        # return newssrc
    else:
        return render_template('news.htm')


@app.route('/books', methods=['GET', 'POST'])
def booklist():
    # return(request.method)
    if request.method == 'POST':
        authname = request.form['txtauthname']
        #print('printing '+authname)
        # if authname != "":
        from goodreadsAPI import goodreadsAPI
        goodreadsAPI_obj = goodreadsAPI()
        book_list = goodreadsAPI_obj.getauthorbooks(authname)
        # print(book_list)
        return render_template('books.htm', results=book_list)
        # return authname
    else:
        # return('I am in else')
        return render_template('books.htm')


@app.route('/words', methods=['GET', 'POST'])
def wordsearch():
    if request.method == 'POST':
        word = request.form['txtwordname']

        if word != '':
            from getSynonymAntonym import getSynonym
            wordsyno = getSynonym(word)
            return render_template('wordvocab.htm', results=wordsyno)
        else:
            return render_template('wordvocab.htm')
    else:
        return render_template('wordvocab.htm')


@app.route('/businessnews', methods=['GET', 'POST'])
def businessnews():
    if request.method == 'GET':
        from getBusinessNews import getnewsheadlines
        newsheadlines = getnewsheadlines()
        return render_template('businessnews.htm', results=newsheadlines)
    else:
        return render_template('businessnews.htm')

# =======Freelance Python projects============
@app.route('/pythonprojects', methods=['GET', 'POST'])
def pythonprojects():
    if request.method == 'GET':
        return render_template('pythonprojects.htm')
    else:
        textsearch = request.form['txttechsearch']
        from getUpWorkPythonProject import getPythonProjects
        obj = getPythonProjects()

        if textsearch == '':
            textsearch = 'python'
        if request.form['prjpython'] == 'upwork':
            jobdetails = obj.getUpworkProjects(textsearch)
            #finaldetails = obj.getUpworkProjects(textsearch)
        if request.form['prjpython'] == 'freelancer':
            jobdetails = obj.getFreelanceProjects(textsearch)

    return render_template('pythonprojects.htm', results=jobdetails)


# =====End====Freelance Python projects============
if __name__ == '__main__':
    app.run(debug=True)
