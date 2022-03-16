# ReadMe

### Required python packages:

1. pandas

2. numpy

3. keras

4. tenSorFlow

5. flask 


### Required files:

1. The historical data: Helsinki-Day-data.csv

2. The OSM dictionary: OSMs_dictionary.csv

3. The Model: Model.h5

4. The path to save the predictions: preds.csv


### To get the prediction:

- Replace the paths according to your directories:

- new_value: is the new noise value comming from the sensor.

- OSM_id: is the OSM id of the road segment.

python Day_predictions.py --data_path=Helsinki-Day-data.csv --new_value=75 --OSM_id=900490572  --d_path=OSMs_dictionary.csv --model_path=Model.h5 --pred_path=preds.csv


### To run the Urban Noise Prediction API:
-Run Python noise.py
-Go to http://127.0.0.1:5000/noise/%NewValue%/%Osm_Id% and replace %NewValue% with your prediction new value and %Osm_Id% with your Osm_Id

- 
