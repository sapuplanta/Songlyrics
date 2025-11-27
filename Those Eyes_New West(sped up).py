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

    delays = [0.9, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 0.8]

    print("\n🎧 Now Playing: New West - Those Eyes\n")
    time.sleep(1.5)
    for line, delay in zip(lyrics, delays):
        type_lyric(line)
        time.sleep(delay)

if __name__ == "__main__":
    print_lyrics()

