import mp3info as MP3
from ffmpeg import image as mpeg_image
from PIL import Image as jpeg_image


def encode(jpg, mp3, output):
    length = MP3.length(mp3)  # 動画の長さとなるベース
    mpeg_image.img_trans_video(jpg, str(length), output)


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("jpeg", help="紙芝居になるJPEGファイル")
    parser.add_argument("mp3", help="音声データ")
    parser.add_argument("output", help="出力先ファイル(MP4)")
    args = parser.parse_args()

    encode(
        args.jpeg,
        args.mp3,
        args.output
    )

