from app import app
import sys, os
import pandas as pd
import numpy as np

CSV_DATA_PATH = 'CSV'
def read_csv(file_name):
    """
    Returns dataframe from requested CSV
    """
    file_path = os.path.join(CSV_DATA_PATH, file_name+'.csv')
    return pd.read_csv(file_path)

def list_all_room_names(category, room_keys = ['ROOMID','NAME']):
    """
    Returns a list of dictionaries filtered by room category.
    Each dictionary has the room ID and the name
    """
    df = read_csv('rooms')
    # filter by category and keep only ID and name
    df = df[df['CATEGORY']==category][room_keys]
    list_rooms = []
    for idx, info in df.iterrows():
        room_dict = {}
        for key in room_keys:
            room_dict[key] = str(info[key])
            if key in ['CAPACITY','ROOMAREA']:
                # hackhackhack: round floats to integers then convert to string
                room_dict[key]= str(round(info[key])).split('.')[0]
                if room_dict.get('ROOMAREA') == '-1':
                    room_dict['ROOMAREA'] = 'N/A'
        list_rooms.append(room_dict)
    return list_rooms
