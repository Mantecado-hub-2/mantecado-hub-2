from flask_wtf import FlaskForm
from wtforms import SubmitField


class CommunitiesForm(FlaskForm):
    submit = SubmitField('Save communities')
