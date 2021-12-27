from datetime import timedelta, date

import dateutil.parser as parser


op_input = {"date":"2020-01-01T00:00:00", "days": 20}

date_inp = parser.parse(op_input["date"])
days_inp = op_input["days"]
date_outp = date_inp+ timedelta(days=days_inp)
"""Adds time delta to provided date."""
print(Date_req)

