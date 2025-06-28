# Владислав Козловский, 31-я когорта — Финальный проект. Инженер по тестированию плюс
import pytest
import sender_stand_request as sender
import data

# Функция создания заказа
def create_new_order():
    response = sender.create_order(data.order_data)
    assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
    
    track = response.json().get("track")
    assert track is not None, "В ответе отсутствует номер трека"
    return track

# Позитивная проверка получения заказа по треку
def positive_assert_get_order(track):
    response = sender.get_order_by_track(track)
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    
    order = response.json().get("order")
    assert order is not None, "В ответе отсутствуют данные заказа"
    assert order["track"] == track, "Номер трека в ответе не совпадает с ожидаемым"

# Основной автотест — создать заказ и получить его по треку
def test_create_order_and_get_by_track():
    track = create_new_order()
    positive_assert_get_order(track)