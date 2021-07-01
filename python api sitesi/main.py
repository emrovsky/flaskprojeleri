import json
import random
from flask import Flask
app = Flask(__name__)



@app.route("/")
def giris():
    sayı = random.randrange(1,10)
    MyList = ["Kucuk su birikintisine ne denir? Sucuk!", "Bi adam laptop almis dellenmis", "Hic bozuk paran var mi? yok cunku hepsini tamir ettim", "ineklerin sevmedigi element? az-ot", "En kasli ilyas kimdir? casillas", "Adama evlimisiniz diye sormuslar, hayir arsaliyim demi", "Bu gece seni kiniyorum , cunku kina gecesi", "Adamin kafasi atmis bacaklari esek.", "Yagmur yagmis, kar peynir!", "Gulen ordege ne denir? kikirdak"]
    a = MyList[sayı]
    data = {}
    data['all'] = []
    data['all'].append({
        'statusCode': '200',
    })
    data['all'].append({
        'espri': a,
    })
    return data




app.run()