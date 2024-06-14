from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class StepForm(FlaskForm):
    date = DateField('Дата', format='%Y-%m-%d', validators=[DataRequired()])#Поле для ввода количества шагов.
    steps = IntegerField('Количество шагов', validators=[DataRequired(), NumberRange(min=0)])#Поле для ввода даты.
    submit = SubmitField('Сохранить') #Кнопка для отправки формы
