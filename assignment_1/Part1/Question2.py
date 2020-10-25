String1 = '''I'm a "Alaric"'''
print("Initial String with use of Triple Quotes: ")
print(String1)
String1 = 'I\'m a "Alaric"'
print("\nEscaping Single Quote: ")
print(String1)
String1 = "I'm a \"Alaric\""
print("\nEscaping Double Quotes: ")
print(String1)
String1 = "C:\\Python\\Alaric\\"
print("\nEscaping Backslashes: ")
print(String1)
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ")
print(String1)
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)


# Out Put
Initial String with use of Triple Quotes:
I'm a "Alaric"

Escaping Single Quote:
I'm a "Alaric"

Escaping Double Quotes:
I'm a "Alaric"

Escaping Backslashes:
C: \Python\Alaric\

Printing in HEX with the use of Escape Sequences:
This is Geeks in HEX

Printing Raw String in HEX Format:
This is \x47\x65\x65\x6b\x73 in \x48\x45\x58
