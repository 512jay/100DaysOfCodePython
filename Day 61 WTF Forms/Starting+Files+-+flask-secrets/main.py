from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    name = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "This is my very secret key"
app.testing = True


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = MyForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
