#!/bin/bash

DESTDIR="./sylk/types"
SRCDIR="_proto/"

# Python compilations
python3 -m grpc_tools.protoc  --pyi_out=$DESTDIR --python_out=$DESTDIR  --proto_path=$SRCDIR -I$SRCDIR _proto/google/rpc/*.proto
python3 -m grpc_tools.protoc  --pyi_out=$DESTDIR --python_out=$DESTDIR --proto_path=$SRCDIR --grpc_python_out=$DESTDIR -I$SRCDIR _proto/google/longrunning/*.proto
python3 -m grpc_tools.protoc  --pyi_out=$DESTDIR --python_out=$DESTDIR  --proto_path=$SRCDIR -I$SRCDIR _proto/sylk/io/*.proto
# Go compilations
protoc --go_out=$DESTDIR --go_opt=paths=source_relative -I$SRCDIR _proto/google/rpc/*.proto
protoc --go_out=$DESTDIR --go_opt=paths=source_relative -I$SRCDIR _proto/google/longrunning/*.proto
protoc --go_out=$DESTDIR --go_opt=paths=source_relative -I$SRCDIR _proto/sylk/io/*.proto
