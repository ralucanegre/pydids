from did_manager import DIDManager


# Example Usage
if __name__ == '__main__':
    # Initialize DID manager
    did_manager = DIDManager()

    # Register an identity
    did_manager.register_identity("Alice", "alice@example.com")

    # Retrieve and print the DID from the blockchain
    did = did_manager.get_did(1)
    print(f"DID for Alice: {json.dumps(did, indent=2)}")

    # Assume Alice signed a message (using her private key)
    did_data = did_manager.get_did(1)
    private_key_bytes = bytes.fromhex(did_data['private_key'])
    private_key = ed25519.SigningKey(private_key_bytes)

    # Alice signs the message
    message = "This is a test message"
    signature = private_key.sign(message.encode())

    # Verify the identity by checking the signature
    is_valid = did_manager.verify_identity(1, signature, message)
    print(f"Is the signature valid? {is_valid}")
  
