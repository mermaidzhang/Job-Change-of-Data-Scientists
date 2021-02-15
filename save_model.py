# Run and save the model

# import dependencies
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
# conda install -c conda-forge pickle5
import pickle5 as pickle
from etl import hrds_train_df

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
filename = 'finalized_model.sav'
pickle.dump(rf_model, open(filename, 'wb'))
