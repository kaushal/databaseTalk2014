from flask import Flask, render_template, request
import random
import pymongo

client = pymongo.MongoClient()

db = client.gerlandas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process')
def process():
    amount = random.choice(range(3, 800))
    prodId = random.choice(range(3000, 80000))
    order  = request.args['order']

    dbEntry = {'amount': amount, 'prodId': prodId, 'order': order}

    db.gerlandas.insert(dbEntry)

    return render_template('thanks.html', amount=amount, order=order)

@app.route('/history')
def history():
    return str([entry for entry in db.gerlandas.find()])

if __name__ == '__main__':
    app.run(debug=True)
