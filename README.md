# protobuf101
A hello world project for protobuf writer and reader

## How to compile the protobuf file to a python parser
Install protobuf compiler
```
git clone https://github.com/google/protobuf.git
cd protobuf
./autogen.sh
./configure
make
# Check the protoc and its version
which protoc
protoc --version
```
Compile .proto to xxx_pb2.py
```
# This will generate the test_pb2.py parser file
protoc -I=`pwd` --python_out=`pwd` `pwd`/test.proto
```


## Running writer and reader example
Installation
```
pip install -r requirements.txt
```

Writer
```
python protofWriter.py
```
Reader
```
python protofReader.py
```
