import os

url = 'https://api.openai.com/v1/chat/completions'
auth = os.environ.get('KEY')

headers = {
    'Content-Type': 'application/json',
    'Authorization': auth
}