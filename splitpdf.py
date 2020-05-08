from pdf2image import convert_from_path
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("file", help="分割したいPDFファイル")
args = parser.parse_args()

file = args.file

pages = convert_from_path(file)
for i, page in enumerate(pages):
    filename = f"{i+1:02}.jpg"
    page.save(filename)
