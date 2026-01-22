from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User, University

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=3, max=64)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Это имя пользователя уже занято.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Этот email уже зарегистрирован.')

class UniversityForm(FlaskForm):
    full_name = StringField('Полное название', validators=[DataRequired(), Length(max=255)])
    short_name = StringField('Сокращённое название', validators=[DataRequired(), Length(max=50)])
    creation_date = DateField('Дата создания', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Сохранить')

class StudentForm(FlaskForm):
    full_name = StringField('ФИО', validators=[DataRequired(), Length(max=255)])
    birth_date = DateField('Дата рождения', format='%Y-%m-%d', validators=[DataRequired()])
    university_id = SelectField('Университет', coerce=int, validators=[DataRequired()])
    enrollment_year = IntegerField('Год поступления', validators=[DataRequired()])
    submit = SubmitField('Сохранить')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.university_id.choices = [(u.id, u.short_name) for u in University.query.order_by('short_name').all()]