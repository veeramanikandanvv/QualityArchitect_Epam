import os, uuid, pytest, requests

PARTS = os.getenv('INVENTREE_PARTS_PATH','/api/part/part/')
CATS = os.getenv('INVENTREE_CATEGORIES_PATH','/api/part/category/')

def p():
    x = uuid.uuid4().hex[:8]
    return {'name': f'QA Part {x}', 'IPN': f'QA-{x}'}

def test_list(client, base_url):
    r = client.get(base_url + PARTS)
    assert r.status_code == 200, r.text
    assert isinstance(r.json(), (list, dict))

def test_crud(client, base_url):
    r = client.post(base_url + PARTS, json=p())
    assert r.status_code in (200, 201), r.text
    d = r.json(); pk = d.get('pk', d.get('id')); assert pk is not None
    assert client.get(f'{base_url}{PARTS}{pk}/').status_code == 200
    assert client.patch(f'{base_url}{PARTS}{pk}/', json={'name': d['name'] + ' updated'}).status_code in (200, 202)
    assert client.delete(f'{base_url}{PARTS}{pk}/').status_code in (200, 202, 204)

def test_duplicate_ipn(client, base_url):
    x = p(); assert client.post(base_url + PARTS, json=x).status_code in (200, 201)
    assert client.post(base_url + PARTS, json=x).status_code in (400, 409)

@pytest.mark.parametrize('q', [{'limit': 1}, {'page': 1}, {'search': 'QA'}])
def test_query(client, base_url, q):
    assert client.get(base_url + PARTS, params=q).status_code == 200

def test_categories(client, base_url):
    assert client.get(base_url + CATS).status_code == 200

def test_unauthenticated(base_url):
    assert requests.get(base_url + PARTS).status_code in (401, 403)
