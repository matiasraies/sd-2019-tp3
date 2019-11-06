$(document).ready(function () {

  var chatHistory = $('.chat-history');
  var button = $('#submitMsg');
  var textarea = $('#message-to-send');
  var chatHistoryList = chatHistory.find('ul');
  var button1 = $('#submitUser');
  var button2 = $('#logoutUser');

  var username = $('#username');
  var peopleView = $('.people-list');
  var peopleViewList = peopleView.find('ul');
  var mostrarMsg = true;
  var countLineas = 0;

  button.on('click', addMessage.bind(this));
  button1.on('click', addUser.bind(this));
  button2.on('click', removeUser.bind(this));
  textarea.on('keyup', addMessageEnter.bind(this));

  /* 
   * Si ya existe una cookie.
   * Si existe una sesion no dejamos que agrege otro usuario.
   */
  if (checkCookie('session')) {
    document.getElementById("username").disabled = true;
    document.getElementById("submitUser").disabled = true;
    document.getElementById("logoutUser").disabled = false;
    document.getElementById("submitMsg").disabled = false;
    document.getElementById("message-to-send").disabled = false;
  }

  /*
   * Renderiza el template de mensaje con los datos del mensaje y lo agrega a la lista
   * de mensajes enviados.
   */
  function renderMsg(from_to, name, time, messageToSend) {
    scrollToBottom();

    var cookie = getCookie('session');
    var idUser = cookie.split("-")[0];

    if (messageToSend !== '') {
      if (idUser === from_to) {
        var template = Handlebars.compile($("#message-template").html());
      }
      else {
        var template = Handlebars.compile($("#message-response-template").html());
      }

      var context = {
        name: name,
        message: messageToSend,
        time: time
      };

      chatHistoryList.append(template(context));
      scrollToBottom();

      setTimeout(function () {
        scrollToBottom();
      }.bind(this), 1500);
    }
  }

  /*
   * Renderiza el template de user con los datos del usuario y lo agrega a la lista
   * de usuarios conectados.
   */
  function renderUser(idUser, nick) {
    var template = Handlebars.compile($("#user-template").html());

    var context = {
      ID: idUser,
      nick: nick,
    };
    peopleViewList.append(template(context));
  }

  /*
   * Elimina un user nuevo en el servidor y altera los elementos del chat.
   */
  function removeUser() {
    document.getElementById("username").disabled = false;
    document.getElementById("submitUser").disabled = false;
    document.getElementById("logoutUser").disabled = true;
    document.getElementById("submitMsg").disabled = true;
    document.getElementById("message-to-send").disabled = true;
    document.getElementById("username").focus();

    var cookie = getCookie('session');
    var idUser = cookie.split("-")[0];

    $.ajax({
      type: "GET",
      url: "/chat/cgi-bin/users.py",
      data: "user=" + idUser + "&op=1",
      success: function (data) {
        eliminarCookie('session', '/chat/');
      }
    });
  }

  /*
   * Agrega un user nuevo en el servidor y altera los elementos del chat.
   */
  function addUser() {
    document.getElementById("username").disabled = true;
    document.getElementById("submitUser").disabled = true;
    document.getElementById("logoutUser").disabled = false;
    document.getElementById("submitMsg").disabled = false;
    document.getElementById("message-to-send").disabled = false;
    document.getElementById("message-to-send").focus();

    $.ajax({
      type: "GET",
      url: "/chat/cgi-bin/users.py",
      data: "user=" + username.val() + "&op=0"
    });
  }

  /*
   * Obtiene los valores de la cookie de session para enviar mensajes al servidor.
   */
  function addMessage() {
    var cookie = getCookie('session');
    var idUser = cookie.split("-")[0];
    var nickuser = cookie.split("-")[1];

    sendMessage(idUser, nickuser);
  }

  /*
   * Enviar mensajes al servidor.
   */
  function sendMessage(idUser, nickuser) {
    $.ajax({
      type: "GET",
      url: "/chat/cgi-bin/message.py",
      data: "idUser=" + idUser + "&message=" + textarea.val() + "&nick=" + nickuser + "&hora=" + getCurrentTime() + "&op=0",
      success: function (data) {
        textarea.val('');
      }
    });
  }

  /*
   * Evento keyCode 13 para enviar mensajes al servidor.
   */
  function addMessageEnter(event) {
    if (event.keyCode == 13) {
      addMessage();
    }
  }

  /*
   * Mantiene el cursor en las ultimas lineas de chat.
   */
  function scrollToBottom() {
    chatHistory.scrollTop(chatHistory[0].scrollHeight);
  }

  /*
   * Obtiene la fecha actual.
   */
  function getCurrentTime() {
    return new Date().toLocaleTimeString().
      replace(/([\d]+:[\d]{2})(:[\d]{2})(.*)/, "$1$3");
  }

  /*
   * Obtiene la cookie con el nombre pasado por parametros.
   */
  function getCookie(name) {
    var pairs = document.cookie.split("; "),
      count = pairs.length, parts;

    while (count--) {
      parts = pairs[count].split("=");
      if (parts[0] === name)
        return parts[1];
    }
    return null;
  }

  /*
   * Verifica si existe un valor para el usuario, de existir devuelve true.
   */
  function checkCookie(value) {
    var cookie = getCookie(value);

    if (cookie == null)
      return false;

    var user = cookie.split("-")[1];

    if (user != null) {
      getUser(user);
      return true;
    }
    return false;
  }

  /*
   * Busca al usuario en la cookie y le da la bienvenida.
   */
  function getUser(value) {
    var cookie = getCookie('session');
    var user = cookie.split("-")[1];
    alert("Bienvenido " + user);
  }

  /*
   * Eliminar Cookie. Setea la propiedad de la cookie expires en una fecha
   * antigua.
   */
  var eliminarCookie = function (key, path) {
    if (getCookie(key)) {
      document.cookie = key + "="
        + ((path == null) ? "" : ";path=" + path)
        + ";expires=Thu,01-Jan-70 00:00:01 GMT";
    }
  }

  /*
   * Evento de tiempo para actualizar los mensajes enviados en el chat.
   */
  setInterval(function () {

    if (getCookie('session') != null) {
      $.ajax({
        type: "GET",
        url: "/chat/cgi-bin/message.py?lineas=" + countLineas + "&op=1",
        dataType: "json",
        success: function (dat) {
          var cookie = getCookie('cantMsg');
          var cantMsg = cookie;

          countLineas = parseInt(cantMsg); /* Lineas nuevas */
          if (mostrarMsg) {
            if (dat != ' ') {
              for (d in dat) {
                renderMsg(dat[d][0], dat[d][2], dat[d][1], dat[d][3])
              }
            }
          }
          else {
            countLineas = 0;
          }
        }
      });
    }
  }, 1000);

  /*
   * Evento de tiempo para actualizar usuarios conectados en el chat.
   */
  setInterval(function () {
    peopleViewList.empty();

    $.ajax({
      type: "GET",
      url: "/chat/cgi-bin/users.py",
      data: "op=2",
      success: function (data) {
        if (data == '') {
          mostrarMsg = false;
          countLineas = 0;
        }
        else {
          mostrarMsg = true;
          for (d in data) {
            renderUser(data[d][0], data[d][1])
          }
        }
      }
    });
  }, 5000);

});