import hashlib
import base58
import binascii

with open("/home/nex/resultGit1.txt", "r") as f:    #Input file path
      for line in f:
        # private_key_WIF = input("WIF: ")
        first_encode = base58.b58decode(line)
        private_key_full = binascii.hexlify(first_encode)
        private_key = private_key_full[2:-8]

        print(private_key)

# grep -E -o '5[HJK][1-9A-HJ-NP-Za-km-z]{49}' dir/test.txt > goal.txt
# grep -E -o '[KL][1-9A-HJ-NP-Za-km-z]{51}' dir/test > goal.txt



# private_key_WIF = input("WIF: ")
# first_encode = base58.b58decode(private_key_WIF)
# private_key_full = binascii.hexlify(first_encode)
# private_key = private_key_full[2:-8]
# print(private_key)
