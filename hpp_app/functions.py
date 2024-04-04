import json
import pickle
import numpy as np
import pandas as pd
import config

def get_column_names():
    with open(config.MUMBAI_COLUMN_NAMES_PATH, 'r') as col:
        column_dict = json.load(col)
    return column_dict["columns"]

column_list = get_column_names()

def get_location_names():
    return column_list[16:]

def get_predicted_price(*args):
    with open(config.MODEL_FILE_PATH, 'rb') as f:
        model = pickle.load(f)
    x_test_array = np.zeros(len(column_list))
    for i in range(1,17):
        x_test_array[i] = args[i]

    loc_index = column_list.index(args[0])
    x_test_array[loc_index] = 1
    x_test = pd.DataFrame([x_test_array], columns=column_list)

    price = model.predict(x_test)
    return price[0]