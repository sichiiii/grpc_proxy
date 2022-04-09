import concurrent.futures
import sys
import logging
import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import configparser

class Hello(helloworld_pb2_grpc.HelloServicer):
	def  SayHello(self, request, context):
		with grpc.insecure_channel('localhost:50055') as channel:
			stub = helloworld_pb2_grpc.HelloStub(channel)
			response = stub.SayHello(helloworld_pb2.HelloRequest(name=request.name))
		print(response)
		kwargs = dict(arg.split('=') for arg in sys.argv[1:])
		configfile_path = '/home/jabka/python/grpc_proxy/grpc/config.ini'
		config = configparser.ConfigParser()
		config.read(configfile_path)
		delete_params = list(config['delete'])
		for i in delete_params:
			setattr(response, i, '')

		return helloworld_pb2.HelloReply(message='Hello, %s!' % str(response), age=str(response))

def serve():

	server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
	helloworld_pb2_grpc.add_HelloServicer_to_server(Hello(), server)
	server.add_insecure_port('[::]:50050')
	server.start()
	server.wait_for_termination()

if __name__ == '__main__':
	logging.basicConfig()
	serve()
