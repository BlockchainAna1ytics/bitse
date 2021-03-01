# From public key to address
# Reference: https://medium.freecodecamp.org/how-to-create-a-bitcoin-wallet-address-from-a-private-key-eca3ddd9c05f
#            https://docs.python.org/2/library/hashlib.html
# https://jun-wang-2018.github.io/MyBlog/en/ECDSA-and-Bitcoin-III/
import codecs  #If not installed: "pip3 install codecs"
import hashlib
# UK0 is a demo public key.
UK0 = ['3a56bd64573c28050bfe202c57e56b46c63744a253d1430e2b737876fa883b19','73c2f565444dc62151562993ff4b566c826010befb289fa2fc749293266066c0']
UK1 = "04" + UK0[0] + UK0[1]
UK2 = hashlib.sha256(codecs.decode(UK1, 'hex'))
h = hashlib.new('ripemd160')
h.update(UK2.digest())
UK3 = h.hexdigest()
UK4 = "00" + UK3
UK5 = hashlib.sha256(codecs.decode(UK4, 'hex'))
UK6 = hashlib.sha256(UK5.digest())
checksum = codecs.encode(UK6.digest(), 'hex')[0:8]
UK7 = UK4 + str(checksum)[2:10]  #I know it looks wierd

# Define base58
def base58(address_hex):
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    b58_string = ''
    # Get the number of leading zeros
    leading_zeros = len(address_hex) - len(address_hex.lstrip('0'))
    # Convert hex to decimal
    address_int = int(address_hex, 16)
    # Append digits to the start of string
    while address_int > 0:
        digit = address_int % 58
        digit_char = alphabet[digit]
        b58_string = digit_char + b58_string
        address_int //= 58
    # Add ‘1’ for each 2 leading zeros
    ones = leading_zeros // 2
    for one in range(ones):
        b58_string = '1' + b58_string
    return b58_string

Address = base58(UK7)
print(Address)