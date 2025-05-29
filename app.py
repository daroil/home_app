# app.py
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Pi server is running."

@app.route('/run-script')
def run_script():
    subprocess.run(['python3', 'your_script.py'])
    return "Script executed."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
