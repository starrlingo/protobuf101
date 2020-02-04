import test_pb2
import sys

my_pb_file = "ppl.pb"

person = test_pb2.Person()

with open(my_pb_file, "rb") as f:
  person.ParseFromString(f.read())

print('id: {id}, name: {name}, email: {email} '.format(
    id=person.id, name=person.name, email=person.email))
