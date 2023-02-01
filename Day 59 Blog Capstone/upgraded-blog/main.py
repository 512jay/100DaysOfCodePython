from flask import Flask, render_template
import requests

url = "https://api.npoint.io/cc03a5956b41677ec7b6"
app = Flask(__name__)

response = requests.get(url)
data = response.json()
print(data)

@app.route('/')
def get_all_posts():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/post.html")
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
