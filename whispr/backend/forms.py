from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from whispr.backend.models import User

"""
DataRequired -- Forces the user to input some type of data, no whitespace allowed to be inputted.
Length -- Minimum and Maximum amount of characters for a certain field
Email -- Checks if email is valid
EqualTo -- Checks if the confirm password field is the same as the password field (if its equal to duh)
"""

# SignUP form | Author: Andre Nunes da Silva 04/22/26

class RegistrationForm(FlaskForm): # included validators, a username must have a min of 2 characters and a max of 20 chars
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    # Functions used for validating if usernames or emails are taken, raises an exception and prints {user, email} is taken

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Username is taken, choose a different username.')
        
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email is taken, choose a different email.')

# Login form | Author: Andre Nunes da Silva 04/22/26

class LoginForm(FlaskForm): # included validators, a username must have a min of 2 characters and a max of 20 chars

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')