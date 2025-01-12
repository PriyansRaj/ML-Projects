from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

titanic = pd.read_csv("Titanic-Dataset.csv")
svc = pickle.load(open('SvcModel.pkl', 'rb'))
logistic = pickle.load(open('Logistic.pkl', 'rb'))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == 'POST':
        # Extract form data
        pclass = int(request.form['pclass'])
        embarked = request.form['embarked']
        sex = request.form['sex']
        family_members = int(request.form['family_members'])
        age = float(request.form['age'])
        fare = float(request.form['fare'])

       
        Sex_dict = {"male": 0, "female": 1}
        embarked_dict = {"S": 0, "C": 1, 'Q': 2}

        Sex_num = Sex_dict.get(sex, 0)
        embarked_num = embarked_dict.get(embarked, 2)

       
        features = np.array([[pclass, Sex_num, age, fare, embarked_num, family_members]])

        prediction = logistic.predict(features)

       
        if prediction == 1:
            survival_status = "Survived"
        else:
            survival_status = "Did not survive"

        return render_template("index.html", prediction_text=f"The passenger {survival_status}")

if __name__ == "__main__":
    app.run(debug=True)
