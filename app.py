from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')  #To render template
    # return 'Hello, World!'

@app.route('/products')
def prod():  
    return 'Hello Product page'

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True,port=8000) #To change default port
