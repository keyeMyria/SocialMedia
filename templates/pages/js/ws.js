var socket = new WebSocket('ws://' + window.location.host + '/ws/');

socket.onopen = function open() {
  return 1;
};


socket.onmessage = function message(event) {
  var data = JSON.parse(event.data);


};

if (socket.readyState == WebSocket.OPEN) {
  socket.onopen();
}
