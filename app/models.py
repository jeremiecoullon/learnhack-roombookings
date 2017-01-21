from app import app, db
import sys, os
from config import CSV_DATA_PATH
import pandas as pd


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
            room_dict[key] = info[key]
        list_rooms.append(room_dict)
    return list_rooms
