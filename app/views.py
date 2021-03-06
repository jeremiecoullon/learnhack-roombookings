from flask import json
from app import app
from models import list_all_room_names, read_csv


"----------------------------------------------------------------------------------------------------"

@app.route('/')
def home():
    return 'hello!'

@app.route('/list_rooms')
def list_rooms():
    # le_json = json.dumps({'home':'hello'})
    room_keys = ['ROOMID','NAME']
    return json.dumps(list_all_room_names(category='CLU', room_keys=room_keys))


@app.route('/room_info')
def room_info():
    room_keys = ['ROOMID','NAME', 'CAPACITY', 'ROOMAREA']
    list_rooms = list_all_room_names(category='CLU', room_keys=room_keys)
    # selected_room = [elem for elem in list_rooms if elem['ROOMID']==str(id)]
    return json.dumps(list_rooms)


@app.errorhandler(404)
def not_found_error(error):
    return '404'

@app.errorhandler(500)
def internal_error(error):
    return '500'

"----------------------------------------------------------------------------------------------------"
