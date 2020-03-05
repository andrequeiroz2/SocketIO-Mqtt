=========List Port==============
sudo lsof -i -P -n | grep LISTEN
netstat -lntu
================================


=========Kill Port==============
sudo kill -9 `sudo lsof -t -i:9001`
================================


=========Broker Start===========
mosquitto -v
================================


=========Broker Stop============
sudo service mosquitto stop
sudo systemctl stop mosquitto.service
================================


=========Client Publish=========
mosquitto_pub -h localhost -m "test msg" -t test/test -d
================================


=========Client Subscrib========
mosquitto_sub -h localhost -m "test msg" -t test/test
================================


