# app.py
from flask import Flask, render_template, request, redirect, url_for
import subprocess
from output import Command
import socket
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led', methods=['GET'])
def led():
    return render_template('led.html')


@app.route('/rainbow', methods=['GET'])
def rainbow():
    send_color_command(1,1,1,1,0,0)
    return "Rainbow send", 200

def send_color_command(red, green, blue, mod, len, time):
    cmd = Command()
    cmd.red = red
    cmd.green = green
    cmd.blue = blue
    cmd.mod = mod  # You can adjust this as needed
    cmd.len = len  # Example value
    cmd.time = time  # Example value in milliseconds

    udp_data = cmd.to_struct()

    UDP_IP = "192.168.0.116"  # Or the target IP
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(udp_data, (UDP_IP, UDP_PORT))
@app.route('/send_color', methods=['POST'])
def send_color():
    data = request.get_json()

    red = int(data.get('red', 0))
    green = int(data.get('green', 0))
    blue = int(data.get('blue', 0))

    send_color_command(red, green, blue, 0, 0, 0)

    return "Color sent via UDP", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
