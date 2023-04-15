from flask import Flask, render_template, request
import json
from pymongo import MongoClient
import certifi

app = Flask(__name__)

# MongoDB configuration
client = MongoClient('mongodb+srv://vegardstamadsen:zvNcYlvVwuE1ScJv@cluster0.bomsogj.mongodb.net/test', tlsCAFile=certifi.where())
db = client['CloudContacts']
collection = db['Contacts']

# Vcard parsing function
def parse_vcard(vcard):
    contacts = []
    vcard_list = vcard.split('\nEND:VCARD\n')
    for vcard_item in vcard_list:
        if vcard_item:
            vcard_item = vcard_item.replace('\n ', '')
            contact = {}
            vcard_item_list = vcard_item.split('\n')
            for item in vcard_item_list:
                if item:
                    key, value = item.split(':', 1)
                    contact[key] = value
            contacts.append(contact)
    return contacts

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    vcard = file.read().decode('utf-8')
    contacts = parse_vcard(vcard)
    collection.insert_many(contacts)
    print(contacts)
    return 'File uploaded successfully'
    

if __name__ == '__main__':
    app.run(debug=True)