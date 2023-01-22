REDIS_CHANNEL: str = 'channel:1'

HTML = """
<!DOCTYPE html>
<html>
    <head>
        <title>WS</title>
    </head>
    <body>
        <h1>USE DEVTOOLS</h1>

        <div>
            var ws = new WebSocket("ws://localhost:8000/ws");<br>
            ws.onmessage = function(event) {    <br>
                var messages = document.getElementById('messages')<br>
                var message = document.createElement('li')<br>
                var content = document.createTextNode(event.data)<br>
                message.appendChild(content)<br>
                messages.appendChild(message)<br>
            };<br>
            function sendMessage(event) {<br>
                var input = document.getElementById("messageText")<br>
                ws.send(input.value)<br>
                input.value = ''<br>
                event.preventDefault()<br>
            }<br>
        </div>

        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
        </script>

    </body>
</html>
"""
