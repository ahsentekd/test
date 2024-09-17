api_key = "1234567890abcdef"
db_password = "password123"
secret_key = "my_secret_key_1234"
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflK7Fhw27G0MTwCF_EU11H7a3o91zF7G4D5SH4z"
url = "https://example.com/login?username=admin&password=secret"
oauth_client_secret = "client_secret_9876543210"
ssh_private_key = """
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA7s7F2I3L4K2u5f5t6a6N9nU3W9V6A3TxT+NnRT4F4mYcI8Qs
...
-----END RSA PRIVATE KEY-----
"""
encryption_key = "s3cr3t_encryption_key_!@#"
admin_password = "admin_pass_123"
jwt_secret = "jwt_super_secret_!@#"

user_name = "JohnDoe"

db_config = {
    "host": "localhost",
    "port": 5432,
    "user": "admin",
    "password": "******"
}

complete_secret = "The key is " + secret_part + "_key"

import os
api_key = os.getenv('API_KEY')


