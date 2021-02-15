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
    # check if it's a POST


    # dependencies
    from db_connection import postgreSQLConnection
    import numpy as np
    import pandas as pd
    import pickle5 as pickle
    import matplotlib.pyplot as plt


    hrds_train_features = pd.read_sql("select * from \"hrds_train_features\"", postgreSQLConnection);

    # import model and get predictions on the dataset
    filename='finalized_model.sav'
    from etl import hrds_train_df,result_metrics

    # get the features
    features = ['city','city_development_index','gender','relevent_experience','enrolled_university','education_level', \
        'major_discipline','experience','company_size','company_type','last_new_job','training_hours']
    chart1 = hrds_train_features.count()
    chart1=chart1.to_frame()
    chart1 = chart1.rename(columns={0:'count'})
    chart1['Features']=chart1.index
    chart1.set_index('Features',drop=True,inplace=True)
    chart1=chart1.to_html()

    # Run the model
    df = hrds_train_df.drop(['training_buckets','city_index_buckets','experience_buckets','target'],axis=1)
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    predicted = loaded_model.predict(df)

    # save results
    y = hrds_train_df['target']
    chart2 = np.unique(y,return_counts = True)[1]
    chart2 = pd.DataFrame(chart2)[0]
    
    chart5 = np.unique(y,return_counts = True)[1]
    chart5 = pd.DataFrame(chart2)[0]
    
    # accuracy report
    chart4, chart3 = result_metrics(y, predicted, 'RandomForest')
    
    chart3=chart3.to_html()


    chart4 = chart4.to_html()

    #jsonify the data frames
    chart2=json.loads(chart2.to_json(orient='records'))
    chart5=json.loads(chart5.to_json(orient='records'))

    # render the webpage with the data passed
    return render_template('index.html',chart1=chart1,chart2=chart2,chart3=chart3,chart4=chart4,chart5=chart5)

if __name__ == '__main__':
    app.run(debug=True)
