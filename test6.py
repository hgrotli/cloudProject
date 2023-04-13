import pymongo

# Replace the placeholders with your database information
connection_string = "mongodb+srv://vegardstamadsen:zvNcYlvVwuE1ScJv@cluster0.bomsogj.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)

# Replace <database-name> and <collection-name> with your actual database and collection names
db = client.<database-name>
collection = db.<collection-name>

# Example query
query = {"name": "John Doe"}
results = collection.find(query)

for result in results:
    print(result)

    