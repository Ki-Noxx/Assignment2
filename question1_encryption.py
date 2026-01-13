
# Question 1: Text Encryption and Decryption

# Shift value for Caesar Cipher
SHIFT = 3


def encrypt_text(text):
    """
    This function encrypts the given text by shifting
    each alphabetical character forward by SHIFT.
    Uppercase and lowercase letters are handled separately.
    Non-alphabet characters are left unchanged.
    """
    encrypted = ""

    # Loop through each character in the text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Convert character to ASCII, apply shift, then convert back
            encrypted += chr((ord(char) - 65 + SHIFT) % 26 + 65)

        # Check if the character is a lowercase letter
        elif char.islower():
            encrypted += chr((ord(char) - 97 + SHIFT) % 26 + 97)

        # If character is not a letter, keep it the same
        else:
            encrypted += char

    return encrypted


def decrypt_text(text):
    """
    This function decrypts the encrypted text by shifting
    each alphabetical character backward by SHIFT.
    This reverses the encryption process.
    """
    decrypted = ""

    # Loop through each character in the encrypted text
    for char in text:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted += chr((ord(char) - 65 - SHIFT) % 26 + 65)

        # Decrypt lowercase letters
        elif char.islower():
            decrypted += chr((ord(char) - 97 - SHIFT) % 26 + 97)

        # Keep non-alphabet characters unchanged
        else:
            decrypted += char

    return decrypted


# ---------------- MAIN PROGRAM ----------------

# Step 1: Open and read the original text file
with open("raw_text.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

# Step 2: Encrypt the original text
encrypted_text = encrypt_text(raw_text)

# Step 3: Save the encrypted text into a new file
with open("encrypted_text.txt", "w", encoding="utf-8") as file:
    file.write(encrypted_text)

# Step 4: Decrypt the encrypted text back to original
decrypted_text = decrypt_text(encrypted_text)

# Step 5: Verify that decrypted text matches original text
if decrypted_text == raw_text:
    print("Decryption successful. Text matches original.")
else:
    print("Decryption failed. Text does not match original.")
