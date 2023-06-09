import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app,db  # Definitions initialization
from model.favorites import initFAVs

# setup APIs
from api.favorite import FAV_api


# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition


# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

# register URIs
app.register_blueprint(app_projects) # register app pages
app.register_blueprint(FAV_api)

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/table/')  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")

@app.before_first_request
def activate_job():  # activate these items 
    initFAVs()

#@app.after_request
#def after_request(response):
    #response.headers.add('Access-Control-Allow-Origin', '*')
    #response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    #response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS, PATCH')
    #return response


# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8086")
