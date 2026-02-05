from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):    # repr - When this class object is called then it returns sno & title
        return f"{self.sno} - {self.title}"


@app.route('/',methods=['GET','POST']) #should provide methods here to use
def hello():
    if request.method=='POST':
        # print("post")
        title = request.form['title']   #error
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
# todo = Todo(title="First todo", desc="Start investing in stock market")
# db.session.add(todo)
# db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html',allTodo=allTodo)  #To render template
    # return 'Hello, World!'

@app.route('/show')
def prod():  
    allTodo = Todo.query.all()
    print(allTodo)
    return 'this is product page'

@app.route('/update')
def update():  
    allTodo = Todo.query.all()
    print(allTodo)
    return 'this is product page'

@app.route('/delete/<int:sno>')
def delete(sno):  
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

# @app.route('/products')
# def prod():  
#     return 'Hello Product page'

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True,port=8000) #To change default port
    # For development debug=true, to see what the error is
