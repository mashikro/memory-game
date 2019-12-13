################# Necessary IMPORTS ############################
from jinja2 import StrictUndefined

from flask import Flask, render_template, request, redirect, session, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension

import os
 
#################### FLASK APP SET-UP ####################################
app = Flask(__name__)

app.secret_key = os.environ['FLASK_SECRET_KEY']

app.jinja_env.undefined = StrictUndefined #to prevent silent but deadly jinja errors

######################### ROUTES #####################################

@app.route('/') 
def index():
    '''Index. User can read instructions here for the game'''
    
    return render_template('index.html') 


####################### RUNNING MY SERVER ###############################
if __name__ == "__main__":
   
    app.debug=True # We have to set debug=True here, since it has to be True at the point that we invoke the DebugToolbarExtension

    DebugToolbarExtension(app) # Use the DebugToolbar

    app.run(host="0.0.0.0") 
