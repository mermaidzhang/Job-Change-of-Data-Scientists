# Job-Change-of-Data-Scientists
# Overview
Every `Big data` company risks losing their technical resources following initial training as they move on to new jobs. It's very costly both in time and money for the companies to train people and then fill in the vacant technical positions. The objective of this project is to analyze the cause of turnover and come up with solutions to both predict it and prevent it from happening.
This helps `Big Data` companies to reduce the cost and time as well as the quality of training or planning the courses and categorization of candidates.

# Dataset
The [data set](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists) is taken from Kaggle<br>

The dataset is divided into train and test with same features with the exclusion of the target in the test data.

* The dataset is imbalanced.<br>
* Most features are categorical (Nominal, Ordinal, Binary), some with high cardinality.<br>
* Missing imputation that must be addressed in the pipeline.

## Features

|Feature|Description|
|--------------|--------------------------------------------------------------------|
|enrollee_id|Unique ID for candidate|
|city|City code|
|city_ development _index|Developement index of the city (scaled)|
|gender|Gender of candidate|
|relevent_experience|Relevant experience of candidate|
|enrolled_university|Type of University course enrolled if any|
|education_level|Education level of candidate|
|major_discipline|Education major discipline of candidate|
|experience|Candidate total experience in years|
|company_size|No of employees in current employer's company|
|company_type|Type of current employer|
|lastnewjob|Difference in years between previous job and current job|
|training_hours|training hours completed|
|target|0 – Not looking for job change, 1 – Looking for a job change|

## data structure
We created the below database structure for the above dataset<br>
Scripts for generating [database](createDatabase.sql) and [tables](createTables.sql)

## ERD
<img src="ERD_hrds.jpeg" alt="HR data science database" height="500" width="500"> 

# Technologies Used
## Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

## Database Storage
Postgres is the database we intend to use, and we will integrate Tableau to display the data.

## Machine Learning
SciKitLearn is the ML library we'll be using to create a classifier. We will be using the Logistic regression model. This decision was based on the type of data that we are working.

## Dashboard
We will be using HTML, CSS and Java Script to display our findings on a webpage. Plot libraries will be used for displaying graphs.

# Project Management
## Team roles - 1st segment
* `Square`: YI XIN ZHANG. (Set up Github ripository)<br>
* `Triangle`: Pegah. (Mock Machine learning)<br>
* `Circle`: goes to Faramarz (Mock-up database)<br>
* `X-Role`: Adanma Eleweke (Which tools to choose for the project)<br>

## Communications
- We use the Breakout rooms zoom meetings for team meetings<br>
- For the daily communications we have created a slack channel.<br> 
- We also have exchanged emails for sharing repository.<br>

# Summary
The goal of the project is to find out which feature mostly affects the candidate decision of staying or leaving the company. 


