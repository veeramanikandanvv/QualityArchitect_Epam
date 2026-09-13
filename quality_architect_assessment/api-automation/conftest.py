import os, pytest, requests

@pytest.fixture(scope='session')
def base_url():
    return os.getenv('INVENTREE_URL','http://localhost:8000').rstrip('/')

@pytest.fixture(scope='session')
def client(base_url):
    s = requests.Session()
    token = os.getenv('INVENTREE_TOKEN')
    if token:
        s.headers['Authorization'] = f'Token {token}'
    s.headers['Accept'] = 'application/json'
    return s
