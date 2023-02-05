from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html', library=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        book_data = {
            "title": request.form['title'],
            "author": request.form['author'],
            "rating": request.form['rating'],
        }
        all_books.append(book_data)
        print(all_books)
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route("/login", methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        return f"<h1>Name: {request.form['name']}, Password: {request.form['password']}"

if __name__ == "__main__":
    app.run(debug=True)

