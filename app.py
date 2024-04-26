from flask import Flask
import pandas
import numpy
from views2 import views




app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
# app_website.register_blueprint(views, url_prefix="/views/home")
if __name__ == '__main__':
    app.run(debug=True,port=9000) # we set debug = True because whenevever we change a file inside the flask app it will automatically refresh the app
     