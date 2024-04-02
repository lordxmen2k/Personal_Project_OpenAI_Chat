import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from openai_chat import ChatApp  # Make sure openai_chat.py uses the updated ChatApp class


app = Flask(__name__)
socketio = SocketIO(app)

# Create an instance of ChatApp without the api_key parameter
chat_app = ChatApp()

@app.route('/')
def index():
    return render_template('index.html')  # Ensure the 'templates/index.html' exists


@socketio.on('message')
def handle_message(data):
    user_message = data['message']
    print(user_message)

    if (user_message.strip() != ""):
        chat_response = chat_app.send_message(user_message)
        emit('response', {'message': chat_response})

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)