from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Optional, Length, Email, EqualTo, ValidationError

class SubmitForm(FlaskForm):
    major = StringField("Major", validators = [DataRequired()])

    
