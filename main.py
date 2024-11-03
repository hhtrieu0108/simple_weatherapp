#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, render_template, request
from weather import query_api
import json

with open("./place.json", "r", encoding="utf-8") as file:
    place_data = json.load(file)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=place_data
    )
@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
        data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)
if __name__=='__main__':
    app.run(debug=True)
