import json


# Settings
INPUT_NAME = 'sample.vcf'
OUTPUT_NAME = 'export.json'


# Read vCard file
with open(INPUT_NAME, 'r') as f:
    text = f.read()
    


# Split into lists
contact_texts = text.split('END:VCARD\nBEGIN:VCARD')

# Fix first and last contact_text
contact_texts[0] = contact_texts[0].replace('BEGIN:VCARD\n', '')
contact_texts[-1] = contact_texts[-1].replace('END:VCARD\n', '')


# Key lookup table
def fix_key(key):
    '''Receive a string. E.g. : "EMAIL;TYPE=INTERNET"
    Get whichever is before the first semi-colon (if any): "EMAIL"
    Use lookup-table (dict) to return it's value: "email
    If key not in table, simply return key"
    '''

    key_main = key.split(';')[0]
    return {
        'BDAY': 'birthday',
        'VERSION': 'version',
        'N': 'name',
        'FN': 'first name',
        'ORG': 'organisation',
        'ADR': 'address',
        'TEL': 'telefon',
        'EMAIL': 'email'
    }.get(key_main, key)


# Make dicts
contactsDATA = []
for contact_text in contact_texts:
    # Create new, empty contact, and split the text into lines.
    contact = {}
    lines = contact_text.split('\n')

    for line in lines:
        
        # Skip this iteration if the line is empty.
        if len(line) < 1:
            continue

        # Fix colon-values
        key, *value = line.split(':')
        value = ':'.join(value)

        # Update/fix key
        key = fix_key(key)

        # Add key-value-pair to the contact dictionary, and add to contact list.
        contact[key] = value
    contactsDATA.append(contact)


# Create JSON
json_text = json.dumps(contactsDATA, indent=2)


# Write JSON to file
with open(OUTPUT_NAME, 'w') as f:
    
    print(json_text)
    
