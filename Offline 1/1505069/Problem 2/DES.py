import  Convertion

# taking input for key and plain text
#key = input("Enter key : ")
#plaintext = input("Enter plain text : ")

key="megabuck"
plaintext="Hello world"
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
key_in_64bits=Convertion.tobits(key)
# convert key into 56 bits
key_in_56bits=Convertion.to56bits(key_in_64bits)

for i in range(0 , chunks) :
    # Group the plaintext by 64 bits
    current_text = plaintext[i*8:(i+1)*8]
    current_text_in_bits = Convertion.tobits(current_text)

    # tranposed current text
    input_text = Convertion.Initial_Transpose(current_text_in_bits)

    SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for j in range(0,16):
        # get first and second half after shifting
        firsthalf_from_key = Convertion.getfirsthalf(key_in_56bits,SHIFT[j])
        secondhalf_from_key = Convertion.getsecondhalf(key_in_56bits,SHIFT[j])
        current_key = []
        for k in range(0,28):
            current_key.append(firsthalf_from_key[k])
        for k in range(0, 28):
            current_key.append(secondhalf_from_key[k])

        # convert key into 48 bits
        current_key = Convertion.keyto48bits(current_key)

        left_from_text = Convertion.getfirsthalftext(input_text)
        right_from_text = Convertion.getsecondhalftext(input_text)

        #expanding data to 48 bits
        expanded_right_from_text = Convertion.expandbits(right_from_text)

        #xoring current key and expanded right bit
        Xored_bit = []
        for k in range(0,48):
            Xored_bit.append(current_key[k]^expanded_right_from_text[k])

        # sampling 32 bits

        sampledbit=Convertion.samplebit(Xored_bit)

        # simulated by P-box
        simulatedbit=Convertion.PBox(sampledbit)


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
    cipherbit=Convertion.Final_Transpose(swapbit)

    cipher_text+=Convertion.frombits(cipherbit)
print(cipher_text)