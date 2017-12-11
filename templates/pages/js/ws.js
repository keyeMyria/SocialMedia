var socket = new WebSocket('ws://' + window.location.host + '/ws/')

socket.onopen = function open() {
   document.write('WebSockets connection created.');
};


socket.onmessage = function message(event) {
  var data = JSON.parse(event.data);
  document.write(data);
  // NOTE: We escape JavaScript to prevent XSS attacks.
  //var username = encodeURI(data['username']);
 // var user = $('li').filter(function () {
   // return $(this).data('username') == username;
 // });

  //if (data['is_logged_in']) {
   // user.html(username + ': Online');
  //}
  //else {
   // user.html(username + ': Offline');
  //}
};

if (socket.readyState == WebSocket.OPEN) {
  socket.onopen();
}
