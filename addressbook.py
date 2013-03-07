#!/usr/bin/python
import json

file = open('addressbook.json')
json_object = file.read()
address_book = json.loads(json_object)

for entity in address_book:
    if ('lastName' in entity and 'firstName' in entity and
        entity['lastName'] and entity['firstName']):
        print '{last_name}, {first_name}'.format(
                last_name=entity['lastName'], 
                first_name=entity['firstName'])
    elif 'household' in entity and entity['household']:
        print entity['household']

    for address in entity['addresses']:
        print '{}'.format(address['address1'])
        if 'address2' in address.keys() and address['address2']:
            print '{}'.format(address['address2'])
        print '{city}, {state}  {zip}\n'.format(
                city=address['city'],
                state=address['state'],
                zip=address['postalCode'])




