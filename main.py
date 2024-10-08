# Function to perform bitwise AND
def bitwise_and(str1, str2):
    return ''.join(['1' if str1[i] == '1' and str2[i] == '1' else '0' for i in range(len(str1))])

# Function to perform bitwise OR
def bitwise_or(str1, str2):
    return ''.join(['1' if str1[i] == '1' or str2[i] == '1' else '0' for i in range(len(str1))])

# Function to perform bitwise XOR
def bitwise_xor(str1, str2):
    return ''.join(['1' if str1[i] != str2[i] else '0' for i in range(len(str1))])

bit_string_1 = input("Enter the first bit string: ")
bit_string_2 = input("Enter the second bit string: ")

if len(bit_string_1) != len(bit_string_2):
    print("Error: Bit strings must have the same length.")
else:
    print("Bitwise AND: ", bitwise_and(bit_string_1, bit_string_2))
    print("Bitwise OR:  ", bitwise_or(bit_string_1, bit_string_2))
    print("Bitwise XOR: ", bitwise_xor(bit_string_1, bit_string_2))