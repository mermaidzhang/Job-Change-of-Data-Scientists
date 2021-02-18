import datetime as dt
import numpy as np
import pandas as pd
import json

# sklearn dependencies
from sklearn import preprocessing

# Add sqlalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

    # dependencies
from db_connection import postgreSQLConnection
import pickle5 as pickle


# Add flask dependencies
from flask import Flask, jsonify, render_template, request, redirect, url_for



# Set up Flask application
app = Flask(__name__)


@app.route("/", methods=['post', 'get'])
def pilot():
    from etl import hrds_train_df,hrds_test_df,result_metrics
    y = hrds_train_df['target']
    hrds_train_df = hrds_train_df.drop(['target'],axis=1)
    hrds_train_df = hrds_train_df.drop(['training_buckets','city_index_buckets','experience_buckets'],axis=1)
    hrds_test_df = hrds_test_df.drop(['training_buckets','city_index_buckets','experience_buckets'],axis=1)

    all_models_accuracy = pd.read_sql("select * from \"all_models_accuracy\"", postgreSQLConnection);
    all_models_cm = pd.read_sql("select * from \"all_models_cm\"", postgreSQLConnection);
    # check if it's a POST

    if request.method == "POST":
        mdl = request.form.get('model')
        ds = request.form.get('dataset')

        if ds=='train':
            features_tbl = "hrds_train_features"
            dataset_df=hrds_train_df

        elif ds=='test':
            features_tbl="hrds_test_features"
            dataset_df=hrds_test_df

        else:
            features_tbl="unknown"
            dataset_df="unknown"
        
        if mdl=='rf':
            model='rf.sav'
        elif mdl=='lr':
            model='lr.sav'
            # We need to scale the data for logistic regression
            scaler = preprocessing.StandardScaler().fit(dataset_df)
            dataset_df = scaler.transform(dataset_df)
        elif mdl == 'knn':
            model='knn.sav'
        else:
            model='unknown'
        #return(f'selected dataset:"{ds}"\tselected model:"{mdl}"')

    else:
        ds="train"
        mdl="rf"
        dataset_df=hrds_train_df
        model='rf.sav'
        features_tbl = "hrds_train_features"

    # start processing **************************************************************
    lookup = {'train':'Training','test':'Test','rf':'Random Forest','lr':'Logistic Regression','knn':'KNN'}
    sel1=json.dumps(lookup[ds])
    sel2=json.dumps(lookup[mdl])
    # get the features
    features_df = pd.read_sql(f"select * from {features_tbl}", postgreSQLConnection);
    features = ['city','city_development_index','gender','relevent_experience','enrolled_university','education_level', \
        'major_discipline','experience','company_size','company_type','last_new_job','training_hours']
    chart1 = features_df.count()
    chart1=chart1.to_frame()
    chart1 = chart1.rename(columns={0:'count'})
    chart1['Features']=chart1.index
    chart1.set_index('Features',drop=True,inplace=True)
    chart1=chart1.to_html(classes=["table-bordered","table-striped"])

    # Run the model
    df = dataset_df
    loaded_model = pickle.load(open(f'{model}', 'rb'))
    predicted = loaded_model.predict(df)
    chart2 = np.unique(predicted,return_counts = True)[1]
    chart2 = pd.DataFrame(chart2)
    chart2['pred']=chart2.index.map(lambda x:'Likely to Stay' if x==0 else 'Likely to Leave')
    chart2 = chart2.set_index('pred',drop=True)
    chart2 = chart2.rename(columns={0:'count'})
    results = chart2
    sum = results.sum()
    results['percentage'] = results['count'].apply(lambda x: (x/sum) )
    results = results.to_html(classes=["table-bordered","table-striped"])
    chart2 = [chart2.index.to_list(),chart2['count'].to_list()]
    chart2=json.dumps(chart2)
    
    # predictions tab2
    chart5 = chart2

    rf_imp_df = pd.read_csv ('Resources/Random_tree_features.csv')
    #print(rf_imp_df['Values'])
    chart6 = [rf_imp_df['Values'].to_list(), rf_imp_df['Feature-Importances'].to_list()]
    chart6 = json.dumps(chart6)

    # accuracy report only available for training dataset
   
    if ds == 'train':
        chart4, chart3 = result_metrics(y, predicted, mdl)
        chart3 = chart3.to_html(classes=["table-bordered","table-striped"])
        chart4 = chart4.to_html(classes=["table-bordered","table-striped"])
        
    else:
            chart3=pd.DataFrame({'Message':'Accuracy is available only for training dataset'},index=[1])
            chart4=pd.DataFrame({'Message':'Confusion matrix is available only for training dataset'},index=[1])
            chart3=chart3.to_html(classes=["table-responsive","table-bordered","table-s","table-striped"])
            chart4 = chart4.to_html(classes=["table-responsive","table-bordered","table-s","table-striped"])
            #chart6 = pd.DataFrame({'Message':'Feature Impotance bar chart is available only for training dataset'},index=[1])
    
    chart9 = all_models_accuracy.to_html(classes=["table-responsive","table-bordered","table-striped"])
    chart10 = all_models_cm.to_html(classes=["table-responsive","table-bordered","table-striped"])

    return render_template('index.html',results=results,chart1=chart1,chart2=chart2,chart3=chart3,chart4=chart4,chart5=chart5,chart6=chart6,chart9=chart9,chart10=chart10,sel1=sel1,sel2=sel2)


if __name__ == '__main__':
    app.run(debug=True)
