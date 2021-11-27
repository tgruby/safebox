import os
import uuid

from flask import Flask, render_template, session, request, redirect, url_for, jsonify

# Create app and set the directory where we store web resources
app = Flask(
    __name__,
    static_url_path='/resources',
    static_folder="www/resources",
    template_folder="www",
    instance_relative_config=True
)
app.config['UPLOAD_FOLDER'] = 'tmp-upload'
app.config['MAX_CONTENT_PATH'] = 33554432 # 32 MB = 1024 * 1024 * 32


# Generate a nice key using secrets.token_urlsafe()
# app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'pfF4skove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')


# Initialize our application the first time it has started.
# @app.before_first_request
# def init_database():
#     pass


# Return Login Route
@app.route("/")
def root():
    return render_template('index.html')


# Upload File
@app.route('/upload', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'

# Maintain good database connection hygiene
# @app.before_request
# def before_request():
#     #if db.database.is_closed():
#     #   db.database.connect()


# Maintain good database connection hygiene
# @app.after_request
# def after_request(response):
#     #if not db.database.is_closed():
#     #    db.database.close()
#     #return response
