## RSA algorythm python implementation
The main RSA class is in the `rsa.py` file. Everything needed for proper algorythm work is in the `utils.py` file.  

The following functions were implemented:
-    gcd (greatest common divider)
-    Miller Rabin's primality check
-    large prime number pseudorandom generation
-    extended euclid's algorythm

### Usage

Just create a `RSA` class and use it's methods.

    >>> from rsa import RSA
    >>> A = RSA()  # Alice
    >>> B = RSA()  # Bob
    >>> E = RSA()  # Eve
    >>> ciphertext_B = A.encrypt("Hello Bob", B.public_key)
    >>> B.decrypt(ciphertext_B) 
    'Hello Bob'

    >>> E.decrypt(ciphertext_B)
    '\x12\x0eA\x8c\xc5\x1f\xa1\x05\xfe\x80Q\x1e\x1b|\xbb\xb8\xe9\xa6\x84\xc1\xda\x8b:XC\xed\x91\xb8\x12q\x11\xd9'
    
Eve can't see our cyphered message.
