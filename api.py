from flask import Flask, request
from parseVcard import contacts
import json
from pymongo import MongoClient
import pymongo

print("hei")
# print(json_text)



myclient = pymongo.MongoClient("mongodb+srv://vegardstamadsen:zvNcYlvVwuE1ScJv@cluster0.bomsogj.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]







'''
mongodb+srv://vegardstamadsen:zvNcYlvVwuE1ScJv@cluster0.bomsogj.mongodb.net/?retryWrites=true&w=majority
'''


app = Flask("Api")


# Simulated database
CONTACTS =[{"name": "Paul", "address": "road_66", "telefon": "1234"}, {"name": "Mary"}, {"name": "John"}]




@app.route('/')
def hello():
    return 'Hello! hei!!'



@app.route('/contacts')
def get_contacts():
    return CONTACTS


@app.route('/contacts/<id>')
def get_contact(id):
    return CONTACTS[int(id)]


@app.route('/contacts', methods=['POST'])
def update_contact():
    name = request.json['name']
    address = request.json['address']
    contact = {"name": name, "address": address}
    
    CONTACTS.append(contact)
    CONTACTS.append(address)
    

    id = len(CONTACTS) - 1
    return {'id': id}


@app.route('/contacts/<id>', methods=['DELETE'])
def delete_contact(id):
    del CONTACTS[int(id)]
    return  {'id': id}


# This starts the application (if you run the script instead of launging flask
# from the command line).
if __name__ == '__main__':
    '''The variable __name__ is set to the name/title of the script. If this is
    equal to '__main__', then that means this program is run directly (from the
    start button or the command line). If not, it probably means that the script
    was imported as a module and not as a script. I.e. the code in this if does
    not run if the file is imported as a module.'''

    app.run()
