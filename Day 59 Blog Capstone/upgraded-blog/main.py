from flask import Flask, render_template, request
import requests

url = "https://api.npoint.io/cc03a5956b41677ec7b6"
app = Flask(__name__)

response = requests.get(url)
datas = response.json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", datas=datas)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", header="Successfully sent your message")
    return render_template("contact.html", header="Contact Me")


@app.route("/post.html/<num>")
def post(num):
    post_data = datas[int(num) - 1]
    return render_template("post.html", post=post_data)


@app.route("/form-entry", methods=["POST", "GET"])
def receive_data():
    print(request.method)
    # Write your code here.
    if request.method == "POST":
        return "<h1>Successfully sent your message</h1>"

        # print(type(request))
        # name = request.form["name"]
        # email = request.form["email"]
        # phone = request.form["phone"]
        # message = request.form["message"]
        #
        # return f"<h1>Successfully sent your message</h1>\n" \
        #        f"{name}\n" \
        #        f"{email}\n" \
        #        f"{phone}\n" \
        #        f"{message}"

    return f"It did not work!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
