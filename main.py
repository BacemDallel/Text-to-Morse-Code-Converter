from morse_code import code


def text_to_morse(text):
    morse = ''
    for char in text.upper():
        if char in code:
            morse += code[char] + ' '
        else:
            morse += ' '

    return morse




user_text = input("Enter text to translate to Morse code: ")

morse_text = text_to_morse(user_text)

print(f'Morse code: {morse_text}')



