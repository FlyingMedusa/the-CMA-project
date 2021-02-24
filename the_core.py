from flask import Flask, redirect, url_for, render_template, request, session, flash
import os
from os.path import join, dirname, realpath
import pandas as pd
# from second import second
# import stats as sts
# import graph_gen as gg

app = Flask(__name__)
app.secret_key = "hello"
# app.register_blueprint(second, url_prefix="/")

# UPLOAD_FOLDER = 'static/files'
# app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/us/")
# def us():
#     return render_template("authors.html")


# @app.route("/login/", methods=["POST", "GET"])
# def login():
#     return render_template("login.html")


# @app.route("/upload", methods=['POST'])
# def upload():
#     file = request.files['inputFile']
#     if file.filename != '':
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(file_path)
#         target_top5 = sts.counter("target")
#         source_top5 = sts.counter("source")
#         tlist = sts.counter("tlist")
#         slist = sts.counter("slist")
#         gg.generate_g1(tlist, slist)
#     return render_template("data.html", target_top5=target_top5, source_top5=source_top5)


# @app.route("/logout")
# def logout():
#     return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(port = 5000, debug=True)