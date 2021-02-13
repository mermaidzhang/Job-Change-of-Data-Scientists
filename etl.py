# Dependencies
import pandas as pd
import numpy as np
import psycopg2
import random
from db_connection import postgreSQLConnection

# Import dependencies

from sklearn.preprocessing import LabelEncoder


# read the tables
hrds_train_features_df      = pd.read_sql("select * from \"hrds_train_features\"", postgreSQLConnection);
hrds_train_labels_df      = pd.read_sql("select * from \"hrds_train_labels\"", postgreSQLConnection);
hrds_test_df = pd.read_sql("select * from \"hrds_test_features\"", postgreSQLConnection);

#Merge the dataset
hrds_train_df = hrds_train_features_df.merge(hrds_train_labels_df, on='enrollee_id', how='left')

#drop the 
hrds_train_df.drop('enrollee_id', axis=1, inplace=True)
hrds_test_df.drop('enrollee_id', axis=1, inplace=True)


# fill missing data  
hrds_train_df['experience'] = hrds_train_df['experience'].fillna('-1')
hrds_train_df['last_new_job'] = hrds_train_df['last_new_job'].fillna('-1')
hrds_train_df['enrolled_university'] = hrds_train_df['enrolled_university'].fillna('Unknown')
hrds_train_df['major_discipline'] = hrds_train_df['major_discipline'].fillna('Others')
hrds_train_df['education_level'] = hrds_train_df['education_level'].fillna('Unknown')

hrds_test_df['experience'] = hrds_test_df['experience'].fillna('-1')
hrds_test_df['last_new_job'] = hrds_test_df['last_new_job'].fillna('-1')
hrds_test_df['enrolled_university'] = hrds_test_df['enrolled_university'].fillna('Unknown')
hrds_test_df['major_discipline'] = hrds_test_df['major_discipline'].fillna('Others')
hrds_test_df['education_level'] = hrds_test_df['education_level'].fillna('Unknown')

#import random
def na_randomfill(series):
    na_mask = pd.isnull(series)   # boolean mask for null values
    n_null = na_mask.sum()        # number of nulls in the Series
    
    if n_null == 0:
        return series             # if there are no nulls, no need to resample
    
    # Randomly sample the non-null values from our series
    #  only sample this Series as many times as we have nulls 
    fill_values = series[~na_mask].sample(n=n_null, replace=True, random_state=0)

    # This ensures our new values will replace NaNs in the correct locations
    fill_values.index = series.index[na_mask]
    
    return series.fillna(fill_values)

out = na_randomfill(hrds_train_df["company_type"])
out_1 = na_randomfill(hrds_train_df["company_size"])
out_2 = na_randomfill(hrds_train_df["gender"])

hrds_train_df["company_type"] = out  
hrds_train_df["company_size"] = out_1
hrds_train_df["gender"] = out_2

out = na_randomfill(hrds_test_df["company_type"])
out_1 = na_randomfill(hrds_test_df["company_size"])
out_2 = na_randomfill(hrds_test_df["gender"])

hrds_test_df["company_type"] = out  
hrds_test_df["company_size"] = out_1
hrds_test_df["gender"] = out_2

# strip the 'city_' from city
hrds_test_df['city'] = hrds_test_df['city'].map(lambda x:int(x.strip().strip('city_')))
hrds_train_df['city'] = hrds_train_df['city'].map(lambda x:int(x.strip().strip('city_')))
hrds_test_df['city'] = hrds_test_df['city'].map(lambda x:int(x))
hrds_train_df['city'] = hrds_train_df['city'].map(lambda x:int(x))

# Fitting and encoding the columns with the LabelEncoder
# Create the LabelEncoder instance
le = LabelEncoder()

# gender column
le.fit(hrds_train_df["gender"])
hrds_train_df["gender"] = le.transform(hrds_train_df["gender"])
le.fit(hrds_test_df["gender"])
hrds_test_df["gender"] = le.transform(hrds_test_df["gender"])

# city column
le.fit(hrds_train_df["city"])
hrds_train_df["city"] = le.transform(hrds_train_df["city"])
le.fit(hrds_test_df["city"])
hrds_test_df["city"] = le.transform(hrds_test_df["city"])

# Encoding relevent_experience column
le.fit(hrds_train_df["relevent_experience"])
hrds_train_df["relevent_experience"] = le.transform(hrds_train_df["relevent_experience"])
le.fit(hrds_test_df["relevent_experience"])
hrds_test_df["relevent_experience"] = le.transform(hrds_test_df["relevent_experience"])

