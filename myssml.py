from ssml_builder.core import Speech
import re
from dataclasses import dataclass


class Builder:
    text: str = ""
    ZEN = "".join(chr(0xff01 + i) for i in range(94))
    HAN = "".join(chr(0x21 + i) for i in range(94))
    ZEN2HAN = str.maketrans(ZEN, HAN)

    def __init__(self, text):
        self.text = (text.strip('\n')+'<break time="3s"/>').translate(self.ZEN2HAN)
        print("init: " + self.text)


    # sub: 文字列の読み方を教える
    def sub(self, from_text, to_text):
        r = re.compile(from_text, re.IGNORECASE)
        self.text = re.sub(r, f"<sub alias=\"{to_text}\">{from_text}</sub>", self.text)

    # get: 変換結果を取得する
    def get(self):
        speech = Speech()
        return speech.add_text(self.text).speak()


if __name__ == "__main__":
    s = Builder(text="こんにちは。\nこんにちは。")
    s.sub("こん", "にゃあ")
    print(s.get())
