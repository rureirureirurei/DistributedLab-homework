from SHA256 import sha256hash

if __name__ == '__main__':
    TESTSET = [
            {'val' : 'pokek doliloli', 'hash' : 'f34d6a11af126c4d27256deb127ad5609da7d6db49499bc99104e1daa66ce361'},
            {'val' : 'DDDDDDDD', 'hash' : 'b1eedd29abf7e8b9b5c67030fc59dd42a4e16a0585c26176de357a4757515ed6'},
            {'val' : 'kek hello world :)', 'hash' : '6c375e609a486ca75913d2ef85e36eaccef93c66bc38dc14de33ca97377897fd'}
        ]



    for test in TESTSET:
        assert sha256hash(test['val']).hex() == test['hash']

    print('All tests passed')
