from pyMorse.utils import encode

if __name__ == "__main__":
    message = input("Message:")
    print(f"Morse Code: {encode(message, seperator=' ' * 3)}")
