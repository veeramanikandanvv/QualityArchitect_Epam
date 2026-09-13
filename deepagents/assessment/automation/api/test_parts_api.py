import os
import requests


def test_list_parts(api_base_url, api_token):
    headers = {"Authorization": f"Token {api_token}"} if api_token else {}
    response = requests.get(f"{api_base_url.rstrip('/')}/part/part/", headers=headers, timeout=15)
    assert response.status_code == 200, response.text
    assert isinstance(response.json(), (dict, list))
