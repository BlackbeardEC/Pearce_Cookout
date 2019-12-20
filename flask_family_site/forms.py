## Import all the things
# 3rd Party
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, MultipleFileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# Local
from flask_family_site.models import User

# Registration Form and Function
class Registration_Form(FlaskForm):
    # Validate all the things are real and/or matching
    username = StringField('Username', validators=[DataRequired(), \
            Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', \
            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('SignUp')

    # Validate unique username
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken, please \
                    choose another.')
    # Validate unique email
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken, please \
                    choose another.')

# Login Form and Function
class Login_Form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# Update Account Form and Function
class Update_Account_Form(FlaskForm):
    # Validate all the things are real and/or matching
    username = StringField('Username', validators=[DataRequired(), \
            Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    pic = FileField('Update Profile Picture', \
            validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    # Validate unique username
    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is already taken, please \
                        choose another.')
    # Validate unique email
    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is already taken, please \
                        choose another.')


class Post_Form(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    images = MultipleFileField('File(s) Upload')
    submit = SubmitField('Submit')

