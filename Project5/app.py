from flask import Flask, render_template, request
import pickle
import os
import numpy as np

app = Flask(__name__)
MODEL_FOLDER = 'models'


models = [f for f in os.listdir(MODEL_FOLDER) if f.endswith('.pkl')]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    selected_model = None

    if request.method == 'POST':
        selected_model = request.form['model']
        inputs = [
            float(request.form['Temperature']),
            float(request.form['SquareFootage']),
            float(request.form['Occupancy']),
            float(request.form['HVACUsage']),
            float(request.form['LightingUsage']),
            float(request.form['RenewableEnergy']),
            int(request.form['Holiday']),
        ]

        model_path = os.path.join(MODEL_FOLDER, selected_model)
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        

        prediction = round(float(model.predict([inputs])[0]), 2)



    return render_template('index.html', models=models, prediction=prediction, selected_model=selected_model)

if __name__ == '__main__':
    app.run(debug=True)
