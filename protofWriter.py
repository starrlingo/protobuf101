from test_pb2 import Person

import sys

# destination
my_pb_file = "ppl.pb"

person = Person()
person.id = 123
person.name = "jason"
person.email = "jason@gmail.com"

with open(my_pb_file, "wb") as f:
  f.write(person.SerializeToString())
