def my_function(message, decalage=3):
    return ''.join([chr((ord(char) - 
                        ord('A' if char.isupper() else 'a') + decalage) % 26 + 
                        ord('A' if char.isupper() else 'a')) 
                        if char.isalpha() else char for char in message])

message_original = "Bonjour, Jules César!"
print(f"Message original: {message_original}")
message_chiffre = my_function(message_original)
print(f"Message chiffré: {message_chiffre}")