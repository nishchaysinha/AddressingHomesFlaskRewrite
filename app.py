import json
import flask
from flask import request, url_for, render_template, redirect

import communicator

app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def my_maps():

  mapbox_access_token = 'pk.eyJ1IjoibmlzaGNoYXlzaW5oYSIsImEiOiJjazhiaDdsMGcwOHNkM2Rvd3NyejNqcXI3In0.CDBnWKxSzYRiXgbOZWp8Ew'

  return render_template('index.html',mapbox_access_token=mapbox_access_token)

@app.route('/revg/<string:latlng>',methods=['POST'])
def revg(latlng):
    latlng=json.loads(latlng)
    print({latlng['lat']})
    print({latlng['lng']})
    communicator.passing(str(latlng['lat']), str(latlng['lng']))
    return '200'


if __name__ == '__main__':
    app.run(debug=True)