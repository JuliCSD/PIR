import ipfsApi
import time

api = ipfsApi.Client('127.0.0.1', 5001)
res = api.add('hello')
res
api.cat(res['Hash'])

# while True:
# 	time.sleep(5)
# 	print("A")
