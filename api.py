from flask import Flask, request
from flask import jsonify
from parseVcard import contactsDATA
import json
from pymongo import MongoClient
import pymongo
import certifi
from bson import json_util
from parseVcard import INPUT_NAME, json_text


print(INPUT_NAME)
print(json_text)
print("hei")
# print(json_text)







#mongodb+srv://vegardstamadsen:zvNcYlvVwuE1ScJv@cluster0.bomsogj.mongodb.net/test
try:
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb+srv://vegardstamadsen:zvNcYlvVwuE1ScJv@cluster0.bomsogj.mongodb.net/test", tlsCAFile=certifi.where())
    print("Connected to MongoDB")

    # Select database
    mydb = client["CloudContacts"]

    # Select collection
    mycol = mydb["Contacts"]

    # Define document to be inserted
   # mydoc = {"name": "Johnnybot", "address": "Highway 39"}

    # Insert document into collection
   # x = mycol.insert_one(mydoc)

    # Print the ObjectID of the inserted document
   # print(x.inserted_id)
  

except Exception as e:
    print(f"Could not connect to MongoDB: {e}")










'''
mongodb+srv://vegardstamadsen:zvNcYlvVwuE1ScJv@cluster0.bomsogj.mongodb.net/?retryWrites=true&w=majority
'''


app = Flask("Api")


# Simulated database
CONTACTS =[]
contactsMy = []
sampledata = json_text

# Load the JSON data from file



@app.route('/')
def hello():
    
    return 'Velkommen til vår API'
    
    



@app.route('/contacts')
def get_contacts():
    
    for contact in mycol.find():
        contactsMy.append({
            'id': str(contact['_id']),
            'name': contact['name'],
            'address': contact['address']
        })
    return {'contacts': contactsMy}  


@app.route('/contacts/<id>')
def get_contact(id):
    return CONTACTS[int(id)]

@app.route('/data')
def get_data():
    for d in contactsDATA:
        data = json.dumps(d) 
        mycol.insert_one(json.loads(data))
    return contactsDATA
    


@app.route('/contacts', methods=['POST'])
def create_contact():
    # get the contact data from the request body
    name = request.json['name']
    address = request.json['address']

    # create a new contact object
    contact = {'name': name, 'address': address}

    # insert the contact object into the MongoDB collection
    result = mycol.insert_one(contact)

    # return the ID of the newly inserted contact
    return {'id': str(result.inserted_id)}


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
