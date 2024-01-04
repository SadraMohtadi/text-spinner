import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_rotating_text(text, offset):
    clear_screen()
    text_length = len(text)
    rotated_text = text[offset:] + text[:offset]
    print(rotated_text)
    time.sleep(0.5)

if __name__ == "__main__":
    input_text = input("Enter text: ")

    while True:
        for i in range(len(input_text)):
            print_rotating_text(input_text, i)
        for i in range(len(input_text)-2, 0, -1):
            print_rotating_text(input_text, i)
