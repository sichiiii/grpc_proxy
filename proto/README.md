Python from protoc directly
```shell
~/Code/protoc/bin/protoc -I=. --python_out=./ --grpc_python_out=. ./proto/ucsmodel.proto
```

As python plugin
```shell
python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./proto/ucsmodel.proto
```

C#
```shell
/home/alexey/Code/protoc/bin/protoc -I=. --csharp_out=./proto/ ./proto/ucsmodel.proto --grpc_out=./proto/ --plugin=protoc-gen-grpc=/home/alexey/Code/protoc/bin/grpc_csharp_plugin
```

JavaScript+TypeScript- messages only (browser client can't call grpc)
```shell
sudo protoc --plugin="protoc-gen-ts=./node_modules/.bin/protoc-gen-ts" --js_out="import_style=commonjs,binary:./" --ts_out="service=grpc-web:./" ./static/proto/ucsmodel.proto
```

```shell
/home/alexey/Code/protoc/bin/protoc --plugin="protoc-gen-ts=./node_modules/.bin/protoc-gen-ts" --js_out="import_style=commonjs,binary:./" --ts_out="service=grpc-web:./" ./static/proto/ucsmodel.proto
```