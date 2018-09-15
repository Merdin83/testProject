import hashlib
import json
from time import time


<<<<<<< HEAD
#source: https://hackernoon.com/learn-blockchains-by-building-one-117428612f46  #Test2
=======
#source: https://hackernoon.com/learn-blockchains-by-building-one-117428612f46              # Test 3   # Test 4
>>>>>>> 00b1bc960e2802c3f09b09fdacb8f946b8e5cd4d
class Blockchain(object):
    
    def __init__(self):
        self.chain = []
        self.current_transaction = []
    
        #Create the genesis Block
        self.new_block(previous_hash=1, proof=100)
        
        
    #-------------------------------------------------------------------------#
    def new_block(self, proof, previous_hash=None):
        
        """
        Create a new Block in the Blockchain
        
        :param proof: <int> The proof given by the Prof of Work algorithm
        :param revious_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        
        #Reset the current list of transactions
        self.current_transaction = []
        
        self.chain.append(block)
        return block

    #-------------------------------------------------------------------------#
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        
        :param sender: <str> Adress of the Sender
        :param recipient: <str> Adress of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        
        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        
        return self.last_block['index'] + 1
        
    #-------------------------------------------------------------------------#
        
    @property
    def last_block(self):
        return self.chain[-1]
        
        
 
    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        
        :param block: <dic> Block
        :return: <str>
        """
    
        # We must make sure that the Dictionary is Ordered, or we'll have invonsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    #-------------------------------------------------------------------------#
    def prof_of_work(self, last_proof):
        """
        Simple Proof Of Work Algorithm:
        - Find a number p' such that hash(pp') contains leading 4 zeros, where p is the previous p'
        - p is the previous proof, and p' is the new proof
        
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
    
        return proof
        
    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof) contain 4 leading zeros?
        
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    #-------------------------------------------------------------------------#
    
