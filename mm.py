def generate_matrix(key):
    key = key.upper().replace('J', 'I')  # Replace J with I
    matrix = []
    used = set()

    for char in key:
        if char not in used and char.isalpha():
            matrix.append(char)
            used.add(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # No 'J'
        if char not in used:
            matrix.append(char)
            used.add(char)

    # Convert list into 5x5 matrix
    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def prepare_text(text):
    text = text.upper().replace('J', 'I')
    text = ''.join(filter(str.isalpha, text))

    prepared = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        char2 = ''
        if i + 1 < len(text):
            char2 = text[i + 1]
        if char1 == char2:
            prepared += char1 + 'X'
            i += 1
        else:
            prepared += char1
            if char2:
                prepared += char2
                i += 2
            else:
                prepared += 'X'
                i += 1
    if len(prepared) % 2 != 0:
        prepared += 'X'
    return prepared

def playfair_encrypt(plaintext, key):
    matrix = generate_matrix(key)
    text = prepare_text(plaintext)
    cipher_text = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            cipher_text += matrix[row1][(col1 + 1) % 5]
            cipher_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += matrix[(row1 + 1) % 5][col1]
            cipher_text += matrix[(row2 + 1) % 5][col2]
        else:
            cipher_text += matrix[row1][col2]
            cipher_text += matrix[row2][col1]

    return cipher_text

# Example usage:
key = "ASIF"
plaintext = "UMBRELLA"
ciphertext = playfair_encrypt(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
