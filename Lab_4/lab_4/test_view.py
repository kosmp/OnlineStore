from django.urls import reverse 
import pytest
import requests
import django.test.client
import pytest
import django.test.utils
from django.conf import settings


def test_home_page(): # Get the home page 
    url = 'http://127.0.0.1:8000/'
    response = requests.get(url)
    assert response.status_code == 200


def test_detail_page(): # Get the home page 
    url = 'http://127.0.0.1:8000/2'
    response = requests.get(url)
    assert response.status_code == 200

def test_developing_page(): # Get the home page 
    url = 'http://127.0.0.1:8000/Developing'
    response = requests.get(url)
    assert response.status_code == 200

def test_1():
    url = 'http://127.0.0.1:8000/?sort=ascending'
    response = requests.get(url)
    assert response.status_code == 200

def test_2():
    url = 'http://127.0.0.1:8000/?sort=descending'
    response = requests.get(url)
    assert response.status_code == 200

def test_3():
    url = 'http://127.0.0.1:8000/Developing/?sort=descending'
    response = requests.get(url)
    assert response.status_code == 200

def test_4():
    url = 'http://127.0.0.1:8000/Developing/?sort=ascending'
    response = requests.get(url)
    assert response.status_code == 200

def test_7():
    url = 'http://127.0.0.1:8000/cart/'
    response = requests.get(url)
    assert response.status_code == 403

def test_8():
    url = 'http://127.0.0.1:8000/order/create/'
    response = requests.get(url)
    assert response.status_code == 403

def test_9():
    url = 'http://127.0.0.1:8000/statistic/'
    response = requests.get(url)
    assert response.status_code == 403

def test_10():
    url = 'http://127.0.0.1:8000/statistic/tables/2/'
    response = requests.get(url)
    assert response.status_code == 403

def test_11():
    url = 'http://127.0.0.1:8000/statistic/tables/'
    response = requests.get(url)
    assert response.status_code == 403

def test_12():
    url = 'http://127.0.0.1:8000/statistic/tables/3/'
    response = requests.get(url)
    assert response.status_code == 403
