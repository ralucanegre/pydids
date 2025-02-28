import unittest
import json
from time import time
from key_manager import generate_keys
from did_manager import Blockchain, Block, DIDManager


class TestDIDManager(unittest.TestCase):
    
    def setUp(self):
        # Set up the DIDManager and the blockchain before each test
        self.did_manager = DIDManager()
    
    def test_key_generation(self):
        # Test key generation using Ed25519
        private_key, public_key = generate_keys()

        # Verify that private and public keys are not None
        self.assertIsNotNone(private_key)
        self.assertIsNotNone(public_key)
        
        # Check that keys are valid by creating a SigningKey and VerifyingKey
        try:
            signing_key = ed25519.SigningKey(private_key)
            verifying_key = ed25519.VerifyingKey(public_key)
            self.assertIsInstance(signing_key, ed25519.SigningKey)
            self.assertIsInstance(verifying_key, ed25519.VerifyingKey)
        except Exception as e:
            self.fail(f"Key generation failed: {str(e)}")
    
    def test_register_identity(self):
        # Register an identity and check if it's correctly added to the blockchain
        self.did_manager.register_identity("Bob", "bob@example.com")

        # Retrieve DID from the blockchain
        did = self.did_manager.get_did(1)
        self.assertIsNotNone(did)
        self.assertEqual(did['name'], "Bob")
        self.assertEqual(did['email'], "bob@example.com")
        
        # Verify public key is in correct format
        self.assertTrue(len(did['public_key']) > 0)
        self.assertTrue(len(did['private_key']) > 0)

    def test_signature_verification(self):
        # Register an identity and get private/public keys
        self.did_manager.register_identity("Charlie", "charlie@example.com")
        did_data = self.did_manager.get_did(1)

        # Retrieve the private key and sign a message
        private_key_bytes = bytes.fromhex(did_data['private_key'])
        private_key = ed25519.SigningKey(private_key_bytes)
        message = "This is a message to sign"
        signature = private_key.sign(message.encode())

        # Verify the signature using the DID public key
        is_valid = self.did_manager.verify_identity(1, signature, message)
        self.assertTrue(is_valid)

    def test_invalid_signature(self):
        # Register an identity and get private/public keys
        self.did_manager.register_identity("Dave", "dave@example.com")
        did_data = self.did_manager.get_did(1)

        # Sign a message with the private key
        private_key_bytes = bytes.fromhex(did_data['private_key'])
        private_key = ed25519.SigningKey(private_key_bytes)
        message = "This is a message to sign"
        signature = private_key.sign(message.encode())

        # Try verifying with a different message (should fail)
        invalid_message = "This is an invalid message"
        is_valid = self.did_manager.verify_identity(1, signature, invalid_message)
        self.assertFalse(is_valid)

    def test_blockchain_integrity(self):
        # Register an identity and check blockchain integrity
        self.did_manager.register_identity("Eve", "eve@example.com")
        
        # Ensure that the blockchain has one more block than the genesis block
        self.assertEqual(len(self.did_manager.blockchain.get_chain()), 2)
        
        # Check if the last block is a valid block
        last_block = self.did_manager.blockchain.get_chain()[-1]
        self.assertEqual(last_block.index, 1)
        self.assertEqual(last_block.timestamp, last_block.timestamp)  # Just ensure timestamp exists
        self.assertIsInstance(last_block.hash, str)  # Ensure block hash is a string
        self.assertNotEqual(last_block.hash, last_block.previous_hash)  # Ensure hash is not the same as the previous block's hash

    def test_empty_chain(self):
        # Check the chain before registering any identities
        self.assertEqual(len(self.did_manager.blockchain.get_chain()), 1)
        genesis_block = self.did_manager.blockchain.get_chain()[0]
        self.assertEqual(genesis_block.data, "Genesis Block")

if __name__ == "__main__":
    unittest.main()
