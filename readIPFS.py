import ipfsApi
hash_nose = 'QmWRE2rsvCr7XRWjZrN81wYLwoV6ei6SLLtjzu2PNWNoDX'
api = ipfsApi.Client('127.0.0.1', 5001)
res= api.cat(hash_nose)

# lst = [1, 77, 'lol']
# print(api.add_pyobj(lst))
