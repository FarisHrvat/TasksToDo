from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.date}: {self.task}>'

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    date = request.form['date']
    task = request.form['task']
    new_task = Task(date=date, task=task)
    db.session.add(new_task)
    db.session.commit()
    return 'Success'

@app.route('/done/<int:task_id>')
def done(task_id):
    task = Task.query.get(task_id)
    task.done = True
    db.session.commit()
    return 'Success'

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
