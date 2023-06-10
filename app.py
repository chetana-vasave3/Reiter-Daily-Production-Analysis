from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import datetime
import pickle

model = pickle.load(open('model.pkl', 'rb'))


app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the input data from the form
    month = datetime.date.today().month
    weekday = datetime.date.today().weekday()

    result_prediction = []
    item_name = []

    for index, item in enumerate(df['Product_Name'].unique()):
        test = [(month, index, weekday)]
        result_prediction.append(int(np.round(model.predict(test))))
        item_name.append(item)

    new_df = pd.DataFrame()
    new_df['item_name'] = item_name
    new_df['prediction'] = result_prediction

    return render_template('result.html', result=new_df)


if __name__ == '__main__':
    app.run(debug=True)
