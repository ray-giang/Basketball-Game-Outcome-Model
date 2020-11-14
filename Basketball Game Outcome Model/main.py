# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 17:10:21 2020

@author: raygi
"""


import pickle
import pandas as pd
from flask import Flask
from model_files.model import predict_game_outcome
app = Flask(__name__)



@app.route('/predict', methods=['POST','GET'])
def predict():
    df = pd.read_csv('final_game_results.csv')
    retrieved_input = df[:1].to_dict()
    with open('./model_files/model.bin', 'rb') as f_in:
        model = pickle.load(f_in)
    predictions = predict_game_outcome(retrieved_input, model)
    return predictions

@app.route('/ping', methods=['GET'])
def ping():
    return "Pinging Model!!"

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=9696)