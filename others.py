from Crypto.Cipher import DES
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


print("\n")
prGreen("1.DES ECB - Weak Keys attack")
prGreen("2.DES OFB - Weak Keys attack")

b = int(input(">>>"))

if(b==1):
	prGreen("Give Cipher text in hex")
	ciphertext = input(">>>")
	ciphertext = bytes.fromhex(ciphertext)

	KEY=b'\x00\x00\x00\x00\x00\x00\x00\x00'
	a = DES.new(KEY, DES.MODE_ECB)
	plaintext = a.decrypt(ciphertext)

	prGreen("Key 1 :"+str(plaintext))

	KEY=b'\x1E\x1E\x1E\x1E\x0F\x0F\x0F\x0F'
	a = DES.new(KEY, DES.MODE_ECB)
	plaintext = a.decrypt(ciphertext)
	prGreen("Key 2 :"+str(plaintext))

	KEY=b"\xE1\xE1\xE1\xE1\xF0\xF0\xF0\xF0"
	a = DES.new(KEY, DES.MODE_ECB)
	plaintext = a.decrypt(ciphertext)
	prGreen("Key 3 :"+str(plaintext))

	KEY=b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
	a = DES.new(KEY, DES.MODE_ECB)
	plaintext = a.decrypt(ciphertext)
	prGreen("Key 4 :"+str(plaintext))

if(b==2):
	prGreen("Give Ciphertext in hex")
	ciphertext = input(">>>")
	ciphertext = bytes.fromhex(ciphertext)
	prGreen("Give IV in hex")
	IV = input(">>>")
	IV = bytes.fromhex(IV)

	KEY=b'\x00\x00\x00\x00\x00\x00\x00\x00'
	a = DES.new(KEY, DES.MODE_OFB, IV)
	plaintext = a.decrypt(ciphertext)

	prGreen("Key 1 :"+str(plaintext))

	KEY=b'\x1E\x1E\x1E\x1E\x0F\x0F\x0F\x0F'
	a = DES.new(KEY, DES.MODE_OFB, IV)
	plaintext = a.decrypt(ciphertext)
	prGreen("Key 2 :"+str(plaintext))

	KEY=b"\xE1\xE1\xE1\xE1\xF0\xF0\xF0\xF0"
	a = DES.new(KEY, DES.MODE_OFB, IV)
	plaintext = a.decrypt(ciphertext)
	prGreen("Key 3 :"+str(plaintext))

	KEY=b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
	a = DES.new(KEY, DES.MODE_OFB, IV)
	plaintext = a.decrypt(ciphertext)
	prGreen("Key 4 :"+str(plaintext))