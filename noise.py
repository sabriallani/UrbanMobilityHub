import sys
import argparse
import pandas as pd
import numpy as np
import json
from json import JSONEncoder
from keras.models import load_model
from flask import Flask
from flask import request, jsonify
app = Flask(__name__)




def prepare_data(Osm_id, new_value, data, d):
    data.loc[-1] = [Osm_id, new_value]  # adding a row
    data.index = data.index + 1  # shifting index
    data = data.sort_index()
    New_data = data.copy()
    New_data = New_data[New_data['OSM_id'] == Osm_id]
    new_osm = d[d['OSM_id'] == Osm_id].iloc[0, 0]
    New_data['OSM_id'] = new_osm
    return New_data.iloc[-6:]


# Function that returns the next 6 noise prediction values:
def Future_Preditcion(new_value, Osm_id):
    # Read the historical data:
    data = pd.read_csv('Helsinki-Day-data.csv')
    # Upload the dictionary:
    d = pd.read_csv('OSMs_dictionary.csv')
    dictionary = {}
    for k in range(len(d)):
        dictionary.update({d.iloc[k, 1]: d.iloc[k, 0]})

    # Upload the model:
    model = load_model('Model.h5')

    New_data = prepare_data(Osm_id, new_value, data, d)
    New_data = New_data.values.reshape(-1, 2)
    pred = model.predict([New_data[:, 1].reshape(1, -1).astype(np.float32), New_data[:, 0].reshape(1, -1).astype(int)])
    #print('\n\nNext 6 noise predictions values: ', pred.tostring())
    return pred


@app.route('/noise/<int:newvalue>/<int:osm>')
def noise(newvalue,osm):
    return 'Next noise values %s!' % Future_Preditcion(newvalue, osm)


@app.route('/')
def all1():
  #jsonStr = json.dumps(Future_Preditcion(75, 900490572))
  #print(jsonStr)

  pred = Future_Preditcion(75, 900490572)

  return 'Next noise values %s!' % pred


if __name__ == '__main__':
    app.run(debug=True)
