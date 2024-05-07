#Define the alphabetical content in this array.
content="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 

def encrypt(strin,key):
	keywrap=key*(len(strin)//len(key))
	keywrap+=key[:len(strin)%len(key)]
	encryptedData=""
	for i in range(len(strin)):
		encryptedData+=content[((content.index(strin[i])+content.index(keywrap[i]))%62)]
	return encryptedDatabb

def decrypt(strin,key):
	keywrap=key*(len(strin)//len(key))
	keywrap+=key[:len(strin)%len(key)]
	decryptedData=""
	for i in range(len(strin)):
		decryptedData+=content[((content.index(strin[i])-content.index(keywrap[i]))%62)]
	return decryptedData

msg="Your Message"
key="Your Key"

enc=encrypt(msg,key)

print(enc)
print("Encrypted succesfully!!!")
print(decrypt(enc,key))
print("Decrypted succesfully!!")