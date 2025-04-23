from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User, Question, UserAnswer

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        gender = request.form['gender']
        user = User(name=name, age=age, gender=gender)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('quiz', user_id=user.id))
    return render_template('index.html')

@app.route('/quiz/<int:user_id>', methods=['GET', 'POST'])
def quiz(user_id):
    questions = Question.query.all()
    if request.method == 'POST':
        for question in questions:
            ans = request.form.get(f'q{question.id}')
            user_answer = UserAnswer(user_id=user_id, question_id=question.id, answer=ans)
            db.session.add(user_answer)
        db.session.commit()
        return redirect(url_for('result', user_id=user_id))
    return render_template('quiz.html', questions=questions, user_id=user_id)

@app.route('/result/<int:user_id>')
def result(user_id):
    user = User.query.get_or_404(user_id)
    answers = UserAnswer.query.filter_by(user_id=user_id).all()
    return render_template('result.html', user=user, answers=answers)

