from flask import Flask
import random
app=Flask(__name__)
@app.route("/")
def home():
  return f"Temp:{random.randint(20,30)}C"
app.run(host="0.0.0.0",port=5000)