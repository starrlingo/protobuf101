import test_pb2
import sys
import json
from google.protobuf import json_format

my_pb_file = "ppl.pb"

person = test_pb2.Person()

with open(my_pb_file, "rb") as f:
  person.ParseFromString(f.read())

print('id: {id}, name: {name}, email: {email} '.format(
    id=person.id, name=person.name, email=person.email))

# Covert to JSON string
person_obj = json_format.MessageToDict(person)
print('Convert to JSON string: {}'.format(json.dumps(person_obj)))
