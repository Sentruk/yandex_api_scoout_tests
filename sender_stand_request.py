import requests
from config import URL_SERVICE, CREATE_ORDER_PATH, ORDER_TRACK_PATH

def create_order(data):
    url = URL_SERVICE + CREATE_ORDER_PATH
    return requests.post(url, json=data)

def get_order_by_track(track):
    url = URL_SERVICE + ORDER_TRACK_PATH
    params = {"t": track}
    return requests.get(url, params=params)