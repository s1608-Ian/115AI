keys = list(map(int, input().split()))
ciphertext = input()

l = len(keys)
plaintext = []

for i, ch in enumerate(ciphertext):
    shift = keys[i % l]
    if 'A' <= ch <= 'Z':
        new_ch = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        plaintext.append(new_ch)
    elif 'a' <= ch <= 'z':
        new_ch = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        plaintext.append(new_ch)
    else:
        plaintext.append(ch)

print("".join(plaintext))
