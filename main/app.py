from flask import Flask, render_template
from flask_socketio import SocketIO
from api import Monitor

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def root():
    return render_template("index.html")

# hosts/topics to listen
monitors = [
    Monitor("192.168.98.10", "vanetza/in/spatem"),     # rsu (SPATEM)
    Monitor("192.168.98.10", "in/frames"),             # rsu (Camera)   
    Monitor("192.168.98.10", "in/detections"),         # rsu (Yolo)
    Monitor("192.168.98.20", "in/coord"),              # obu
    Monitor("192.168.98.30", "in/coord")               # obu 2
]

@socketio.on('connect')
def start():
    print('Client connected.')
    print('Starting monitors...')
    for monitor in monitors:
        monitor.on_message = lambda topic, msg: socketio.emit(topic, msg)
        monitor.start()
        print(f"{monitor.topic} monitor: OK!")
    socketio.emit('connect', {'data': 'Connected to monitors'})

@socketio.on('disconnect')
def end():
    print('Disonnected')
    socketio.emit('disconnect', {'data': 'Disconnected'})

if __name__ == '__main__':
    socketio.run(app, debug=True)