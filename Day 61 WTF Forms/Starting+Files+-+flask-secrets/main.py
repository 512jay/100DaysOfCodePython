from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    recaptcha = RecaptchaField()


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
