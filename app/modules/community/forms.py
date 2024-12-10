from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField
from wtforms.validator import DataRequired, Length


class CommunityForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=50)])
    description = TextAreaField("Description", validators=[DataRequired(), Length(min=3, max=1000)])

    submit = SubmitField("Community Succesfully Created")
