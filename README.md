# xor calculator
A Python script to XOR values also known as XOR decryption.
If you're not familiar with XOR, think of it like a box with a key. The box holds the string, and the key unlocks it simple as that. Just enter the two values, and the script will compare them and return the plaintext.

## Code
### Original cpp code
```C++
void main()
{
	printf("first\n");
	printf(xorstr_("Hello World\n"));
}
```
### IDA Pro Output
```asm
  *(_QWORD *)_Format = 0x5590329DB441A4BBLL; ; Message
  *(_QWORD *)&_Format[8] = 0xCBD43E3710EE1EF6uLL;
  v6.m128i_i64[0] = 0x3AC712F2D82DC1F3LL; ; Key
``` 
### Script output 
```
Key: 0x5590329DB441A4BB
String: 0x3AC712F2D82DC1F3
XOR Result: 0X6F57206F6C6C6548
H
e
l
l
o
W
o
```
## ToDo 
1. Support ida
2. Improve the output formatting
