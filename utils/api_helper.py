import requests
import configparser

from utils.logger import Logger

# Load base URL from config
config = configparser.ConfigParser()
config.read('config/config.ini')
BASE_URL = config['API']['base_url']
API_KEY = config['API']['api_key']

base_url_jph = config['API']['base_url_jph']

logger = Logger.get_logger()

def get(endpoint, params=None):
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "x-api-key": "reqres-free-v1"
    }

    logger.info(f"GET Request: {url} | Params: {params}")
    response = requests.get(url, params=params , headers=headers)
    logger.info(f"Response: {response.status_code} | Body: {response.text}")
    return response

def get_post(endpoint, params=None):
    url_jph = f"{base_url_jph}{endpoint}"
    logger.info(f"GET Request: {url_jph} | Params: {params}")
    response = requests.get(url_jph, params=params)
    logger.info(f"Response: {response.status_code} | Body: {response.text}")
    return response

def post(endpoint, json=None):
    headers = {
        "x-api-key": "reqres-free-v1"
    }
    return requests.post(f"{BASE_URL}{endpoint}", json=json, headers=headers)

def update(endpoint, json=None):
    headers = {
        "x-api-key": "reqres-free-v1"
    }
    return requests.put(f"{BASE_URL}{endpoint}", json=json, headers=headers)

def update_jph(endpoint, json=None):

    return requests.put(f"{base_url_jph}{endpoint}", json=json)