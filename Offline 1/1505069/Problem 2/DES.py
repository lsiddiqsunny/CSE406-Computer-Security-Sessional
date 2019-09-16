import  Conversion

# taking input for key and plain text
#key = input("Enter key : ")
#plaintext = input("Enter plain text : ")

key=input("Enter key : ")
plaintext=input("Enter plain text : ")

# Encryption

# padding with ~ to make it divisible by 8
length = len(plaintext)
if length % 8 != 0 :
    remain = 8-(length % 8)
    for i in range(0,remain):
        plaintext=plaintext+"~"

length = len(plaintext)
chunks=length//8
cipher_text=""

# convert key to bit
key_in_64bits=Conversion.tobits(key)

# convert key into 56 bits
key_in_56bits=Conversion.to56bits(key_in_64bits)


SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
keys=[]
for j in range(0,16):
    # get first and second half after shifting
    firsthalf_from_key = Conversion.getfirsthalf(key_in_56bits, SHIFT[j])
    secondhalf_from_key = Conversion.getsecondhalf(key_in_56bits, SHIFT[j])
    current_key = []
    for k in range(0,28):
        current_key.append(firsthalf_from_key[k])
    for k in range(0, 28):
        current_key.append(secondhalf_from_key[k])

    # convert key into 48 bits
    current_key = Conversion.keyto48bits(current_key)
    keys.append(current_key)


for i in range(0 , chunks) :
    # Group the plaintext by 64 bits
    current_text = plaintext[i*8:(i+1)*8]
    current_text_in_bits = Conversion.tobits(current_text)

    # tranposed current text
    input_text = Conversion.Initial_Transpose(current_text_in_bits)


    for j in range(0,16):

        current_key=keys[j]
        left_from_text = Conversion.getfirsthalftext(input_text)
        right_from_text = Conversion.getsecondhalftext(input_text)

        #expanding data to 48 bits
        expanded_right_from_text = Conversion.expandbits(right_from_text)

        #xoring current key and expanded right bit
        Xored_bit = []
        for k in range(0,48):
            Xored_bit.append(current_key[k]^expanded_right_from_text[k])

        # sampling 32 bits

        sampledbit=Conversion.samplebit(Xored_bit)

        # simulated by P-box
        simulatedbit=Conversion.PBox(sampledbit)


        righ_output = []
        for k in range(0,32):
            righ_output.append(left_from_text[k]^simulatedbit[k])

        newinput_text = []
        for k in range(0,32):
            newinput_text.append(right_from_text[k])
        for k in range(0,32):
            newinput_text.append(righ_output[k])

        input_text=newinput_text
       # print(input_text)


    swapbit = []
    for j in range(0,32):
        swapbit.append(input_text[j+32])
    for j in range(0,32):
        swapbit.append(input_text[j])
    cipherbit=Conversion.Final_Transpose(swapbit)

    cipher_text+=Conversion.frombits(cipherbit)
print("Ciphered : "+cipher_text)

#Decryption
newplaintext=""

for i in range(0 , chunks) :
    # Group the plaintext by 64 bits
    current_text = cipher_text[i*8:(i+1)*8]
    current_text_in_bits = Conversion.tobits(current_text)

    # tranposed current text
    input_text = Conversion.Initial_Transpose(current_text_in_bits)


    for j in range(0,16):

        current_key=keys[16-j-1]
        left_from_text = Conversion.getfirsthalftext(input_text)
        right_from_text = Conversion.getsecondhalftext(input_text)

        #expanding data to 48 bits
        expanded_right_from_text = Conversion.expandbits(right_from_text)

        #xoring current key and expanded right bit
        Xored_bit = []
        for k in range(0,48):
            Xored_bit.append(current_key[k]^expanded_right_from_text[k])

        # sampling 32 bits

        sampledbit=Conversion.samplebit(Xored_bit)

        # simulated by P-box
        simulatedbit=Conversion.PBox(sampledbit)


        righ_output = []
        for k in range(0,32):
            righ_output.append(left_from_text[k]^simulatedbit[k])

        newinput_text = []
        for k in range(0,32):
            newinput_text.append(right_from_text[k])
        for k in range(0,32):
            newinput_text.append(righ_output[k])

        input_text=newinput_text
       # print(input_text)

    swapbit = []
    for j in range(0,32):
        swapbit.append(input_text[j+32])
    for j in range(0,32):
        swapbit.append(input_text[j])
    cipherbit=Conversion.Final_Transpose(swapbit)

    newplaintext+=Conversion.frombits(cipherbit)

newplaintext=newplaintext[0:-remain]
print("Deciphered : "+newplaintext)