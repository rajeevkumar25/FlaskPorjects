from flask import Flask,render_template,request
#from requests.api import request
from main import getAllCharacters,getCharacterDetails

app=Flask(__name__)

@app.route('/home')
def allcharacters():
    all_char_details=getAllCharacters()
    charcount=len(all_char_details)
    print(charcount)    
    return render_template('home.html',characters=all_char_details,charcount=charcount)
    #return(char_details[1])

@app.route('/character', methods=['GET', 'POST'])
def characterdetails():
    if request.method == 'POST':
        charid= request.form['btndetails']
        char_details=getCharacterDetails(charid)
        #print(charid)
        #print(char_details)
        
        return render_template('character.html',character=char_details)   
    else:
        return "hello"
    #

@app.route('/episodes')
def getAllEpisodes():
    pass


if __name__ == '__main__':
    app.run(debug=True, port=5000)