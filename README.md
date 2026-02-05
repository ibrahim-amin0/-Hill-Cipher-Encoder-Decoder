# 🔐 Hill Cipher Encoder/Decoder

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-Latest-orange.svg)
![Cryptography](https://img.shields.io/badge/Type-Cryptography-red.svg)


**A Python implementation of the Hill Cipher encryption algorithm using matrix operations**

Encode and decode messages using linear algebra and modular arithmetic

</div>

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [What is Hill Cipher?](#what-is-hill-cipher)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Mathematical Background](#mathematical-background)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 Project Overview

This project implements the **Hill Cipher**, a polygraphic substitution cipher based on linear algebra. It was invented by Lester S. Hill in 1929 and uses matrix multiplication to encrypt and decrypt messages.

### 🎓 Educational Purpose

This implementation is designed to help understand:
- Classical cryptography concepts
- Matrix operations in cryptography
- Modular arithmetic (mod 26)
- Matrix invertibility and determinants
- Greatest Common Divisor (GCD) applications

---

## 🔑 What is Hill Cipher?

The **Hill Cipher** is a polygraphic substitution cipher that encrypts blocks of letters simultaneously. Unlike simple substitution ciphers that replace one letter at a time, Hill Cipher uses linear algebra to transform blocks of plaintext into ciphertext.

### Key Characteristics:

- 📊 **Block Cipher**: Encrypts multiple letters at once
- 🔢 **Matrix-Based**: Uses matrix multiplication for encryption
- 🔄 **Symmetric**: Same key (matrix) used for encryption and decryption
- 🧮 **Modular Arithmetic**: All operations performed modulo 26
- 🔐 **Polyalphabetic**: Each letter can map to multiple ciphertext letters

---

## ✨ Key Features

- ✅ **Encode Messages** - Encrypt plaintext using a key matrix
- ✅ **Decode Messages** - Decrypt ciphertext with the same key matrix
- ✅ **Flexible Matrix Size** - Supports 2x2 and 3x3 matrices
- ✅ **Matrix Validation** - Ensures matrix is valid for decryption
- ✅ **Automatic Padding** - Handles messages of any length
- ✅ **Error Handling** - Validates matrix invertibility
- ✅ **Interactive CLI** - User-friendly command-line interface
- ✅ **Case Insensitive** - Works with both uppercase and lowercase letters

---

## 🔬 How It Works

### Encoding Process:

1. **Text to Numbers**: Convert letters to numbers (A=1, B=2, ..., Z=26)
2. **Padding**: Add zeros if message length isn't divisible by matrix size
3. **Block Formation**: Split numbers into blocks matching matrix size
4. **Matrix Multiplication**: Multiply each block by the key matrix
5. **Modulo Operation**: Apply mod 26 to keep values in range [0, 25]
6. **Output**: Return encoded numbers

### Decoding Process:

1. **Matrix Validation**: Check if determinant is coprime with 26
2. **Matrix Inversion**: Calculate modular inverse of key matrix
3. **Block Decoding**: Multiply encoded blocks by inverse matrix
4. **Modulo Operation**: Apply mod 26
5. **Numbers to Text**: Convert numbers back to letters
6. **Output**: Return decoded message

---

## 🚀 Installation

### Prerequisites

```bash
Python 3.8 or higher
pip package manager
```

### Setup

1. **Clone or download the repository**
```bash
git clone https://github.com/yourusername/hill-cipher.git
cd hill-cipher
```

2. **Install required dependencies**
```bash
pip install numpy
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### Running the Program

```bash
python encode_decode.py
```

### Interactive Mode

The program will prompt you to:

1. **Choose Operation**
   - Enter `1` to encode a message
   - Enter `2` to decode a message

2. **For Encoding:**
   - Enter your message (letters only, spaces ignored)
   - Choose matrix size (2 or 3)
   - Enter the key matrix row by row

3. **For Decoding:**
   - Enter encoded numbers (space-separated)
   - Choose matrix size (2 or 3)
   - Enter the same key matrix used for encoding

---

## 📝 Examples

### Example 1: Encoding with 2x2 Matrix

```
Welcome to the Encoding/Decoding Program!
Choose an operation:
1. Encode a message
2. Decode a message
Enter 1 or 2: 1

Enter the message to encode: HELLO
Enter the encoding matrix (2x2 or 3x3). Example for 2x2:
2 3
1 1
Enter matrix size (2 for 2x2, 3 for 3x3): 2
Enter row 1: 2 3
Enter row 2: 1 1

Encoded Message: [23, 7, 15, 11, 19, 11]
```

### Example 2: Decoding with 2x2 Matrix

```
Welcome to the Encoding/Decoding Program!
Choose an operation:
1. Encode a message
2. Decode a message
Enter 1 or 2: 2

Enter the encoded numbers (space-separated): 23 7 15 11 19 11
Enter the encoding matrix (2x2 or 3x3) used for encoding:
Enter matrix size (2 for 2x2, 3 for 3x3): 2
Enter row 1: 2 3
Enter row 2: 1 1

Decoded Message: HELLO
```

### Example 3: Encoding with 3x3 Matrix

```
Enter the message to encode: CRYPTOGRAPHY
Enter matrix size (2 for 2x2, 3 for 3x3): 3
Enter row 1: 6 24 1
Enter row 2: 13 16 10
Enter row 3: 20 17 15

Encoded Message: [8, 17, 23, 20, 5, 8, 18, 14, 15, 18, 18, 23]
```

### Example 4: Invalid Matrix Detection

```
Enter matrix size (2 for 2x2, 3 for 3x3): 2
Enter row 1: 2 4
Enter row 2: 1 2

Invalid matrix. Determinant (0) is not coprime with 26.
Please restart the program and enter a valid matrix.
```

---

## 🧮 Mathematical Background

### Letter to Number Conversion

```
A = 1, B = 2, C = 3, ..., Z = 26
```

However, for modulo 26 arithmetic:
```
A = 0, B = 1, C = 2, ..., Z = 25
```

### Encoding Formula

For a message block **M** and key matrix **K**:

```
C = (K × M) mod 26
```

Where:
- **C** = Ciphertext block
- **K** = Key matrix (n×n)
- **M** = Message block (n×1 vector)

### Decoding Formula

```
M = (K⁻¹ × C) mod 26
```

Where:
- **K⁻¹** = Modular inverse of key matrix

### Matrix Invertibility Condition

For a matrix to be valid for Hill Cipher:

```
gcd(det(K), 26) = 1
```

This means the determinant must be **coprime** with 26.

**Valid Determinants mod 26:**
1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25

**Invalid Determinants mod 26:**
0, 2, 4, 6, 8, 10, 12, 13, 14, 16, 18, 20, 22, 24

### Modular Matrix Inverse Calculation

Steps to find **K⁻¹ mod 26**:

1. Calculate determinant: `det(K)`
2. Find modular inverse of determinant: `det⁻¹ mod 26`
3. Calculate adjugate matrix: `adj(K)`
4. Compute: `K⁻¹ = (det⁻¹ × adj(K)) mod 26`

### Example Calculation (2x2 Matrix)

**Key Matrix:**
```
K = [2  3]
    [1  1]
```

**Determinant:**
```
det(K) = (2×1) - (3×1) = -1 ≡ 25 (mod 26)
```

**Check Coprimality:**
```
gcd(25, 26) = 1 ✓ (Valid)
```

**Modular Inverse of Determinant:**
```
25⁻¹ ≡ 25 (mod 26)
```

**Adjugate Matrix:**
```
adj(K) = [ 1  -3]  ≡  [ 1  23] (mod 26)
         [-1   2]     [25   2]
```

**Inverse Matrix:**
```
K⁻¹ = 25 × [ 1  23]  ≡  [ 25  575]  ≡  [25  3] (mod 26)
            [25   2]     [625   50]     [1   24]
```

Simplified:
```
K⁻¹ = [25  3]
      [ 1 24]
```

---

## 📁 Project Structure

```
hill-cipher/
│
├── encode_decode.py          # Main program file
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
│
├── examples/                 # Example usage files
│   ├── example_2x2.txt      # 2x2 matrix examples
│   └── example_3x3.txt      # 3x3 matrix examples
│
├── tests/                    # Unit tests
│   ├── test_encoding.py     # Encoding tests
│   ├── test_decoding.py     # Decoding tests
│   └── test_matrix.py       # Matrix validation tests
│
└── docs/                     # Additional documentation
    ├── mathematical_theory.md
    ├── user_guide.md
    └── api_reference.md
```

---

## 📦 Requirements

### Python Dependencies

```
numpy>=1.19.0
```

Create a `requirements.txt` file:
```txt
numpy>=1.19.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Function Reference

### `letter_to_number(letter)`
Converts a letter to its numerical equivalent.

**Parameters:**
- `letter` (str): Single letter character

**Returns:**
- `int`: Number representation (A=1, B=2, ..., Z=26)

**Example:**
```python
>>> letter_to_number('A')
1
>>> letter_to_number('Z')
26
```

---

### `number_to_letter(number)`
Converts a number back to its letter equivalent.

**Parameters:**
- `number` (int): Number to convert

**Returns:**
- `str`: Letter representation

**Example:**
```python
>>> number_to_letter(1)
'A'
>>> number_to_letter(26)
'Z'
```

---

### `encode_message(message, matrix)`
Encodes a message using the Hill Cipher algorithm.

**Parameters:**
- `message` (str): Plain text message to encode
- `matrix` (numpy.ndarray): Key matrix (2x2 or 3x3)

**Returns:**
- `list`: Encoded message as list of integers

**Example:**
```python
import numpy as np
matrix = np.array([[2, 3], [1, 1]])
encoded = encode_message("HELLO", matrix)
print(encoded)  # [23, 7, 15, 11, 19, 11]
```

---

### `decode_message(encoded_numbers, matrix)`
Decodes an encoded message using the Hill Cipher algorithm.

**Parameters:**
- `encoded_numbers` (list): List of encoded integers
- `matrix` (numpy.ndarray): Same key matrix used for encoding

**Returns:**
- `str`: Decoded message

**Raises:**
- `ValueError`: If matrix determinant is not coprime with 26

**Example:**
```python
import numpy as np
matrix = np.array([[2, 3], [1, 1]])
decoded = decode_message([23, 7, 15, 11, 19, 11], matrix)
print(decoded)  # "HELLO"
```

---

### `validate_matrix(matrix)`
Validates if a matrix can be used for Hill Cipher.

**Parameters:**
- `matrix` (numpy.ndarray): Matrix to validate

**Returns:**
- `bool`: True if valid, False otherwise

**Example:**
```python
import numpy as np
matrix = np.array([[2, 3], [1, 1]])
is_valid = validate_matrix(matrix)
print(is_valid)  # True
```

---

## 🚫 Limitations

### Current Limitations:

1. **Matrix Size Constraints**
   - Only supports 2x2 and 3x3 matrices
   - Larger matrices require code modification

2. **Character Set**
   - Only works with English alphabet (A-Z)
   - Numbers, special characters, and spaces are ignored

3. **Matrix Requirements**
   - Determinant must be coprime with 26
   - Limits available key matrices

4. **Security**
   - Not suitable for modern encryption needs
   - Vulnerable to known-plaintext attacks
   - Educational/historical purposes only

5. **Padding**
   - Adds zeros for padding (may appear as 'A' in decoded message)

### Security Considerations:

⚠️ **WARNING**: This implementation is for **educational purposes only**. 

- Hill Cipher is a **classical cipher** from 1929
- **Not secure** against modern cryptanalysis
- Vulnerable to **known-plaintext attacks**
- Use **modern encryption** (AES, RSA) for real security needs

---

## 🔮 Future Enhancements

### Planned Features:

- [ ] **Support for larger matrices** (4x4, 5x5, n×n)
- [ ] **GUI Interface** using Tkinter or PyQt
- [ ] **File encryption/decryption** (read from and write to files)
- [ ] **Better padding schemes** (avoid trailing 'A's)
- [ ] **Extended character sets** (alphanumeric, special characters)
- [ ] **Matrix generator** (auto-generate valid random matrices)
- [ ] **Batch processing** (encrypt multiple messages)
- [ ] **Key storage** (save and load matrices)
- [ ] **Cryptanalysis tools** (demonstrate vulnerabilities)
- [ ] **Performance optimization** (faster matrix operations)
- [ ] **Web interface** (Flask/Django web app)
- [ ] **Unicode support** (international characters)

### Possible Extensions:

- **Combined ciphers**: Chain Hill Cipher with other classical ciphers
- **Visualization**: Animate the encryption/decryption process
- **Educational mode**: Step-by-step explanation of each operation
- **Matrix library**: Pre-defined valid matrices for quick testing

---

## 🛠 Troubleshooting

### Common Issues:

**1. "Invalid matrix. Determinant is not coprime with 26"**

**Solution:** Choose a matrix whose determinant is coprime with 26. Valid determinants mod 26: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25

**Example of valid matrices:**
```python
# 2x2 valid matrix
[[2, 3],
 [1, 1]]  # det = -1 ≡ 25 (mod 26) ✓

# 3x3 valid matrix
[[6, 24, 1],
 [13, 16, 10],
 [20, 17, 15]]  # det ≡ 1 (mod 26) ✓
```

**2. "ModuleNotFoundError: No module named 'numpy'"**

**Solution:**
```bash
pip install numpy
```

**3. Decoded message has extra letters**

**Cause:** Padding zeros appear as 'A' characters

**Solution:** This is expected behavior. Ignore trailing 'A's in decoded message.

**4. Different encoded output than expected**

**Cause:** Different matrix or implementation

**Solution:** Verify you're using the exact same matrix for encoding and decoding

---

## 🧪 Testing

### Run Unit Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_encoding.py

# Run with verbose output
python -m pytest -v tests/
```

### Manual Testing

Test the program with known examples:

```python
import numpy as np
from encode_decode import encode_message, decode_message

# Test 1: Simple 2x2 encoding
matrix = np.array([[2, 3], [1, 1]])
message = "HELLO"
encoded = encode_message(message, matrix)
decoded = decode_message(encoded, matrix)
assert decoded == "HELLO", "Test failed!"
print("✓ Test 1 passed")

# Test 2: 3x3 matrix
matrix_3x3 = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
message = "CRYPTOGRAPHY"
encoded = encode_message(message, matrix_3x3)
decoded = decode_message(encoded, matrix_3x3)
assert "CRYPTOGRAPHY" in decoded, "Test failed!"
print("✓ Test 2 passed")
```

---

## 💡 Usage Tips

### Choosing Good Matrices:

1. **Start with small determinants** (1, 3, 5) for easier calculation
2. **Test your matrix** before using it extensively
3. **Keep a record** of your matrices if encrypting multiple messages
4. **Use integer values only** - no fractions or decimals

### Best Practices:

✅ **Validate matrix** before encoding important messages  
✅ **Store the key matrix** securely if you need to decode later  
✅ **Remove spaces** from message before encoding  
✅ **Use uppercase** for consistency  
✅ **Test with short messages** first to verify your matrix works  

### Example Valid Matrices:

**2x2 Matrices:**
```python
[[2, 3], [1, 1]]      # det = -1 ≡ 25 (mod 26)
[[3, 3], [2, 5]]      # det = 9 (mod 26)
[[5, 8], [17, 3]]     # det = -121 ≡ 9 (mod 26)
```

**3x3 Matrices:**
```python
[[6, 24, 1], [13, 16, 10], [20, 17, 15]]   # det ≡ 1 (mod 26)
[[2, 4, 12], [9, 1, 6], [7, 5, 3]]         # det ≡ 1 (mod 26)
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

### How to Contribute:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Add tests** if applicable
5. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
6. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

### Contribution Ideas:

- 🔹 Add support for larger matrices
- 🔹 Improve error messages
- 🔹 Create GUI interface
- 🔹 Add more unit tests
- 🔹 Optimize performance
- 🔹 Improve documentation
- 🔹 Add more examples
- 🔹 Fix bugs

---



## 📧 Contact

**Project Author:** Ibrahim Amin

- 📧 Email: 0ibrahim0amin@gmail.com
- 🐙 GitHub: @ibrahim-amin0(https://github.com/ibrahim-amin0)
- 💼 LinkedIn: Ibrahim Amin(www.linkedin.com/in/ibrahim-amin-aie0101010101)

---

## 🙏 Acknowledgments

- **Lester S. Hill** - Inventor of the Hill Cipher (1929)
- **NumPy Community** - For the excellent linear algebra library
- **Python Community** - For comprehensive documentation
- **Cryptography Resources:**
  - "The Code Book" by Simon Singh
  - "Introduction to Cryptography" by Johannes Buchmann

---

## 📚 Additional Resources

### Learn More About Hill Cipher:

- [Wikipedia: Hill Cipher](https://en.wikipedia.org/wiki/Hill_cipher)
- [Hill Cipher Tutorial](https://www.geeksforgeeks.org/hill-cipher/)
- [Linear Algebra in Cryptography](https://brilliant.org/wiki/hill-cipher/)

### Related Topics:

- Classical Cryptography
- Matrix Operations
- Modular Arithmetic
- Linear Algebra
- Cryptanalysis Techniques

---

## 📊 Project Statistics

- **Language:** Python 3.8+
- **Lines of Code:** ~80
- **Dependencies:** 1 (NumPy)
- **Functions:** 5
- **Matrix Sizes Supported:** 2x2, 3x3
- **Character Set:** A-Z (26 letters)

---

<div align="center">

### ⭐ If you found this project helpful, please give it a star!

**Made with ❤️ for Cryptography Enthusiasts**

🔐 **Remember**: Use modern encryption for real security needs! 🔐

</div>

---

## ❓ FAQ

**Q: Is Hill Cipher secure for real-world use?**  
A: No. Hill Cipher is a classical cipher from 1929 and is not secure against modern cryptanalysis. Use it for educational purposes only.

**Q: Why does my matrix need to have a determinant coprime with 26?**  
A: For the matrix to be invertible in modulo 26 arithmetic, its determinant must share no common factors with 26 (except 1).

**Q: Can I use matrices larger than 3x3?**  
A: The current implementation supports only 2x2 and 3x3 matrices, but you can modify the code to support larger matrices.

**Q: Why are there extra 'A' letters at the end of decoded messages?**  
A: These come from zero padding added during encoding to make the message length divisible by the matrix size.

**Q: How do I generate a valid random matrix?**  
A: Generate a random matrix, calculate its determinant mod 26, and check if gcd(det, 26) = 1. Repeat until you find a valid one.

**Q: Can I encrypt numbers and special characters?**  
A: The current implementation only handles letters A-Z. You would need to extend the character mapping to include other characters.

---

**Happy Encrypting! 🔐✨**
