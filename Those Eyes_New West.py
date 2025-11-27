import time

def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

def print_lyrics():
    lyrics = [
        "Cause all of the small",
        "things that you do",
        "Are what remind me",
        "why I fell for you",
        "And when we're apart ",
        "and I'm missing you",
        "I close my eyes and all I see is you",
        "And the small things you do"
    ]

    
