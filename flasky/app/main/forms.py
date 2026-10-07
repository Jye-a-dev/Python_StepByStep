from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class NameForm(FlaskForm):
    username = StringField('What is your username?', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
