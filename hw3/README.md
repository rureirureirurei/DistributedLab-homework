## SHA-256 python implementation
The sha256 hash function is in the `SHA256.py` file. Some needed functions, such as rotations and abbreviations are in the `helper_functions.py`. 

The code follows the NIST FIPS 180-4 standard, which can be found here: http://dx.doi.org/10.6028/NIST.FIPS.180-4

### Usage

For the testing, you can use prewritten code:  
`$ python3 test.py`  
If all the tests passed correctly, you should see:  
`All tests passed OK`

If you want to get a SHA256 hash, do:

    from SHA256 import sha256hash
    h = sha256hash('some text')
    
The function returns an array of bytes, to get a number use `.hex()`.

