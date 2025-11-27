import time

def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    print()

def print_lyrics():
    lyrics = [
        "It's my birthday",
        "I'ma do what I like",
        "I'ma wear what I like",
        "I'ma party tonight",
        "Goddamn, it's my birthday",
        "Everybody love me",
        "Yeah, yeah, yeah",
        "Look at me, give me money",
        "Damn, it's my birthday",
        "Everybody love me",
        "And I ain't thinkin' 'bout you",
        "It's my birthday"
    ]

    delays = [0.9, 0.4, 0.3 , 0.3, 0.3, 0.3, 0.3, 0.2, 0.3, 0.3, 0.4, 0.4]

    print("\n🎧 Now Playing: Anne-Marie - Birthday\n")
    time.sleep(1.5)
    for line, delay in zip(lyrics, delays):
        type_lyric(line)
        time.sleep(delay)

if __name__ == "__main__":
    print_lyrics()