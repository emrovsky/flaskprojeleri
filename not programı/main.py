import random
from flask import Flask, render_template, url_for
import time
from flask_minify import minify, decorators
app = Flask(__name__, static_url_path='/static')
time.sleep(2)
notdefteri = input("Ne kaydetmek istersin?  ")
a = random.randint(100000,999999)
print("Notunuz kaydedildi ! http://127.0.0.1:5000/"+str(a))
@app.route("/"+str(a))
@decorators.minify(html=True, js=True, cssless=True)
def hello():
    return '<body style="background-color:#ffffa1;color:#3eb593;">'+"------------------------------------------------------------------------------------------------------------------------- Python Günlükleri Not Defteri---------------------------------------------------------------------------------------------------------------------------" + "\n" +notdefteri 


@app.route("/")
@decorators.minify(html=True, js=True, cssless=True)
def deneme():
    return 'Basit bir Not Defteri Uygulaması Youtube : https://www.youtube.com/channel/UC_q6e2_Um5qiRZZTqY1JgbQ' 

if __name__ == '__main__':
    app.run()

