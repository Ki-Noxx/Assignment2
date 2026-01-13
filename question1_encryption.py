# Question 1: Custom Text Encryption and Decryption
# This program encrypts text based on specific rules,
# decrypts it, and verifies correctness.

def encrypt_char(char, shift1, shift2):
    """Encrypt a single character based on given rules"""

    # Lowercase letters
    if char.islower():
        if 'a' <= char <= 'm':
            shift = shift1 * shift2
            return chr((ord(char) - 97 + shift) % 26 + 97)
        elif 'n' <= char <= 'z':
            shift = shift1 + shift2
            return chr((ord(char) - 97 - shift) % 26 + 97)

    # Uppercase letters
    elif char.isupper():
        if 'A' <= char <= 'M':
            return chr((ord(char) - 65 - shift1) % 26 + 65)
        elif 'N' <= char <= 'Z':
            shift = shift2 ** 2
            return chr((ord(char) - 65 + shift) % 26 + 65)

    # Other characters remain unchanged
    return char


def decrypt_char(char, shift1, shift2):
    """Decrypt a single character by reversing encryption rules"""

    # Lowercase letters
    if char.islower():
        if 'a' <= char <= 'm':
            shift = shift1 * shift2
            return chr((ord(char) - 97 - shift) % 26 + 97)
        elif 'n' <= char <= 'z':
            shift = shift1 + shift2
            return chr((ord(char) - 97 + shift) % 26 + 97)

    # Uppercase letters
    elif char.isupper():
        if 'A' <= char <= 'M':
            return chr((ord(char) - 65 + shift1) % 26 + 65)
        elif 'N' <= char <= 'Z':
            shift = shift2 ** 2
            return chr((ord(char) - 65 - shift) % 26 + 65)

    return char


def encrypt_file(shift1, shift2):
    """Reads raw_text.txt and writes encrypted_text.txt"""

    with open("raw_text.txt", "r", encoding="utf-8") as infile:
        text = infile.read()

    encrypted = ""
    for char in text:
        encrypted += encrypt_char(char, shift1, shift2)

    with open("encrypted_text.txt", "w", encoding="utf-8") as outfile:
        outfile.write(encrypted)


def decrypt_file(shift1, shift2):
    """Reads encrypted_text.txt and writes decrypted_text.txt"""

    with open("encrypted_text.txt", "r", encoding="utf-8") as infile:
        text = infile.read()

    decrypted = ""
    for char in text:
        decrypted += decrypt_char(char, shift1, shift2)

    with open("decrypted_text.txt", "w", encoding="utf-8") as outfile:
        outfile.write(decrypted)


def verify_decryption():
    """Compares raw_text.txt and decrypted_text.txt"""

    with open("raw_text.txt", "r", encoding="utf-8") as f1:
        original = f1.read()

    with open("decrypted_text.txt", "r", encoding="utf-8") as f2:
        decrypted = f2.read()

    if original == decrypted:
        print("Decryption successful. Files match.")
    else:
        print("Decryption failed. Files do not match.")


# ---------------- MAIN PROGRAM ----------------

# Step 1: Get user inputs
shift1 = int(input("Enter shift1 value: "))
shift2 = int(input("Enter shift2 value: "))

# Step 2: Encrypt file
encrypt_file(shift1, shift2)

# Step 3: Decrypt file
decrypt_file(shift1, shift2)

# Step 4: Verify correctness
verify_decryption()