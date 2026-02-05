import numpy as np
from math import gcd

def letter_to_number(letter):
    return ord(letter.upper()) - ord('A') + 1

def number_to_letter(number):
    return chr((number - 1) % 26 + ord('A'))

def encode_message(message, matrix):
    numbers = [letter_to_number(char) for char in message.upper() if char.isalpha()]
    n = len(matrix)
    while len(numbers) % n != 0:
        numbers.append(0)
    blocks = [numbers[i:i + n] for i in range(0, len(numbers), n)]
    encoded_blocks = []
    for block in blocks:
        encoded_block = np.dot(matrix, block) % 26
        encoded_blocks.append(encoded_block)
    return [int(num) for block in encoded_blocks for num in block]

def decode_message(encoded_numbers, matrix):
    det = int(round(np.linalg.det(matrix)))
    if gcd(det, 26) != 1:
        raise ValueError("The determinant of the matrix is not coprime with 26. Decoding is not possible.")
    det_inv = pow(det, -1, 26)
    adj_matrix = np.round(det * np.linalg.inv(matrix)).astype(int) % 26
    inverse_matrix = (det_inv * adj_matrix) % 26
    n = len(matrix)
    blocks = [encoded_numbers[i:i + n] for i in range(0, len(encoded_numbers), n)]
    decoded_blocks = []
    for block in blocks:
        decoded_block = np.dot(inverse_matrix, block) % 26
        decoded_blocks.append(decoded_block)
    decoded_numbers = [int(num) for block in decoded_blocks for num in block]
    decoded_message = ''.join(number_to_letter(num) for num in decoded_numbers if num > 0)
    return decoded_message

def validate_matrix(matrix):
    det = int(round(np.linalg.det(matrix)))
    if gcd(det, 26) != 1:
        print(f"Invalid matrix. Determinant ({det}) is not coprime with 26.")
        return False
    return True

if __name__ == "__main__":
    print("Welcome to the Encoding/Decoding Program!")
    choice = input("Choose an operation:\n1. Encode a message\n2. Decode a message\nEnter 1 or 2:")
    if choice == '1':
        message = input("Enter the message to encode: ")
        print("Enter the encoding matrix (2x2 or 3x3). Example for 2x2:\n2 3\n1 1")
        matrix_size = int(input("Enter matrix size (2 for 2x2, 3 for 3x3):"))
        matrix = []
        for i in range(matrix_size):
            row = list(map(int, input(f"Enter row {i + 1}:").split()))
            matrix.append(row)
        matrix = np.array(matrix)
        if not validate_matrix(matrix):
            print("Please restart the program and enter a valid matrix.")
        else:
            encoded_message = encode_message(message, matrix)
            print("\nEncoded Message:", encoded_message)
    elif choice == '2':
        encoded_numbers = list(map(int, input("Enter the encoded numbers (space-separated):").split()))
        print("Enter the encoding matrix (2x2 or 3x3) used for encoding:")
        matrix_size = int(input("Enter matrix size (2 for 2x2, 3 for 3x3):"))
        matrix = []
        for i in range(matrix_size):
            row = list(map(int, input(f"Enter row {i + 1}:").split()))
            matrix.append(row)
        matrix = np.array(matrix)
        if not validate_matrix(matrix):
            print("Please restart the program and enter a valid matrix.")
        else:
            decoded_message = decode_message(encoded_numbers, matrix)
            print("\nDecoded Message:", decoded_message)
    else:
        print("Invalid choice. Please restart the program.")