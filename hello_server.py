import concurrent.futures

import logging
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

class Hello(helloworld_pb2_grpc.HelloServicer):
	def  SayHello(self, request, context):
		print(request.name[:-1])
		return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name[:-1], age='twenty')

def serve():

	server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
	helloworld_pb2_grpc.add_HelloServicer_to_server(Hello(), server)
	server.add_insecure_port('[::]:50055')
	server.start()
	server.wait_for_termination()

if __name__ == '__main__':
	logging.basicConfig()
	serve()
