from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'dev-secret-change-in-production'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(120), nullable=False)
    grade = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    students = Student.query.order_by(Student.id).all()
    return render_template('index.html', students=students)

@app.route('/add', methods=('GET', 'POST'))
def add_student():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        course = request.form.get('course', '').strip()
        grade = request.form.get('grade', '').strip()

        if not (name and age and course and grade):
            flash('Please fill all fields')
            return redirect(url_for('add_student'))

        try:
            age = int(age)
        except ValueError:
            flash('Age must be a number')
            return redirect(url_for('add_student'))

        new_student = Student(name=name, age=age, course=course, grade=grade)
        db.session.add(new_student)
        db.session.commit()
        flash('Student added successfully')
        return redirect(url_for('index'))

    return render_template('add_student.html')

@app.route('/view/<int:student_id>')
def view_student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('view_student.html', student=student)

@app.route('/edit/<int:student_id>', methods=('GET', 'POST'))
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        course = request.form.get('course', '').strip()
        grade = request.form.get('grade', '').strip()

        if not (name and age and course and grade):
            flash('Please fill all fields')
            return redirect(url_for('edit_student', student_id=student_id))

        try:
            age = int(age)
        except ValueError:
            flash('Age must be a number')
            return redirect(url_for('edit_student', student_id=student_id))

        student.name = name
        student.age = age
        student.course = course
        student.grade = grade
        db.session.commit()
        flash('Student updated successfully')
        return redirect(url_for('index'))

    return render_template('edit_student.html', student=student)

@app.route('/delete/<int:student_id>', methods=('POST',))
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
