from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField("Your Email:", validators=[DataRequired(), Email("This field requires a valid email address")])
    name = StringField("Your Name:", validators=[DataRequired()])
    password = PasswordField("Your Password:", validators=[DataRequired()])
    submit = SubmitField("Sign me up!")

class LoginForm(FlaskForm):
    email = StringField("Your Email:", validators=[DataRequired(), Email("This field requires a valid email address")])
    password = PasswordField("Your Password:", validators=[DataRequired()])
    submit = SubmitField("Log me in!")

class CommentForm(FlaskForm):
    comment = CKEditorField("Comment Content", validators=[DataRequired()])
    sumbit = SubmitField("Submit Comment")

class ContactForm(FlaskForm):

    email = StringField("Your Email:", validators=[DataRequired(), Email("This field requires a valid email address")])
    name = StringField("Your Name:", validators=[DataRequired()])
    phone = StringField("Your Phone:", validators=[DataRequired()])
    message = StringField("Your Message:", validators=[DataRequired()])
    submit = SubmitField("Submit")

