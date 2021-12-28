import json


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    #expected = {'hello': 'world'}
    #assert expected == json.loads(res.get_data(as_text=True))

def test_mode(app, client):
    res = client.post('/mode',data=dict(
        type="2"
    ))
    assert res.status_code in (200,202)
    #expected = {"status": "success", "data": {"task_id": "abcdefg"}}
    #assert expected == json.loads(res.get_data(as_text=True))
