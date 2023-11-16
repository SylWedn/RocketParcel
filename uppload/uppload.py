# Simple HTTP Server Example
# Control Relays and read End Switches using a web browser

import time
import network
import socket
import urequests
from machine import Pin

# Define the pins for the Relays and end switches
relay1 = Pin(15, Pin.OUT)
relay2 = Pin(14, Pin.OUT)
relay3 = Pin(13, Pin.OUT)
relay4 = Pin(12, Pin.OUT)
relay5 = Pin(5, Pin.OUT)

relayState1 = 'Relay 1 State Unknown'
relayState2 = 'Relay 2 State Unknown'
relayState3 = 'Relay 3 State Unknown'
relayState4 = 'Relay 4 State Unknown'
relayState5 = 'Relay 5 State Unknown'

end_switch1 = Pin(16, Pin.IN, Pin.PULL_UP)
end_switch2 = Pin(2, Pin.IN, Pin.PULL_UP)
end_switch3 = Pin(4, Pin.IN, Pin.PULL_UP)
end_switch4 = Pin(0, Pin.IN, Pin.PULL_UP)
end_switch5 = Pin(17, Pin.IN, Pin.PULL_UP)

# Initialize re_status with all relays and end switches OFF (0)
re_status = '0000000000'

def update_re_status():
    global re_status
    re_status = (
        str(relay1.value()) +
        str(relay2.value()) +
        str(relay3.value()) +
        str(relay4.value()) +
        str(relay5.value()) +
        str(end_switch1.value()) +
        str(end_switch2.value()) +
        str(end_switch3.value()) +
        str(end_switch4.value()) +
        str(end_switch5.value())
    )

# Update re_status initially
update_re_status()

ssid = 'WIFI SSID'  # write your wifi ssid
password = 'WIFI PASSWORD' # write password here

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

html = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>
  html {
    font-family: Helvetica;
    display: inline-block;
    margin: 0px auto;
    text-align: center;
  }
  .buttonGreen {
    background-color: #4CAF50;
    border: 2px solid #000000;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
  }
  .buttonRed {
    background-color: #D11D53;
    border: 2px solid #000000;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
  }
  .state {
    font-size: 20px;
  }
</style>
</head>
<body>
  <center><h1>Control Panel</h1></center><br><br>
  <form><center>
    <center>
      <button class="buttonGreen" name="relay1" value="on" type="submit">Relay 1 ON</button>
      <button class="buttonRed" name="relay1" value="off" type="submit">Relay 1 OFF</button>
    </center>
    <br><br>
    <center>
      <button class="buttonGreen" name="relay2" value="on" type="submit">Relay 2 ON</button>
      <button class="buttonRed" name="relay2" value="off" type="submit">Relay 2 OFF</button>
    </center>
    <br><br>
    <center>
      <button class="buttonGreen" name="relay3" value="on" type="submit">Relay 3 ON</button>
      <button class="buttonRed" name="relay3" value="off" type="submit">Relay 3 OFF</button>
    </center>
    <br><br>
    <center>
      <button class="buttonGreen" name="relay4" value="on" type="submit">Relay 4 ON</button>
      <button class="buttonRed" name="relay4" value="off" type="submit">Relay 4 OFF</button>
    </center>
    <br><br>
    <center>
      <button class="buttonGreen" name="relay5" value="on" type="submit">Relay 5 ON</button>
      <button class="buttonRed" name="relay5" value="off" type="submit">Relay 5 OFF</button>
    </center>
    <center>
    <button class="buttonGreen" name="send_status" type="submit">Send Status</button>
</center>
  </form>
  <br><br>
  <div class="state">
    %s
  </div>
</body>
</html>
"""

# Define the target URL
url = 'http://192.168.31.57:8000/dev_in/'

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 83)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)


# Store the last time re_status was sent
last_status_update = time.time()


# Listen for connections, serve client
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print("request:")
        print(request)
        request = str(request)
        relay1_on = request.find('relay1=on')
        relay1_off = request.find('relay1=off')
        relay2_on = request.find('relay2=on')
        relay2_off = request.find('relay2=off')
        relay3_on = request.find('relay3=on')
        relay3_off = request.find('relay3=off')
        relay4_on = request.find('relay4=on')
        relay4_off = request.find('relay4=off')
        relay5_on = request.find('relay5=on')
        relay5_off = request.find('relay5=off')
        send_status = request.find('send_status=on')  # Added line to check for 'send_status'

        print('relay1 on = ' + str(relay1_on))
        print('relay1 off = ' + str(relay1_off))
        print('relay2 on = ' + str(relay2_on))
        print('relay2 off = ' + str(relay2_off))
        print('relay3 on = ' + str(relay3_on))
        print('relay3 off = ' + str(relay3_off))
        print('relay4 on = ' + str(relay4_on))
        print('relay4 off = ' + str(relay4_off))
        print('relay5 on = ' + str(relay5_on))
        print('relay5 off = ' + str(relay5_off))
        print('send_status = ' + str(send_status))  # Added line to print send_status

        if relay1_on != -1:
            print("relay1 on")
            relay1.value(1)
        if relay1_off != -1:
            print("relay1 off")
            relay1.value(0)
        if relay2_on != -1:
            print("relay2 on")
            relay2.value(1)
        if relay2_off != -1:
            print("relay2 off")
            relay2.value(0)
        if relay3_on != -1:
            print("relay3 on")
            relay3.value(1)
        if relay3_off != -1:
            print("relay3 off")
            relay3.value(0)
        if relay4_on != -1:
            print("relay4 on")
            relay4.value(1)
        if relay4_off != -1:
            print("relay4 off")
            relay4.value(0)
        if relay5_on != -1:
            print("relay5 on")
            relay5.value(1)
        if relay5_off != -1:
            print("relay5 off")
            relay5.value(0)

        # Send re_status to the specified URL when send_status is pressed
        if send_status != -1:
            urequests.post(url + re_status)  # Use the specified URL and add re_status

        # Update the re_status variable
        update_re_status()

        # Create and send response
        stateis = "Relay/End Switch Status: %s" % re_status
        response = html % stateis
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
    except OSError as e:
        cl.close()
        print('connection closed')
