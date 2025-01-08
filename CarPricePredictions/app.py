from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

car = pd.read_csv("Cleaned_car_dataset.csv")

@app.route("/home")
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = ['Petrol', 'Diesel', 'LPG']
    return render_template("index.html", companies=companies, car_models=car_models, years=year, fuel_type=fuel_type)
@app.route('/')
def landing():
    return render_template("landing.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
     
        company = request.form.get('company')
        car_model = request.form.get('model')
        year = int(request.form.get('year'))
        fuel_type = request.form.get('fuel_type')
        km = int(request.form.get('km'))

       
        fuel_mapping = {'Diesel': (1, 0, 0), 'Petrol': (0, 1, 0), 'LPG': (0, 0, 1)}
        d, p, l = fuel_mapping.get(fuel_type, (0, 0, 0))

        input_data = pd.DataFrame([[car_model, company, year, km, d, l, p]],
                                  columns=['name', 'company', 'year', 'kms_driven',
                                           'fuel_type_Diesel', 'fuel_type_LPG', 'fuel_type_Petrol'])

      
        prediction = model.predict(input_data)
        print(prediction)

       
        return f"{np.round(prediction[0][0], 2)}"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
