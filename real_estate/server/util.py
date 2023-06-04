import json
import pickle
import numpy as np

__data_columns = None
__locations = None
__model = None


def get_estimated_price(location, sqft, bath, bedroom):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    z = np.zeros(len(__data_columns))
    z[0] = sqft
    z[1] = bath
    z[2] = bedroom
    if loc_index >= 0:
        z[loc_index] = 1

    return round(__model.predict([z])[0], 2)


def get_location_names():
    return __locations


def load_artifacts():
    print('Loadind Started')

    global __data_columns
    global __locations

    with open ('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    global __model
    with open ('./artifacts/Real_Estate_Price_Prediction.pickle', 'rb') as f:
        __model = pickle.load(f) 
    print('Loading...done')


if __name__ == '__main__':
    load_artifacts()
    print(get_location_names())
    print(get_estimated_price('jalahalli', 1500, 2, 2))