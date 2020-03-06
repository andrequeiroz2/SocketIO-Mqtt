# SocketIO-Mqtt
Flask + Mqtt + SocketIO

$ source env/bin/activate

pip install -r requirements.txt

#install broker:(mosquito)

#run broker    :(mosquitto -v)

run app Flask

$ python monitor.py

run client_pub Mqtt
mosquitto_pub -h localhost -m "Hello" -t testeandre/sensor -d

#Browser (http://0.0.0.0:8000/)
