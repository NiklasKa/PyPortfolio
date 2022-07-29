import collections

# morse code translation
MORSE_TRANS = collections.OrderedDict([
    ('A', '.-'),
    ('B', '-...'),
    ('C', '-.-.'),
    ('D', '-..'),
    ('E', '.'),
    ('F', '..-.'),
    ('G', '--.'),
    ('H', '....'),
    ('I', '..'),
    ('J', '.---'),
    ('K', '-.-'),
    ('L', '.-..'),
    ('M', '--'),
    ('N', '-.'),
    ('O', '---'),
    ('P', '.--.'),
    ('Q', '--.-'),
    ('R', '.-.'),
    ('S', '...'),
    ('T', '-'),
    ('U', '..-'),
    ('V', '...-'),
    ('W', '.--'),
    ('X', '-..-'),
    ('Y', '-.--'),
    ('Z', '--..'),
    ('0', '-----'),
    ('1', '.----'),
    ('2', '..---'),
    ('3', '...--'),
    ('4', '....-'),
    ('5', '.....'),
    ('6', '-....'),
    ('7', '--...'),
    ('8', '---..'),
    ('9', '----.'),
    (' ', '.......'),
    (',', '--..--'),
    ('.', '.-.-.-'),
    ('?', '..--..'),
    (';', '-.-.-.'),
    (':', '---...'),
    ("'", '.----.'),
    ('-', '-....-'),
    ('/', '-..-.'),
    ('(', '-.--.-'),
    (')', '-.--.-'),
    ('_', '..--.-')
])


def encode(message: str, seperator=' ') -> str:
    """ Convert String into Morse Code.

    The letter space is encoded with a small gap (see seperator).
    Space between words are represented with '.......'.

    >>> message = "Hello you"
    >>> encode(message)
    '.... . .-.. .-.. --- ....... -.-- --- ..-'

    >>> message = "Hello you"
    >>> encode(message, seperator=' ' * 3)
    '....   .   .-..   .-..   ---   .......   -.--   ---   ..-'

    Parameters
    ----------
    message : String
    seperator: String
        Space between each converted letter.

    Returns
    -------
    morse_code : String
        Converted Morse code.
    """
    message = message.strip()

    morse = [MORSE_TRANS.get(c.upper(), '?') for c in message]
    morse_code = seperator.join([s for s in morse])

    return morse_code
