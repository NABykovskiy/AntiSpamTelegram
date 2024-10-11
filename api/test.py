import requests
from datetime import datetime

url = 'http://localhost:8082/'

item = {'chat_id': 1, 'title': 'test', 'added_date': datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}


res1 = requests.post(url + 'database/new_chat', json=item)
print(res1.text)