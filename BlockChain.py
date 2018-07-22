import hashlib as hasher
import datetime as dt

class Block:
    def __init__(self , index , timestamp , data , old_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.old_hash = old_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        hash_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.old_hash)
        hash_string_2 = hash_string.encode('utf-8')
        sha.update(hash_string_2)
        return sha.hexdigest()

def create_genesis_block():
    return Block(0 , dt.datetime.now() , "Block 1" ,"0")

def next_block(last_block):
    this_index = last_block.index + 1;
    this_timestamp = dt.datetime.now()
    this_data = "Block" + str(this_index)
    this_hash = last_block.hash
    return Block(this_index , this_timestamp , this_data , this_hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

number_of_blocks = 5

for i in range(0, number_of_blocks):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    print ("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print ("Hash: {}\n".format(block_to_add.hash)) 