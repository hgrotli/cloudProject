import certifi
import pymongo
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
    mydoc = {"name": "John", "address": "Highway 37"}

    # Insert document into collection
    x = mycol.insert_one(mydoc)

    # Print the ObjectID of the inserted document
    print(x.inserted_id)

except Exception as e:
    print(f"Could not connect to MongoDB: {e}")




