import hashlib
import datetime
import time
import os

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def read_block_data(self, block_index):
        if block_index >= len(self.chain):
            return None
        block = self.chain[block_index]
        return block.data

# Création de notre blockchain
blockchain = Blockchain()

# Chemin vers le répertoire contenant les fichiers
directory = "C:\\Users\\Admin\\OneDrive\\Documents\\3TC\\PIR\\data"

# Taille de chaque bloc en bytes
block_size = 1024

# Chronomètre de début
start_time = time.time()

# Lecture des fichiers et ajout dans la blockchain
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        with open(file_path, "rb") as file:
            file_data = file.read(block_size)
            while file_data:
                block = Block(file_data, "")
                blockchain.add_block(block)
                file_data = file.read(block_size)

# Chronomètre de fin
end_time = time.time()

# Affichage
print("Nombre de blocs dans la blockchain:", len(blockchain.chain))
print("Temps d'exécution:", end_time - start_time, "secondes")

# Lecture du contenu des blocs
for i, block in enumerate(blockchain.chain):
    print("Contenu du bloc", i, ":", blockchain.read_block_data(i))
