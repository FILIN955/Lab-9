from flask import Flask, render_template, redirect, url_for
from model import db, Step
from vvod import StepForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///steps.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = StepForm()
    if form.validate_on_submit():
        new_step = Step(date=form.date.data, steps=form.steps.data)
        db.session.add(new_step)
        db.session.commit()
        return redirect(url_for('index'))

    steps = Step.query.all()
    return render_template('index.html', form=form, steps=steps)


if __name__ == '__main__':
    app.run(debug=True)
