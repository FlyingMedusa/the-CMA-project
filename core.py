from flask import Flask, render_template, request, redirect
# from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import os
from os.path import join, dirname, realpath
import tables as tbl
import graphs as gr
import tempfile

app = Flask(__name__)

# app.config.update(
#     SECRET_KEY='mykey',
#     SQLALCHEMY_DATABASE_URI='postgresql://postgres:my password@localhost/catalog_db',
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
# )

# db = SQLAlchemy(app)

# UPLOAD_FOLDER = 'static/files' -> when locally - it worked but that's not what I want
#app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

UPLOAD_FOLDER = tempfile.TemporaryDirectory()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    file = request.files['inputFile']
    if file.filename != '' and '.xls' in file.filename:
        # newFile = FileContents(name=file.filename, data=file.read())
        # db.session.add(newFile)
        # db.session.commit()
        # temporary!
        # return 'Saved ' + file.filename + ' to the database!'
        filename = 'file.xls'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'].name, filename)
        file.save(file_path)

        all_requirements = tbl.analysis(file_path)
        ts_top = all_requirements[0]
        abst_top = all_requirements[1]
        target = all_requirements[2]
        source = all_requirements[3]
        abst_top_target = all_requirements[4]
        abst_top_source = all_requirements[5]
        graph1 = gr.generate_g1(abst_top)
        graph2 = gr.generate_g2(abst_top_target)
        graph3 = gr.generate_g3(abst_top_source)
        return render_template("data.html", ts_top=ts_top, abst_top=abst_top, source=source, target=target, graph1=graph1, graph2=graph2, graph3=graph3)
    return render_template('upload.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()