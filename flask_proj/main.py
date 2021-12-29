from werkzeug.exceptions import HTTPException
from flask import Flask, request
from functions.analizer import analize_func
from datetime import timedelta
from flask import jsonify
from werkzeug.wrappers.response import Response
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/services/calculator/", methods=['POST'])
def calculator_service():
    """
    Take a json input with 3 values:
    arg1, agr2 and operation_type
    then return the result in a json format"""
    request_data = request.get_json()
    value1 = int(request_data["arg1"])
    value2 = int(request_data["arg2"])
    op_type = request_data["op_type"]
    try:
        operation_resul = analize_func({"a": value1, "b": value2, "op_type": op_type})
    except:
        return Response("Bad input", 422)
    response = jsonify({"resul": f'{operation_resul}'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/services/date-fmt/", methods=['POST'])
def date_service():
    """Take a date isoformat
    and a number of days and return 
    the date with them"""

    request_data = request.get_json()

    date_time_obj = datetime.datetime.strptime(request_data["date"], "%Y-%m-%dT%H:%M:%S")
    days_inp = request_data["days"]
    date_outp = date_time_obj + timedelta(days=days_inp)

    return {"date": date_outp.isoformat()}




if __name__ == '__main__':
    app.run(debug=True)