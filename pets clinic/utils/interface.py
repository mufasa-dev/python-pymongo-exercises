import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def text_yellow(text):
    return f"\033[93m{text}\033[m"

def text_blue(text):
    return f"\033[94m{text}\033[m"

def text_red(text):
    return f"\033[91m{text}\033[m"

def text_green(text):
    return f"\033[92m{text}\033[m"