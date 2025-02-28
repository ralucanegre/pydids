import hashlib
import json
import time
import ed25519  # For Ed25519 key generation and signing/verification

# Helper function to generate Ed25519 keys
def generate_keys():
    # Generate Ed25519 private and public keys
    private_key, public_key = ed25519.create_keypair()

    # Serialize private and public keys to PEM format (or base64/hex encoding if preferred)
    private_pem = private_key.to_bytes()
    public_pem = public_key.to_bytes()

    return private_pem, public_pem
