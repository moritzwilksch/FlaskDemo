from flask import *

import pandas as pd
import numpy as np
import seaborn as sns
import pickle


app = Flask(__name__)
df = sns.load_dataset("tips")

# Supports GET and POST requests, default would be GET only
@app.route("/", methods=["GET", "POST"])
def hello():
    mintip = 0
    if request.method == "GET":
        # Standard display
        return render_template('test.html',  table_to_show=df.to_html(classes="table table-sm"), mintip=mintip)
    elif request.method == "POST":
        # if frontend request POSTs input value
        for key, val in request.form.items():
            # print to console
            print(f"{key}: {val}")

        # get value
        entered_mintip = request.form.get("mintip")
        if entered_mintip == "":
            # check if empty
            entered_mintip = 0

        mintip = int(entered_mintip)

        # filter df
        res = df.query("tip >= @mintip")
        # pass bootstrap class for styling
        return render_template("test.html", table_to_show=res.to_html(classes="table table-sm"), mintip=mintip)
        
@app.route("/predpage", methods=["GET", "POST"])
def predpage():
    print(f"======> {request.method}")
    if request.method == "GET":
        return render_template("predict.html")
    elif request.method == "POST":
        input_total_bill = request.form.get("input_total_bill")
        input_sex = request.form.get("input_sex")
        input_smoker = request.form.get("input_smoker")
        input_day = request.form.get("input_day")
        input_time = request.form.get("input_time")
        input_size = request.form.get("input_size")
        
        input_df = pd.DataFrame({
            "total_bill": float(input_total_bill),
            "sex": input_sex,
            "smoker": input_smoker,
            "day": input_day,
            "time": input_time,
            "size": int(input_size)
        }, index=[0])

        catcols = ["sex", "smoker", "day", "time"]
        input_df[catcols] = input_df[catcols].astype("category")
        print(input_df.info())
        print(model)
        input_df = transformer.transform(input_df)
        print(input_df)
        prediction = model.predict(input_df)

        return render_template("predict.html", predtip=prediction[0])



if __name__ == "__main__":
    app.debug = True
    with open("ML-API-Example/lmodel.pck", "rb") as f:
        model = pickle.load(f)
    with open("ML-API-Example/transformer.pck", "rb") as f:
        transformer = pickle.load(f)
    app.run()