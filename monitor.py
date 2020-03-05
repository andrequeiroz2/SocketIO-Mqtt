import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO, emit






app =  Flask(__name__)

app.config["MQTT_BROKER_URL"] = "localhost" 
app.config["MQTT_BROKER_PORT"] = 1883
app.config["MQTT_USERNAME"] = "AndreQueiroz"
app.config["MQTT_PASSWORD"] = ""
app.config["MQTT_KEEPALIVE"] = 5
app.config["MQTT_TLS_ENABLED"] = False

mqtt = Mqtt(app)
socketio = SocketIO(app)



@app.route("/")
def index():
    """ Display index page """
    return render_template("index.html")


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    """ Subscribe to a topic """
    
    mqtt.subscribe("testeandre/sensor")


@socketio.on('subscribe')
def handle_client_connected(json):
    """ Show when new Socket IO client registers to receive data """
    print('received json: {0}'.format(str(json)))


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    """ When MQTT data is detected, forward on to Socket IO """
    data = dict(
        topic = message.topic,
        payload = message.payload.decode(),
        qos = message.qos
    )
    print(client, data)
    socketio.emit('mqtt_message', data=data)
    

@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    """ Do some basic MQTT logging """
    print(level,buf)


if __name__=='__main__':
    #app.run(host="0.0.0.0", )
    socketio.run(app, host='0.0.0.0', port=8000, use_reloader=True, debug=True)
