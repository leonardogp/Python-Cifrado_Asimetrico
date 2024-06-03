from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Generar clave privada RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Generar clave pública RSA a partir de la clave privada
public_key = private_key.public_key()

# Serializar claves para guardarlas en archivos
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.OpenSSH,
    format=serialization.PublicFormat.OpenSSH
)

# Guardar claves en archivos
with open('private_key.pem', 'wb') as f:
    f.write(pem_private_key)

with open('public_key.pub', 'wb') as f:
    f.write(pem_public_key)