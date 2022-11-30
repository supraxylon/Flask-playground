import sys
import math
import os
import random
from datetime import date
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from jinja2 import Environment
import jinja2
from markupsafe import escape
from flask import Flask, request, jsonify, render_template, make_response
import hashlib
import csv
from cardinfobuilder import getCard

app = Flask(__name__)

key = str(hashlib.sha256(str(date.today()).encode('utf-8')).hexdigest())
randomnumber = 0

#numberOfCards = getCard(0).length

def csvToList(filename):
    listout = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            listout.append(row)
    return listout


cardInfo = csvToList(r'C:\Users\magna\Documents\projects\flaskapiproject\data\testdata2.csv')
print(cardInfo[0][0][0])

@app.route('/')
def landingPage():
    randomnumber = random.randrange(0,100)
    return render_template('index.html', number=randomnumber) #'<h1>Hello! your lucky number is ' + str(randomnumber) + '!</h1>'

@app.route('/hello' , methods=['GET', 'POST'])
def hello():
    return render_template('hello.html', name=os.name)

@app.route('/reading' , methods=['GET', 'POST'])
def reading():
    print('Produced todays key of: ' + key)
    print(request.form)
    if request.method == 'GET':
        return '<h1>Try returning to the main page and filling out the form</h1>'
    if request.method == 'POST':
        form_data = request.form
        key_offset = str(hashlib.sha256(str(form_data['Field1_name']).encode('utf-8')).hexdigest())
        print(str(form_data) + key_offset)
        cardNums = []
        cardNames = []
        cardText = []
        cardImgs = []
        align = []
        numberOfCards = getCard(0).length
        random.seed(key_offset + key)
        print(int(form_data['Field3_name']))
        deck = []
        for i in range(0, numberOfCards):
            deck.append(i)
        for i in range(0, int(form_data['Field3_name'])):
            num = random.randrange(0,numberOfCards)
            num = deck.pop(num)
            numberOfCards -= 1
            cardNums.append(num)
            cardNames.append(getCard(num).name)
            cardText.append(getCard(num).description)
            cardImgs.append(getCard(num).link)
            align.append(i % 2)
        print(cardNums)
        return render_template('reading.html', form_data=form_data, key=key, numCards=int(form_data['Field3_name']),Question=form_data['Field1_name'],cardNames=cardNames,cardText=cardText,cardImgs=cardImgs, align=align)

if __name__ == '__main__':
    app.run(debug=True)
    print('Hello there! todays key is ' + str(key))

@app.route('/post', methods=["GET","POST"])
def testpost():
    input_json = request.get_json(force=True)
    dictToReturn = {'text':input_json['text']}
    return jsonify(dictToReturn)