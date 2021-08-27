from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id} -{self.title}"

@app.route("/",methods =['GET','POST'])
def hello_world():
    if request.method=="POST":
        title = request.form['title']
        todo = Todo(title=title)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('2.html',allTodo = allTodo)
    #return "<p>Hello, World!</p>"

@app.route("/rishabh")
def rishabh():
    allTodo = Todo.query.all()
    print(allTodo)
    return "<p>Hello rishabh, World!</p>"

@app.route("/update/<int:id>",methods =['GET','POST'])
def update(id):
    if request.method=='POST':
        title = request.form['title']
        todo = Todo.query.filter_by(id=id).first()
        todo.title = title
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
        
    todo = Todo.query.filter_by(id=id).first()
    return render_template('update.html',todo=todo)
    return "<p>Hello rishabh, World!</p>"

@app.route("/delete/<int:id>")
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")
    return "<p>Hello rishabh, World!</p>"

if __name__ =="__main__":
    app.run(debug=True)