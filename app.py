from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "render_template('index.html')"
@app.route('/submit',methods=['POST'])
def submit():
    if request.method== 'POST' :
        verb= request.form['verb']
        print(verb)
        return remder_template('index.html')
    if __name == '__main__':
        app.debug = True
        app.run()
