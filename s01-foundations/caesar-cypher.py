#!/usr/bin/env python3

def caesar_decrypt(ciphertext):
    print("Ciphertext:", ciphertext)
    print("=" * 40)
    
    for shift in range(1, 26):
        decoded = ""
        for char in ciphertext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decoded += chr((ord(char) - base - shift) % 26 + base)
            else:
                decoded += char
        print("Shift -{:02d}: {}".format(shift, decoded))

if __name__ == "__main__":
    sample_ciphertext = "KDFNHU"
    caesar_decrypt(sample_ciphertext)
