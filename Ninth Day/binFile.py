#Binary File

#Writing to a binary File
data = b'\x00\x01\x02\x03\x04'
with open('example.bin' , 'wb') as file:
    file.write(data)
