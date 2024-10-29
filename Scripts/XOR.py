# Define the inputs
username = "mlxs"
xor_string = ".>!#9\\I ^:K!4;0@?_"

extended_username = (username * ((len(xor_string) // len(username)) + 1))[:len(xor_string)]

# Perform byte-by-byte XOR
xor_result = ''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(extended_username, xor_string))

# Convert the result to ASCII
print(xor_result)
