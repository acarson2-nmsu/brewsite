from app.brewsite import app

def test_client():
    client = app.test_client() #Function of the flask applicaiton

    responce = client.get('/')

    assert responce.status_code == 200 #Everything loaded correctly
    assert b'Confucius' in responce.data
    assert b'James Smith' in responce.data
        