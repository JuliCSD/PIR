import ipfsApi
import multiprocessing
import time
import os

def noeudadd(port, queue):
    api = ipfsApi.Client('127.0.0.1', port)
    res = api.add('test.txt')
    file = open("preuveAdd.txt", 'x')
    file.write(api.id()['Addresses'][1])
    file.write(" \n a ajouté le fichier hash : ")
    file.write(res['Hash'])
    print("J'ai add : ", res)
    queue.put_nowait(res['Hash'])

def noeudcat(port, queue):
    api = ipfsApi.Client('127.0.0.3', port)
    time.sleep(2)
    hash = queue.get()
    t1 = time.process_time_ns()
    content = api.cat(hash)
    t2 = time.process_time_ns()
    print("temps = ", t2 - t1)
    print(content)
    file = open("preuveCat.txt", 'x')
    file.write(api.id()['Addresses'][0])
    file.write(" \n a récupéré le fichier hash : ")
    file.write(hash)

if __name__ == "__main__":
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=noeudadd, args=(5001, queue,))
    p2 = multiprocessing.Process(target=noeudcat, args=(5003, queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
