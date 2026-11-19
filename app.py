from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("kidney_model.pkl","rb"))
scaler = pickle.load(open("kidney_scaler.pkl","rb"))
pca = pickle.load(open("pca.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    features = np.array([[
    float(data["age"]),
    float(data["bp"]),
    float(data["sg"]),
    float(data["al"]),
    float(data["su"]),
    float(data["rbc"]),
    float(data["pc"]),
    float(data["pcc"]),
    float(data["ba"]),
    float(data["bgr"]),
    float(data["bu"]),
    float(data["sc"]),
    float(data["sod"]),
    float(data["pot"]),
    float(data["hemo"]),
    float(data["pcv"]),
    float(data["wc"]),
    float(data["rc"]),
    float(data["htn"]),
    float(data["dm"]),
    float(data["cad"]),
    float(data["appet"]),
    float(data["pe"]),
    float(data["ane"])
    ]])

    scaled = scaler.transform(features)

    pca_data = pca.transform(scaled)

    prediction = model.predict(pca_data)

    if prediction[0] == 0:
        result = "⚠ Patient is likely suffering from Chronic Kidney Disease"
    else:
        result = "✅ Patient is NOT suffering from Chronic Kidney Disease"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)