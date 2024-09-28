from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, send, emit
import os
from encryption import encrypt_data, decrypt_data

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
socketio = SocketIO(app)

# Store rooms and the shared key for encryption
rooms = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('create_room')
def on_create():
    room = os.urandom(8).hex()
    rooms[room] = {'key': os.urandom(16)}
    join_room(room)
    emit('room_created', {'room': room})


@socketio.on('join_room')
def on_join(data):
    room = data['room']
    if room in rooms:
        join_room(room)
        emit('room_joined', {'success': True, 'room': room})
    else:
        emit('room_joined', {'success': False})

@socketio.on('sync_clipboard')
def on_sync_clipboard(data):
    room = data['room']
    clipboard_data = data['clipboard_data']
    key = rooms[room]['key']
    encrypted_data = encrypt_data(key, clipboard_data)
    emit('clipboard_synced', {'clipboard_data': encrypted_data}, room=room)

@socketio.on('decrypt_clipboard')
def on_decrypt_clipboard(data):
    room = data['room']
    encrypted_data = data['encrypted_data']
    key = rooms[room]['key']
    try:
        decrypted_data = decrypt_data(key, encrypted_data)
        emit('clipboard_decrypted', {'decrypted_data': decrypted_data})
    except:
        emit('error', {'message': 'Decryption failed'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

