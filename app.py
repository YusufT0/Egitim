from flask import Flask
from flask import request, render_template
import pred
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods= ['POST'])
def predict():
    features = request.form.to_dict()
    final_features =  pred.preprocces(features)
    prediction = model.predict(final_features)

    output = round(prediction[0], 2) * 1000

    return render_template('index.html', prediction_text = f"Tahmin edilen araç Fiyatı: {output}")

if __name__ == "main":
    app.run(debug=True)
