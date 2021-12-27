# from flask import Flask, request
# from dateutil import parser
# import datetime




import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
# app = Flask(__name__)


# @app.route('/services/calculator', methods=['PUT'])
# def calculator() -> dict:
#     """Returns solved equation."""

#     operator = request.args.get('operation')
#     value_1 = int(request.args.get('a'))
#     value_2 = int(request.args.get('b'))

#     if operator == 'sum':
#         result = value_1 + value_2

#     elif operator == 'sub':
#         result = value_1 - value_2

#     elif operator == 'mul':
#         result = value_1 * value_2

#     elif operator == 'div':
#         result = value_1 / value_2

#     return {"result": result}


# @app.route('/services/date-fmt', methods=['PUT'])
# def dateCalculator():
#     """Adds time delta to provided date."""

#     current_date = parser.isoparse(request.args.get('date'))
#     delta = int(request.args.get('days'))

#     end_date = current_date + datetime.timedelta(days=delta)

#     string = str(end_date)

#     return {"date": string}


# if __name__ == '__main__':
#     app.run(debug=True)