import hashlib
import json
import time
from key_manager import generate_keys


# Basic Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # Contains DID information
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

# Basic Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), data, last_block.hash)
        self.chain.append(new_block)

    def get_chain(self):
        return self.chain

# Identity Management class
class DIDManager:
    def __init__(self):
        self.blockchain = Blockchain()

    def register_identity(self, name, email):
        # Generate a public/private key pair for the DID
        private_key, public_key = generate_keys()

        identity = {
            "name": name,
            "email": email,
            "public_key": public_key.hex(),  # Store public key as hex
            "private_key": private_key.hex()  # Store private key as hex (in real case, it should be kept safe)
        }

        # Add DID to the blockchain
        self.blockchain.add_block(identity)

    def get_did(self, index):
        if index < len(self.blockchain.get_chain()):
            return self.blockchain.get_chain()[index].data
        else:
            return None

    def verify_identity(self, index, signature, message):
        # Retrieve the DID
        did = self.get_did(index)
        if did:
            public_key_bytes = bytes.fromhex(did['public_key'])
            public_key = ed25519.VerifyingKey(public_key_bytes)

            # Verify signature with the public key
            try:
                public_key.verify(signature, message.encode())
                return True
            except ed25519.BadSignatureError:
                return False
        else:
            return False

