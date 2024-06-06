from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/adlib')
def adlib():
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural_noun = request.args['plural_noun']
    return render_template('adlib.html',place,noun,verb,adjective,plural_noun)



if __name__ == '__main__':
    app.run(debug=True)