# Encoding enrolled_university column
le.fit(hrds_train_df["enrolled_university"])
hrds_train_df["enrolled_university"] = le.transform(hrds_train_df["enrolled_university"])
le.fit(hrds_test_df["enrolled_university"])
hrds_test_df["enrolled_university"] = le.transform(hrds_test_df["enrolled_university"])

# Encoding education_level column
le.fit(hrds_train_df["education_level"])
hrds_train_df["education_level"] = le.transform(hrds_train_df["education_level"])
le.fit(hrds_test_df["education_level"])
hrds_test_df["education_level"] = le.transform(hrds_test_df["education_level"])

# Encoding major_discipline column
le.fit(hrds_train_df["major_discipline"])
hrds_train_df["major_discipline"] = le.transform(hrds_train_df["major_discipline"])
le.fit(hrds_test_df["major_discipline"])
hrds_test_df["major_discipline"] = le.transform(hrds_test_df["major_discipline"])

# Encoding experience column
le.fit(hrds_train_df["experience"])
hrds_train_df["experience"] = le.transform(hrds_train_df["experience"])
le.fit(hrds_test_df["experience"])
hrds_test_df["experience"] = le.transform(hrds_test_df["experience"])

# Encoding company_size column
le.fit(hrds_train_df["company_size"])
hrds_train_df["company_size"] = le.transform(hrds_train_df["company_size"])
le.fit(hrds_test_df["company_size"])
hrds_test_df["company_size"] = le.transform(hrds_test_df["company_size"])

# Encoding company_type column
le.fit(hrds_train_df["company_type"])
hrds_train_df["company_type"] = le.transform(hrds_train_df["company_type"])
le.fit(hrds_test_df["company_type"])
hrds_test_df["company_type"] = le.transform(hrds_test_df["company_type"])

# Encoding last_new_job column
le.fit(hrds_train_df["last_new_job"])
hrds_train_df["last_new_job"] = le.transform(hrds_train_df["last_new_job"])
le.fit(hrds_test_df["last_new_job"])
hrds_test_df["last_new_job"] = le.transform(hrds_test_df["last_new_job"])

# We bin as follows
#0 to 100
#101 to 250
#251 and up
bins = [-np.inf, 101, 251, np.inf]
hrds_train_df['training_buckets'] =     pd.cut(hrds_train_df['training_hours'], bins,labels=['100 or less','101 to 250','251 and up'])
hrds_test_df['training_buckets'] =     pd.cut(hrds_test_df['training_hours'], bins,labels=['100 or less','101 to 250','251 and up'])


def city_index_bin(x):
    if x < 0.63:
        return 'low density'
    elif (x >= 0.63) and (x < 0.91):
        return 'medim density'
    else:
        return 'high density'

'''
We bin as follows
< 0.63: 'low density'
>= 0.63 and < 0.91:'medium density'
>= 0.91: return 'high density'
'''
hrds_train_df['city_index_buckets'] = hrds_train_df['city_development_index'].map(city_index_bin)
hrds_test_df['city_index_buckets'] = hrds_test_df['city_development_index'].map(city_index_bin)

def train_experience_bin(x):
    if x  <=10:
        return 'junior'
    elif x >10 and x<19:
        return 'associate'
    else:
        return 'senior'

def test_experience_bin(x):
    if x in ['<1','1','2','3','4','5','6','7','8','9','10']:
        return 'junior'
    elif x in ['11','12','13','14','15','16','17','18']:
        return 'associate'
    else:
        return 'senior'

hrds_train_df['experience_buckets'] = hrds_train_df['experience'].map(train_experience_bin)
hrds_test_df['experience_buckets'] = hrds_test_df['experience'].map(test_experience_bin)


# Encode the binned features for training
le.fit(hrds_train_df["training_buckets"])
hrds_train_df["training_encoded"] = le.transform(hrds_train_df["training_buckets"])
le.fit(hrds_train_df["city_index_buckets"])
hrds_train_df["city_index_encoded"] = le.transform(hrds_train_df["city_index_buckets"])
le.fit(hrds_train_df["experience_buckets"])
hrds_train_df["experience_encoded"] = le.transform(hrds_train_df["experience_buckets"])
# Encode the binned features for test
le.fit(hrds_test_df["training_buckets"])
hrds_test_df["training_encoded"] = le.transform(hrds_test_df["training_buckets"])
le.fit(hrds_test_df["city_index_buckets"])
hrds_test_df["city_index_encoded"] = le.transform(hrds_test_df["city_index_buckets"])
le.fit(hrds_test_df["experience_buckets"])
hrds_test_df["experience_encoded"] = le.transform(hrds_test_df["experience_buckets"])

hrds_train_df.head()
hrds_test_df.head()

postgreSQLConnection.close()
