# MP3を受け取って再生時間を確認できるコード
from mutagen.mp3 import MP3


def length(file):
    mp3 = MP3(file)
    return mp3.info.length


if __name__ == "__main__":
    print(length("sample.mp3"))