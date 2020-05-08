import text_to_speech
import argparse
from myssml import Builder

parser = argparse.ArgumentParser()
parser.add_argument("text", help="音声変換したい内容が入ったテキスト(SSML)")
parser.add_argument("output", help="出力ファイル名(存在していたら上書きします)")
args = parser.parse_args()

with open(args.text, "r") as f:
    t = Builder(text=f.read())
    t.sub("Kubernetes", "けーはちえす")
    t.sub("Ⅰ", "1")
    t.sub("Ⅱ", "2")
    t.sub("Ⅲ", "3")
    t.sub("Ⅳ", "4")
    t.sub("湯瀬", "ゆせ")

#    print(f"ssml:'{t.get()}'")
    text_to_speech.convert(t.get(), args.output)
