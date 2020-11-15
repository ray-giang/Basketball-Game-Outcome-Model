# Springboard - Machine Learning Engineer Career Track

This program teaches all of the fundementals of becoming a Machine Learning Engineer.
It includes a set of mini projects and a capstone project.

Under is a Table of Contents which outlines the curriculum through mini projects, capstone submissions, the current and future outlook of the capstone project

## Table of Contents

### 1. Mini Projects
* [APIs](https://github.com/ray-giang/Springboard/blob/master/Mini%20Projects/Mini_Project_Data_Wrangling_at_Scale_with_Spark.ipynb)
* [Data Wrangling](https://github.com/ray-giang/Springboard/blob/master/Mini%20Projects/Mini_Project_Data_Wrangling_at_Scale_with_Spark.ipynb)
* [Spark SQL](https://github.com/ray-giang/Springboard/blob/master/Mini%20Projects/Mini_Project_SQL_with_Spark.ipynb)
* [Linear Regression](https://github.com/ray-giang/Springboard/blob/master/Mini%20Projects/Mini_Project_Linear_Regression.ipynb)
* [Logistic Regression](https://github.com/ray-giang/Springboard/blob/master/Mini%20Projects/Mini_Project_Logistic_Regression.ipynb)
* [Clustering](https://github.com/ray-giang/Springboard/blob/master/Mini%20Projects/Mini_Project_Clustering.ipynb)
* [Tree Based Algorithms](https://github.com/ray-giang/Springboard/blob/master/Mini%20Projects/Mini_Project_Tree-Based_Algorithms.ipynb)
* [ML with Spark](https://github.com/ray-giang/Springboard/blob/master/Mini%20Projects/Mini_Project_Spark_ML.ipynb)

### 2. Capstone Submissions
* [Web Scraping](https://github.com/ray-giang/Springboard/blob/master/Basketball%20Game%20Outcome%20Model/SB%20Capstone%20Project%20-%20Web%20Scraping%20.ipynb)
* [Data Manipulations](https://github.com/ray-giang/Springboard/blob/master/Basketball%20Game%20Outcome%20Model/SB%20Capstone%20Project%20-%20Data%20Manipulations.ipynb)
* [ML Prototype](https://github.com/ray-giang/Springboard/blob/master/Basketball%20Game%20Outcome%20Model/Springboard%20-%20Modelling%20Cleaned.ipynb)
* [DL Prototype](https://github.com/ray-giang/Springboard/blob/master/Basketball%20Game%20Outcome%20Model/SB_Capstone_Project_DL_Prototype.ipynb)
* [Deployment](https://github.com/ray-giang/Springboard/blob/master/Basketball%20Game%20Outcome%20Model/main.py)

### 3. Basketball Game Outcome Prediction

#### Outline
My Capstone Project is to predict the likelihood of a team winning a basketball game.
Using webscrapped data from 2000-2020 season, data is manipulated to have advanced metrics and rolling team statistics. Using all of the results from the capstone submissions, the predictive model is deployed in production locally. There are four main components of this project:

* [Dataset](https://github.com/ray-giang/Springboard/blob/master/Basketball%20Game%20Outcome%20Model/final_game_results.csv)
* [Gradient Boosting Model Parameters](https://github.com/ray-giang/Springboard/blob/master/Basketball%20Game%20Outcome%20Model/model.bin)
* [Prediction Function](https://github.com/ray-giang/Springboard/blob/master/Basketball%20Game%20Outcome%20Model/model.py)
* [Flask API](https://github.com/ray-giang/Springboard/blob/master/Basketball%20Game%20Outcome%20Model/main.py)

#### Current Process 
Currently, this is how the model makes a prediction:
1. API retrieves a fixed observation from historical data of games
2. API loads the saved model parameters 
3. API calls the prediction function to predict the outcome of the game using the retrieved observation and model parameters
4. Server returns the probability at which Team A will win the game 

#### Future Process
For future versions, this project will have additional features. This will include the following:
1. Refactored code for web scraping and data preprocessing
2. Public server 
3. User interface that asks the end user for the two teams that will be playing

By having these additional features, this will allow the product to do the following steps:
1. Webscrape [Basketball Reference](https://www.basketball-reference.com/) for recent game outcomes
2. Normalize the data to better fit the model
3. Create dynamic interface that can predict the outcome of any upcoming game
