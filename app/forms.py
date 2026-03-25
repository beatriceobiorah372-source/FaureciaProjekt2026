from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email')
    submit = SubmitField('Speichern')

class ProjectForm(FlaskForm):
    titel = StringField('Projekt', validators=[DataRequired()])
    user_id = SelectField('Benutzer', coerce=int)
    submit = SubmitField('Speichern')

class ForecastForm(FlaskForm):
    wert = FloatField('Betrag (€)', validators=[DataRequired()])
    projekt_id = SelectField('Projekt', coerce=int)
    submit = SubmitField('Speichern')
