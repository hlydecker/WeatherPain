from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

class PainForm(FlaskForm):
    pain_score = IntegerField('Pain Score', validators=[DataRequired(), NumberRange(min=0, max=10)])
    latitude = FloatField('Latitude', validators=[DataRequired()])
    longitude = FloatField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Submit')
