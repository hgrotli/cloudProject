import json
with open('sample.vcf', 'r') as f:
    text = f.read()
    pretty_data = json.dumps(text, indent=4)
    print(pretty_data)




print("hello")


from flask import Flask

CONTACTS = [{"name": "Paul"}, {"name": "Mary"}, {"name": "John"}]


app = Flask(__name__)


@app.route('/')
def example_function():
    return 'Hello Flask!!'

@app.route('/contacts')
def get_contacts():
    return CONTACTS



if __name__ == '__main__':
    app.run()

