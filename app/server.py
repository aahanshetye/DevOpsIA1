from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask on macOS!"
