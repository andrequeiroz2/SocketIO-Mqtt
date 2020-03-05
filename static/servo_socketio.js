$(document).ready(function () {
    

    var server_address = 'http://0.0.0.0:8000';
    var socket = io(server_address);

    socket.on('connect', function() {
        socket.emit('subscribe', { data: 'I\'m connected!' });
    });

    socket.on('mqtt_message', function(data) {
        if (data['topic'] == 'testeandre/sensor') {
            $('#servo0').text(data['payload']);
        }
    });
});





