from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY']= '12345'
debug= DebugToolbarExtension(app)
app.debug = True

stories = [
    {'id':1,
    'title':'Story 1:A day at the zoo',
     'paragraph': "Today, I went to the zoo with my (adjective) friend. We saw a (adjective2) (animal) that was (verb)in its enclosure. Then, we watched a (adjective3) (animal2) show, where the animals performed (plural_noun) tricks. "},
    {'id':2,
     'title':'Story 2: A day at the park',
     'paragraph':'Today, I went to the park with my (adjective) friend. We brought a (noun) and had a lot of fun (verb) in the (place). It was the best day ever!'}
]

@app.route('/')
def home():
    return render_template('form.html',stories=stories)  

@app.route('/stories/1')
def story_one():
    return render_template('/stories/1.html') 

@app.route('/stories/1', methods=['POST'])
def story_one_post():
    session['adjective']  = request.form['adjective']
    session['animal']  = request.form['animal']
    session['verb']  = request.form['verb']
    session['adjective2']  = request.form['adjective2']
    session['adjective3']  = request.form['adjective3']
    session['animal2']  = request.form['animal2']
    session['plural_noun'] = request.form['plural_noun']
    return render_template('/stories/1.html') 

@app.route('/stories/2')
def story_two():
    return render_template('/stories/2.html') 

@app.route('/stories/2', methods = ['POST'])
def story_two_post():
    session['adjective']  = request.form['adjective']
    session['noun']  = request.form['noun']
    session['verb']  = request.form['verb']
    session['place']  = request.form['place']
    return render_template('/stories/2.html') 


if __name__ == "__main__":
    app.run(port=8000, debug=True)