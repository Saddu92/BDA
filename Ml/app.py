from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("admission_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Get form data
            gre = float(request.form['GRE'])
            toefl = float(request.form['TOEFL'])
            uni_rating = float(request.form['UniversityRating'])
            sop = float(request.form['SOP'])
            lor = float(request.form['LOR'])
            cgpa = float(request.form['CGPA'])
            research = float(request.form['Research'])

            # Prepare input for model
            user_input = np.array([[gre, toefl, uni_rating, sop, lor, cgpa, research]])
            
            # Predict
            pred = model.predict(user_input)[0]
            prediction = round(pred * 100, 2)  # convert to percentage
        except:
            prediction = "Invalid input. Please enter numeric values."
    
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
