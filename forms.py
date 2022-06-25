from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField)
from wtforms.validators import InputRequired, Length


class SitesForm(FlaskForm):
    siteName = StringField('Site Name', validators=[InputRequired(), Length(min=3, max=12)])
    external_ip = StringField('External IP Address', validators=[InputRequired(), Length(min=3, max=15)])
    available = BooleanField('Available', default='checked')
