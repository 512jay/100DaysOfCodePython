from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    email = EmailField(label='Email',
                       validators=[DataRequired(), Email(granular_message=True,check_deliverability=True)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
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

    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com":
            if login_form.password.data == "12345678":
                return render_template('success.html')

    if login_form.validate_on_submit():
        return render_template('denied.html')
    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
