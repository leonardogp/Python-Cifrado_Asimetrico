from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Cargar clave pública desde archivo
with open('public_key.pub', 'rb') as f:
    public_key = serialization.load_ssh_public_key(f.read(), backend=default_backend())

# Mensaje a cifrar
message = b'¡Hola, Mundo!'

# Cifrar mensaje utilizando la clave pública
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)