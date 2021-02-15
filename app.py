import datetime as dt
import numpy as np
import pandas as pd
import json

# Add sqlalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# Add flask dependencies
from flask import Flask, jsonify, render_template, request, redirect, url_for



# Set up Flask application
app = Flask(__name__)







# define routes
@app.route("/")
def pilot():
    # read from my database
    from db_connection import postgreSQLConnection
    #read all your data frames
    train_df = pd.read_sql( \
    "select enrollee_id,city,relevent_experience,training_hours from hrds_train_features limit 10", \
    postgreSQLConnection);
    test_df = pd.read_sql( \
    "select enrollee_id,city,relevent_experience,training_hours from hrds_test_features limit 10", \
    postgreSQLConnection);
    #postgreSQLConnection.close()

    #jsonify the data frames
    train=json.loads(train_df.to_json(orient='records'))
    test=json.loads(test_df.to_json(orient='records'))

    # render the webpage with the data passed
    return render_template('index.html',test=test,train=train)

if __name__ == '__main__':
    app.run(debug = True)
