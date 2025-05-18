

# Do I have to explain this?
def ToHex(Param):
    return hex(Param)

# Come on it's obvious
def XOR(Key, Str):
    return Key ^ Str

# XOR will flip the text so we need
# To get it in the right order
def Translate(Result):
    for i in reversed(Result):
        print(i)

# Compare the string with 16 digits integers AKA Hexadecimal
def Compare(Out):
    return int(Out, 16)


# Now we take the inputs as string
Key = input('Key: ')
StrValue = input('String: ')


# Compare the strings with hexdecimal
Key = Compare(Key)
StrValue = Compare(StrValue)

# Xor result
Result = XOR(Key, StrValue)


print('XOR Result:', ToHex(Result).upper())

# Convert & Translate
length = (Result.bit_length() + 7) // 8
try:
    AsciiOut = Result.to_bytes(length, 'big').decode('ascii')
    Translate(AsciiOut)
except UnicodeDecodeError:
    print('UnicodeDecodeError!')