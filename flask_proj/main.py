from flask import Flask, request
from functions.analizer import analize_func
from datetime import timedelta
import datetime
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/services/calculator/", methods=['POST'])
def calculator_service():
    request_data = request.get_json()
    value1 = int(request_data["a"])
    value2 = int(request_data["b"])
    op_type = request_data["op_type"]

    operation_resul = analize_func({"a": value1, "b": value2, "op_type": op_type})
    
    return {"result": f'{operation_resul}'}


@app.route("/services/date-fmt/", methods=['POST'])
def date_service():
    """Take a date and a number of days and return the date with them"""
    request_data = request.get_json()
    date_time_obj = datetime.datetime.strptime(request_data["date"], "%Y-%m-%dT%H:%M:%S")
    days_inp = request_data["days"]
    date_outp = date_time_obj + timedelta(days=days_inp)

    return {"date": date_outp.isoformat()}




if __name__ == '__main__':
    app.run(debug=True)