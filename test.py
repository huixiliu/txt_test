# -*- coding: utf-8 -*-

def encrypt(text, shift):
    encrypted_text = []
    for char in text:
        # 对中文字符进行处理（这里只是简单的示例）
        if '\u4e00' <= char <= '\u9fff':
            encrypted_char = chr((ord(char) + shift - ord('\u4e00')) % (0x9fff - 0x4e00 + 1) + ord('\u4e00'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

# 设置移位值
shift = 3

# 逐行加密
with open('note.txt', 'r', encoding='utf-8') as infile, open('encrypted_utf8.txt', 'w', encoding='utf-8') as outfile:
    for line in infile:
        encrypted_line = encrypt(line, shift)
        outfile.write(encrypted_line)
