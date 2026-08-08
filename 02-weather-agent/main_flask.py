from flask import Flask, render_template, request, redirect, url_for, session
from flask_agent import agent
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    if 'thread_id' not in session:
        session['thread_id'] = str(uuid.uuid4())
    if 'messages' not in session:
        session['messages'] = []
    print('home', session)
    return render_template('chat.html', messages=session['messages'])

@app.route('/send', methods=['POST'])
def send():
    user_message = request.form['message']

    user_lat = request.form.get('latitude')
    user_lon = request.form.get('longitude')

    print("LAT:", user_lat)
    print("LON:", user_lon)

    if user_lat and user_lon:
        session['user_location'] = {
            'lat': user_lat,
            'lon': user_lon
        }

    print("SESSION:", session)

    response = agent.invoke(
        {
            "messages": [
                {
                    'role': 'user',
                    'content': user_message
                }
            ]
        },
        {
            "configurable": {
                "thread_id": session['thread_id']
            }
        }
    )

    session['messages'].append({
        'type': 'human',
        'content': user_message
    })

    content = response['messages'][-1].content

    session['messages'].append({
        'type': 'ai',
        'content': content[0]['text']
    })

    session.modified = True

    print("FINAL SESSION:", session)

    return redirect(url_for('home'))

@app.route('/clear')
def clear():
    session.clear()
    return redirect(url_for('home'))

app.run(debug=True)