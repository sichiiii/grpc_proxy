from __future__ import print_function
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

def run():
	with grpc.insecure_channel('localhost:50050') as channel:
		stub = helloworld_pb2_grpc.HelloStub(channel)
		response = stub.SayHello(helloworld_pb2.HelloRequest(name='cyberjabka'))
	print("Hello server: " + response.message)

if __name__ == '__main__':
	logging.basicConfig()
	run()

