# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_render_template]

from flask import Flask, render_template, request, g
import json
import os
import flask_sijax
# from generatepngs import *

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app = Flask(__name__)
app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)
# g.sijax.register_callback('function_name', function_name)

@flask_sijax.route(app, '/')
def mainPage():
    # Every Sijax handler function (like this one) receives at least
    # one parameter automatically, much like Python passes `self`
    # to object methods.
    # The `obj_response` parameter is the function's way of talking
    # back to the browser
    def get_attention(obj_response,param):

        fin = open("data.txt")
        attention_level = 0
        for each_line in fin:
            attention_level = int(each_line.rstrip())

        obj_response.html('#currentAttentionPercentage', str(attention_level)+"%")
        obj_response.html('#numericalhidden', attention_level)

    def get_relaxation(obj_response,param):
        myrelaxfile = open("relax.txt")
        relax_level = 0
        for each_line in myrelaxfile:
            relax_level = int(each_line.rstrip())

        obj_response.html('#currentRelaxationPercentage', str(relax_level)+"%")
        obj_response.html('#numericalhiddenRelaxation', relax_level)

    if g.sijax.is_sijax_request:
        # Sijax request detected - let Sijax handle it
        g.sijax.register_callback('get_attention', get_attention)
        g.sijax.register_callback('get_relaxation', get_relaxation)

        return g.sijax.process_request()

    # Regular (non-Sijax request) - render the page template
    return render_template('index.html')

# def function_name(obj_response, arg1, arg2, arg3):
#     obj_response.alert('You called the function successfully!')

@flask_sijax.route(app, '/hello')
def hello():
    # Every Sijax handler function (like this one) receives at least
    # one parameter automatically, much like Python passes `self`
    # to object methods.
    # The `obj_response` parameter is the function's way of talking
    # back to the browser
    def say_hi(obj_response,param):

        fin = open("data.txt")
        attention_level = 0
        for each_line in fin:
            attention_level = int(each_line.rstrip())

        obj_response.html('#currentAttentionPercentage', str(attention_level)+"%")


    if g.sijax.is_sijax_request:
        # Sijax request detected - let Sijax handle it
        g.sijax.register_callback('say_hi', say_hi)
        return g.sijax.process_request()

    # Regular (non-Sijax request) - render the page template
    return render_template('run.html')

# def function_name(obj_response, arg1, arg2, arg3):
#     obj_response.alert('You called the function successfully!')


# @app.route('/cloudtest')
# def ooga():
#     make_png('test')
#     return 'uploaded to cloud!'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]
