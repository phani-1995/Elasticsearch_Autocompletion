from flask import Flask
from flask import request, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("home.html")


@app.route('/method', methods=["GET", "POST"])
def method():
    data = request.form.get("data")
    payload = {}
    headers= {}
    url = "http://127.0.0.1:4000/autocomplete?query="+str(data)
    response = requests.request("GET", url, headers=headers, data = payload)
    return response.json()


if __name__ == "__main__":
    app.run(debug=True, port=5000)

