from flask_ngrok import run_with_ngrok
from flask import Flask

app = Flask(__name__)
run_with_ngrok(app)  # starts ngrok when the app is run


@app.route("/")
def home():
    return "<h1>Running Flask on Google Colab!</h1>"


app.run()