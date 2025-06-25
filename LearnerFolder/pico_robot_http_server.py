import network
import socket
import machine
import time
import ure  # lightweight regex

from machine import Pin, PWM

# ---- Configuration ----
SSID = "your_wifi_name"
PASSWORD = "your_wifi_password"
STATIC_IP = "192.168.1.10"
SUBNET_MASK = "255.255.255.0"
GATEWAY = "192.168.1.1"
DNS = "192.168.1.1"
PORT = 12345

# Motor pins (front left and right)
LEFT1 = PWM(Pin(14))
LEFT2 = PWM(Pin(15))
RIGHT1 = PWM(Pin(16))
RIGHT2 = PWM(Pin(17))
for m in (LEFT1, LEFT2, RIGHT1, RIGHT2):
    m.freq(1000)

# Optional: rear motor control
REAR_LEFT1 = PWM(Pin(12))
REAR_RIGHT1 = PWM(Pin(13))
REAR_LEFT1.freq(1000)
REAR_RIGHT1.freq(1000)
enable_rear_motors = True  # Set False to disable rear wheels

def set_all_pwm(l1, l2, r1, r2):
    LEFT1.duty_u16(l1)
    LEFT2.duty_u16(l2)
    RIGHT1.duty_u16(r1)
    RIGHT2.duty_u16(r2)
    if enable_rear_motors:
        REAR_LEFT1.duty_u16(l1 if l1 > 0 else l2)
        REAR_RIGHT1.duty_u16(r1 if r1 > 0 else r2)

# ---- Wi-Fi Setup ----
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.ifconfig((STATIC_IP, SUBNET_MASK, GATEWAY, DNS))
wlan.connect(SSID, PASSWORD)

print("Connecting to Wi-Fi...")
while not wlan.isconnected():
    time.sleep(1)
print("Connected:", wlan.ifconfig())

# ---- Web Server ----
addr = socket.getaddrinfo(STATIC_IP, PORT)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Listening on http://{}:{}".format(STATIC_IP, PORT))

def stop_all():
    set_all_pwm(0, 0, 0, 0)

def handle_command(cmd, speed):
    duty = int(speed / 100 * 65535)
    if cmd == "F":
        set_all_pwm(duty, 0, duty, 0)
    elif cmd == "B":
        set_all_pwm(0, duty, 0, duty)
    elif cmd == "L":
        set_all_pwm(0, 0, duty, 0)  # spin right wheels forward
    elif cmd == "R":
        set_all_pwm(duty, 0, 0, 0)  # spin left wheels forward
    elif cmd == "S":
        stop_all()

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode("utf-8")
    print("Request:", request)

    match = ure.search("GET /send\?msg=([A-Z]),(\d+)", request)
    if match:
        cmd = match.group(1)
        speed = int(match.group(2))
        print("Parsed:", cmd, speed)
        handle_command(cmd, speed)
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nOK"
    else:
        response = "HTTP/1.1 400 Bad Request\r\nContent-Type: text/plain\r\n\r\nInvalid"

    conn.send(response)
    conn.close()
'''

your previously listed instructions still apply:

✅ You can run your index.html GUI from your Mac over Wi-Fi and access it on your iPhone via Safari.

✅ Your Pico W HTTP server will receive commands like F,80 via fetch().

Here’s a fully clarified guide including the final step: how to “Add to Home Screen” on your iPhone.

🪛 Step-by-step Instructions

On your Mac:
Save the updated HTML as index.html.
Open Terminal and navigate to the folder:
cd /path/to/index.html
Start the local web server:
python3 -m http.server 8000
Find your Mac's IP address:
In Terminal:

ipconfig getifaddr en0
Example: 192.168.1.20

On your iPhone:
Connect to the same Wi-Fi network as your Mac.
Open Safari.
Go to:
http://192.168.1.20:8000
(Replace with your actual Mac IP address.)
Your robot controller GUI should appear.

To Add to Home Screen:
Tap the Share icon at the bottom of Safari (looks like a square with an arrow pointing up).
Scroll down in the menu and tap “Add to Home Screen.”
Optionally rename it (e.g., “Robot Controller”).
Tap “Add” in the top-right corner.
Now the GUI appears as a standalone app icon on your iPhone’s home screen!

✅ From then on, you can launch it like any app and use it to control your Pico robot.

Would you like a custom app icon to show on the Home Screen too? I can help with that'''