



import colorama
import pyperclip


colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
RED = colorama.Fore.RED
LIGHTRED = colorama.Fore.LIGHTRED_EX

ZERO_WIDTH_SPACE = '\u200b'
ZERO_WIDTH_NON_JOINER = '\u200c'
ZERO_WIDTH_JOINER = '\u200d'
LEFT_TO_RIGHT_MARK = '\u200e'
RIGHT_TO_LEFT_MARK = '\u200f'
MIDDLE_DOT = '\u00b7'

padding = 11

zero_space_symbols = [
    ZERO_WIDTH_SPACE,
    ZERO_WIDTH_NON_JOINER,
    ZERO_WIDTH_JOINER,
    ]



def banner_ascii():
    """Print the app's title screen."""
    print("")
    print(f"\n{RED}               Steganography Tool{RESET}")
    print(f"{RED}                    Made By {RESET}")
    print(f"{RED}  Ehthe Samul Islam Laskar USN:1DS16CS712 {RESET}")
    print(f"{RED}  B Padma                  USN:1DS19CS420{RESET}")
    print(f"{RED}  Nikhil D Kanyal          USN:1DS17CS731{RESET}")
    print(f"{YELLOW}Type 'help' to see commands{RESET}")
   


def help():
    """Print the help menu."""
    print(f"{YELLOW}zwc{RESET} - Hidden messages using Zero Width Characters.")


banner_ascii()

# ZERO WIDTH CHARACTERS #

def to_base(num, b, numerals='0123456789abcdefghijklmnopqrstuvwxyz'):
    """Docstring TODO"""
    return ((num == 0) and numerals[0]) or (to_base(num // b, b, numerals).lstrip(numerals[0]) +
        numerals[num % b])


def encode_text():
    """Requests input string, encodes, then copies encoded text to clipboard."""
    print(f"{YELLOW}[{MIDDLE_DOT}]{RESET} Enter message to encode: ", end="")
    message = input()
    encoded = LEFT_TO_RIGHT_MARK
    for message_char in message:
        code = '{0}{1}'.format('0' * padding, int(str(to_base(
            ord(message_char), len(zero_space_symbols)))))
        code = code[len(code) - padding:]
        for code_char in code:
            index = int(code_char)
            encoded = encoded + zero_space_symbols[index]

    encoded += RIGHT_TO_LEFT_MARK

    pyperclip.copy(encoded)
    print(f"{GREEN}[+]{RESET} Encoded message copied to clipboard. {GREEN}[+]{RESET}")


def decode_text():
    """Requests encoded text, then displays decoded text."""
    print(f"{YELLOW}[{MIDDLE_DOT}]{RESET} Enter message to decode: ", end="")
    message = input()
    extract_encoded_message = message.split(LEFT_TO_RIGHT_MARK)[1]
    message = extract_encoded_message
    extract_encoded_message = message.split(RIGHT_TO_LEFT_MARK)[0]
    encoded = ''
    decoded = ''

    for message_char in message:
        if message_char in zero_space_symbols:
            encoded = encoded + str(zero_space_symbols.index(message_char))

    cur_encoded_char = ''

    for index, encoded_char in enumerate(encoded):
        cur_encoded_char = cur_encoded_char + encoded_char
        if index > 0 and (index + 1) % padding == 0:
            decoded = decoded + chr(int(cur_encoded_char, len(zero_space_symbols)))
            cur_encoded_char = ''

    return decoded


def hidden_message():
    """Launches text encoding or decoding."""
    print("")
    print(f"{YELLOW}[{MIDDLE_DOT}]{RESET} "
        "Choose ZWC option (1 - Encode / 2 - Decode): ", end="")
    option = int(input().lower())
    if option == 1:
        encode_text()
    elif option == 2:
        print(f"{GREEN}[+]{RESET} Decoded Message:  " + decode_text())




if __name__ == '__main__':
    while True:
        print(f'\n{RED}Steganography Tool: {RESET}', end='')
        command = input()
        cmd_splitted = command.split(' ', 1)

        if cmd_splitted[0] == "zwc":
            hidden_message()
 
        if cmd_splitted[0] == "help":
            help()
