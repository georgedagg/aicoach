from flask import Flask, render_template, request, session
import json
import login
import requests
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        print('Error:', e)

@app.route('/begin', methods=['GET','POST'])
def begin():
    if request.method == 'POST':
        try:
            print('Ajax query successful')
            user_begin ='You are an AI endurance expert. Introduce yourself and ask if your client is ready to begin.'
            session['conversation'] = [{'role': 'system', 'content': user_begin}]
            payload = {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "system", "content": user_begin}],
                "temperature": 0.4
            }
            response = requests.post(login.url, headers=login.headers, data=json.dumps(payload))
            response_json = response.json()
            content = response_json['choices'][0]['message']['content']
            conversation = session.get('conversation', [])
            conversation.append({'role':'assistant', 'content': content})
            session['conversation'] = conversation
            print('\nResponse received: ', content)
            print('\nSession History:', session)
            print('\nConversation:', conversation)
            return json.loads(response.content)
        except Exception as e:
            print('Error:', e)

@app.route('/process', methods=['GET','POST'])
def process():
    if request.method == 'POST':
        try:
            print('Ajax query successful')
            user_string = request.form['data']
            print('User response:', user_string)
            conversation = session.get('conversation', [])
            conversation.append({'role': 'user', 'content': user_string})
            try:
                payload = {
                    "model": "gpt-3.5-turbo",
                    "messages": conversation,
                    "temperature": 0.4
                }
                response = requests.post(login.url, headers=login.headers, data=json.dumps(payload))
            except Exception as e:
                print('Error in request', e)
            response_json = response.json()
            content = response_json['choices'][0]['message']['content']
            conversation.append({'role': 'assistant', 'content': content})
            session['conversation'] = conversation
            print('\nResponse received: ', content)
            print('\nSession:', session)
            print('\nConversation:', conversation)
            return json.loads(response.content)
        except Exception as e:
            print('Error:', e)

