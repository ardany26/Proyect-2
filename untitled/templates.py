from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Registro')
def registro():
    return render_template('registro.html')

@app.route('/input')
def input():
    return render_template('input.html')
        

if __name__ == '__main__':
    app.run(debug = True, port=9000)
 

