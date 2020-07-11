from flask import Flask,render_template
from main import getAllCharacters

app=Flask(__name__)

@app.route('/home')
def allcharacters():
    char_details=getAllCharacters()
    return render_template('home.html',characters=char_details)
    #return(char_details[1])

@app.route('/character')
def characterdetails():
    pass

@app.route('/episodes')
def getAllEpisodes():
    pass


if __name__ == '__main__':
    app.run(debug=True, port=5000)