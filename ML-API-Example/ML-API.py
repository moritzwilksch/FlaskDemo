from flask import *
app = Flask(__name__)


@app.route("/api", methods=["POST"])
def getsquare():
    request_json = request.get_json()
    print(f"REQUEST JSON = {request_json}")
    return {"square_of_input_num": int(request_json["inputnum"])**2}



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")