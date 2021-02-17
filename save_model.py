# Run and save the model

# import dependencies
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from db_connection import postgreSQLConnection
import pandas as pd

# conda install -c conda-forge pickle5
import pickle5 as pickle
from etl import hrds_train_df,result_metrics
from db_connection import postgreSQLConnection

# drop the categorical values
hrds_train_df = hrds_train_df.drop(['training_buckets','city_index_buckets','experience_buckets'],axis=1)

X =hrds_train_df.drop("target" , axis =1)
y = hrds_train_df["target"]


X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    random_state=1, 
                                                    stratify=y)

# Create a random forest classifier.
rf_model = RandomForestClassifier(n_estimators=128, random_state=78)
# Fitting the model
rf_model = rf_model.fit(X_train, y_train)
# Save the model
filename = 'rf.sav'
pickle.dump(rf_model, open(filename, 'wb'))

# Calculate the balanced accuracy score
y_pred = rf_model.predict(X_test)
rf_cm, rf_acc = result_metrics(y_test, y_pred, 'RandomForest')

# We need to scale the data for logistic regression
scaler = preprocessing.StandardScaler().fit(X_train)
X_scaled = scaler.transform(X_train)

#Run and save logical regression
# Train the Logistic Regression model using the resampled data

model = LogisticRegression(solver='lbfgs', random_state=1)
model.fit(X_scaled, y_train)
filename = 'lr.sav'
pickle.dump(model, open(filename, 'wb'))

# Calculate the balanced accuracy score
y_pred = model.predict(X_test)
lr_cm, lr_acc = result_metrics(y_test, y_pred, 'LogisticRegression')


#from sklearn.cross_validation import cross_val_score
# instantiate learning model (k = 3)
knn_model = KNeighborsClassifier(n_neighbors=3)
# fit the model
knn_model.fit(X_train, y_train)
filename = 'knn.sav'
pickle.dump(knn_model, open(filename, 'wb'))

# Calculate the balanced accuracy score
y_pred = pd.DataFrame(knn_model.predict(X_test))
knn_cm, knn_acc = result_metrics(y_test, y_pred, 'KNN')

# Save scores and confusion metrics for all the models
accuracy_df = pd.concat([rf_acc,lr_acc,knn_acc],axis=0)
accuracy_df = accuracy_df.sort_values(by='accuracy',ascending=False)
confusion_df = pd.concat([rf_cm,lr_cm,knn_cm])

# Persist the results in postgres
accuracy_df.to_sql('all_models_accuracy', postgreSQLConnection, if_exists='fail')
confusion_df.to_sql('all_models_cm', postgreSQLConnection, if_exists='fail')