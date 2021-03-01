from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    jsonify,
    request,
    session,
    send_file,
)
from werkzeug import secure_filename
import os
import time


UPLOAD_FOLDER = "/static/UPLOADS"

app = Flask(__name__)

app.secret_key = "RPS@108_189_059"
app.config["UPLOADS"] = UPLOAD_FOLDER


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    person_ = request.files["person"]
    cloth_ = request.files["cloth"]

    person_.save(os.path.join("static", "UPLOADS", "person.png"))
    cloth_.save(os.path.join("static", "UPLOADS", "cloth.png"))

    return render_template("home.html", status=True)


@app.route("/get_image/<filename>", methods=["GET"])
def get_image(filename):
    print(filename)
    return send_file("./static/UPLOADS/" + filename, as_attachment=True)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
