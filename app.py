from flask import *

import pandas as pd
import numpy as np
import seaborn as sns


app = Flask(__name__)
df = sns.load_dataset("tips")

# Supports GET and POST requests, default would be GET only
@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        # Standard display
        return render_template('test.html',  table_to_show=df.to_html())
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
        return render_template("test.html", table_to_show=res.to_html(classes="table table-sm"))
        
if __name__ == "__main__":
    app.debug = True
    app.run()