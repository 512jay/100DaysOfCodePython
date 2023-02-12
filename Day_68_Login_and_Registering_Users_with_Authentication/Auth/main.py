from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# Login Manager
login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = '38c3f7101d215271a968aeb51d0577416b25712b7711d38a009a38c679772d55'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


# Line below only required once, when creating DB.
# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('secrets', name=new_user.name))
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for("secrets", name="someName"))
    return render_template("login.html")


@app.route('/secrets/<name>')
def secrets(name):
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    file_path = "files/cheat_sheet.pdf"
    return send_from_directory(directory=app.static_folder, path='files/cheat_sheet.pdf')
    # return send_from_directory(directory='static', path=file_path)


if __name__ == "__main__":
    app.run(debug=True)