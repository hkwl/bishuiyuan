#! /usr/bin/python
# enconding:utf-8

import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('templates/index.html')


@socketio.on('my event', namespace='/demo')
def handle_my_custom_event(message):
    print 'receive'
    emit('connect', {'num': 5, 'kind': 'apple', 'message': message['data']})

@socketio.on('my event',namespace='/demo')
def show_data_event():
    while True:
        tds = random.randint(0,100)
        water = random.randint(0,100)
        create_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        socketio.emit("my response",{'tds':tds,'water':water,'create_time':create_time})
        time.sleep(5)

if __name__ == '__main__':
    socketio.run(app,host='127.0.0.1',port=50001,debug=True)
